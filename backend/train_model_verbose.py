# Author: Daksha009
# Repo: https://github.com/Daksha009/AirSense-Guardian.git

"""
Enhanced Model Training Script with Live Progress
Shows detailed progress during training
"""
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pickle
import os
from datetime import datetime
import warnings
import json
import sys
import time
warnings.filterwarnings('ignore')

class ProgressTracker:
    """Track and display training progress"""
    def __init__(self):
        self.start_time = time.time()
        self.stage = ""
        
    def update(self, stage, message="", progress=None):
        """Update progress display"""
        elapsed = time.time() - self.start_time
        self.stage = stage
        
        if progress is not None:
            bar_length = 40
            filled = int(bar_length * progress)
            bar = "█" * filled + "░" * (bar_length - filled)
            print(f"\r[{bar}] {progress*100:.1f}% - {stage}: {message}", end="", flush=True)
        else:
            print(f"\n[{elapsed:.1f}s] {stage}: {message}")
    
    def complete(self, message=""):
        """Mark stage as complete"""
        elapsed = time.time() - self.start_time
        print(f"\n[OK] [{elapsed:.1f}s] {self.stage} Complete! {message}")

class AQIModelTrainerVerbose:
    """Train AQI model with verbose progress output"""
    
    def __init__(self, data_path: str = 'data/aqi_training_data.csv'):
        self.data_path = data_path
        self.model_dir = 'models'
        os.makedirs(self.model_dir, exist_ok=True)
        self.best_model = None
        self.best_params = None
        self.progress = ProgressTracker()
        
    def load_data(self) -> pd.DataFrame:
        """Load training data with progress"""
        self.progress.update("Loading Data", "Checking data file...")
        
        if not os.path.exists(self.data_path):
            self.progress.update("Loading Data", "Data file not found, generating synthetic data...")
            return pd.DataFrame()
        
        df = pd.read_csv(self.data_path)
        self.progress.complete(f"Loaded {len(df)} data points")
        return df
    
    def _generate_synthetic_features(self):
        """Generate synthetic training data with realistic patterns"""
        self.progress.update("Generating Data", "Creating synthetic dataset...")
        
        n_samples = 5000
        np.random.seed(42)
        
        # Generate timestamps
        start_date = datetime(2024, 1, 1)
        timestamps = [start_date + pd.Timedelta(hours=i) for i in range(n_samples)]
        
        # Generate realistic AQI patterns
        base_aqi = 100
        hourly_pattern = np.sin(np.arange(n_samples) * 2 * np.pi / 24) * 20  # Daily cycle
        weekly_pattern = np.sin(np.arange(n_samples) * 2 * np.pi / (24*7)) * 15  # Weekly cycle
        noise = np.random.normal(0, 10, n_samples)
        aqi_values = base_aqi + hourly_pattern + weekly_pattern + noise
        aqi_values = np.clip(aqi_values, 0, 500)  # Keep in valid range
        
        # Create features
        df = pd.DataFrame({
            'timestamp': timestamps,
            'aqi': aqi_values,
            'wind_speed': np.random.uniform(5, 25, n_samples),
            'humidity': np.random.uniform(30, 90, n_samples),
            'temperature': np.random.uniform(15, 35, n_samples),
            'pressure': np.random.uniform(990, 1020, n_samples)
        })
        
        # Create lag features
        df['aqi_lag1'] = df['aqi'].shift(1).fillna(df['aqi'].iloc[0])
        df['aqi_lag2'] = df['aqi'].shift(2).fillna(df['aqi'].iloc[0])
        df['aqi_lag3'] = df['aqi'].shift(3).fillna(df['aqi'].iloc[0])
        
        # Rolling means
        df['aqi_rolling_mean_3h'] = df['aqi'].rolling(window=3, min_periods=1).mean()
        df['aqi_rolling_mean_6h'] = df['aqi'].rolling(window=6, min_periods=1).mean()
        
        # Time features
        df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
        df['day_of_week'] = pd.to_datetime(df['timestamp']).dt.dayofweek
        df['month'] = pd.to_datetime(df['timestamp']).dt.month
        df['is_weekend'] = (df['day_of_week'] >= 5).astype(int)
        
        # Target: next hour AQI
        df['future_aqi'] = df['aqi'].shift(-1).fillna(df['aqi'].iloc[-1])
        
        # Select features
        feature_cols = [
            'aqi', 'aqi_lag1', 'aqi_lag2', 'aqi_lag3',
            'aqi_rolling_mean_3h', 'aqi_rolling_mean_6h',
            'hour', 'day_of_week', 'month', 'is_weekend',
            'wind_speed', 'humidity', 'temperature'
        ]
        
        X = df[feature_cols].values
        y = df['future_aqi'].values
        
        self.progress.complete(f"Generated {n_samples} synthetic samples")
        return X, y, feature_cols
    
    def prepare_features(self, df: pd.DataFrame) -> tuple:
        """Prepare features with progress tracking"""
        self.progress.update("Preparing Features", "Processing data...")
        
        if df is None or df.empty:
            return self._generate_synthetic_features()
        
        required_cols = ['timestamp', 'aqi']
        if not all(col in df.columns for col in required_cols):
            return self._generate_synthetic_features()
        
        # Convert timestamp
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
        df = df.dropna(subset=['timestamp'])
        df = df.sort_values('timestamp')
        
        # Create features
        df['hour'] = df['timestamp'].dt.hour
        df['day_of_week'] = df['timestamp'].dt.dayofweek
        df['month'] = df['timestamp'].dt.month
        df['is_weekend'] = (df['day_of_week'] >= 5).astype(int)
        
        df['aqi_lag1'] = df['aqi'].shift(1).fillna(df['aqi'].iloc[0])
        df['aqi_lag2'] = df['aqi'].shift(2).fillna(df['aqi'].iloc[0])
        df['aqi_lag3'] = df['aqi'].shift(3).fillna(df['aqi'].iloc[0])
        
        df['aqi_rolling_mean_3h'] = df['aqi'].rolling(window=3, min_periods=1).mean()
        df['aqi_rolling_mean_6h'] = df['aqi'].rolling(window=6, min_periods=1).mean()
        
        df['future_aqi'] = df['aqi'].shift(-1).fillna(df['aqi'].iloc[-1])
        df = df.dropna()
        
        if len(df) < 100:
            return self._generate_synthetic_features()
        
        feature_cols = [
            'aqi', 'aqi_lag1', 'aqi_lag2', 'aqi_lag3',
            'aqi_rolling_mean_3h', 'aqi_rolling_mean_6h',
            'hour', 'day_of_week', 'month', 'is_weekend'
        ]
        
        weather_cols = ['wind_speed', 'humidity', 'temperature']
        for col in weather_cols:
            if col in df.columns:
                feature_cols.append(col)
            else:
                df[col] = np.random.uniform(5, 25) if col == 'wind_speed' else \
                         np.random.uniform(30, 90) if col == 'humidity' else \
                         np.random.uniform(15, 35)
                feature_cols.append(col)
        
        X = df[feature_cols].values
        y = df['future_aqi'].values
        
        self.progress.complete(f"Prepared {len(X)} samples with {len(feature_cols)} features")
        return X, y, feature_cols
    
    def train_test_split_data(self, X, y):
        """Split data with progress"""
        self.progress.update("Splitting Data", "Creating train/val/test sets...")
        
        # First split: train+val vs test (80/20)
        X_train_val, X_test, y_train_val, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Second split: train vs val (87.5/12.5 of remaining 80% = 70/10 overall)
        X_train, X_val, y_train, y_val = train_test_split(
            X_train_val, y_train_val, test_size=0.125, random_state=42
        )
        
        self.progress.complete(f"Train: {len(X_train)}, Val: {len(X_val)}, Test: {len(X_test)}")
        return X_train, X_val, X_test, y_train, y_val, y_test
    
    def train_random_forest(self, X_train, y_train, X_val, y_val):
        """Train model with live progress"""
        print("\n" + "="*70)
        print("[TRAINING] Random Forest Model")
        print("="*70)
        
        param_grid = {
            'n_estimators': [50, 100, 200],
            'max_depth': [8, 10, 12, 15],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4]
        }
        
        total_combinations = np.prod([len(v) for v in param_grid.values()])
        print(f"[INFO] Testing {total_combinations} hyperparameter combinations...")
        print("[INFO] This may take a few minutes...\n")
        
        base_model = RandomForestRegressor(random_state=42, n_jobs=-1)
        
        grid_search = GridSearchCV(
            base_model,
            param_grid,
            cv=3,
            scoring='neg_mean_squared_error',
            n_jobs=-1,
            verbose=2  # Show progress
        )
        
        start_time = time.time()
        grid_search.fit(X_train, y_train)
        elapsed = time.time() - start_time
        
        self.best_params = grid_search.best_params_
        self.best_model = grid_search.best_estimator_
        
        print(f"\n[SUCCESS] Grid search completed in {elapsed:.1f} seconds")
        print(f"\n[BEST PARAMS] Best Parameters Found:")
        for param, value in self.best_params.items():
            print(f"   {param}: {value}")
        
        # Validate
        y_val_pred = self.best_model.predict(X_val)
        val_mse = mean_squared_error(y_val, y_val_pred)
        val_mae = mean_absolute_error(y_val, y_val_pred)
        val_r2 = r2_score(y_val, y_val_pred)
        val_rmse = np.sqrt(val_mse)
        
        print(f"\n[VALIDATION] Validation Set Performance:")
        print(f"   R² Score: {val_r2:.4f} ({val_r2*100:.2f}% variance explained)")
        print(f"   RMSE: {val_rmse:.2f} AQI points")
        print(f"   MAE: {val_mae:.2f} AQI points")
        print(f"   MSE: {val_mse:.2f}")
        
        return self.best_model
    
    def evaluate_model(self, model, X_test, y_test):
        """Evaluate with detailed metrics"""
        print("\n" + "="*70)
        print("[EVALUATION] Model Evaluation on Test Set")
        print("="*70)
        
        y_pred = model.predict(X_test)
        
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)
        mape = np.mean(np.abs((y_test - y_pred) / (y_test + 1e-6))) * 100
        
        print(f"\n[TEST RESULTS] Test Set Performance:")
        print(f"   R² Score: {r2:.4f} ({r2*100:.2f}% variance explained)")
        print(f"   RMSE: {rmse:.2f} AQI points")
        print(f"   MAE: {mae:.2f} AQI points")
        print(f"   MSE: {mse:.2f}")
        print(f"   MAPE: {mape:.2f}%")
        
        # Feature importance
        if hasattr(model, 'feature_importances_'):
            print(f"\n[FEATURES] Top 5 Most Important Features:")
            importances = model.feature_importances_
            indices = np.argsort(importances)[::-1][:5]
            for i, idx in enumerate(indices, 1):
                print(f"   {i}. Feature {idx}: {importances[idx]:.4f} ({importances[idx]*100:.2f}%)")
        
        return {
            'mse': float(mse),
            'mae': float(mae),
            'rmse': float(rmse),
            'r2': float(r2),
            'mape': float(mape)
        }
    
    def save_model(self, model, feature_cols, metrics):
        """Save model with confirmation"""
        self.progress.update("Saving Model", "Writing model files...")
        
        model_path = os.path.join(self.model_dir, 'aqi_model.pkl')
        with open(model_path, 'wb') as f:
            pickle.dump(model, f)
        
        metadata = {
            'feature_columns': feature_cols,
            'training_date': datetime.now().isoformat(),
            'metrics': metrics,
            'best_params': self.best_params
        }
        
        metadata_path = os.path.join(self.model_dir, 'model_metadata.json')
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        file_size = os.path.getsize(model_path) / (1024 * 1024)  # MB
        self.progress.complete(f"Model saved ({file_size:.2f} MB)")
    
    def train_full_pipeline(self):
        """Complete training pipeline with progress"""
        print("\n" + "="*70)
        print("AirSense Guardian - Model Training Pipeline")
        print("="*70)
        print(f"[START] Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        try:
            # Load data
            df = self.load_data()
            
            # Prepare features
            result = self.prepare_features(df)
            if len(result) == 3:
                X, y, feature_cols = result
            else:
                X, y = result
                feature_cols = [f'feature_{i}' for i in range(X.shape[1])]
            
            # Split data
            X_train, X_val, X_test, y_train, y_val, y_test = self.train_test_split_data(X, y)
            
            # Train model
            model = self.train_random_forest(X_train, y_train, X_val, y_val)
            
            # Evaluate
            metrics = self.evaluate_model(model, X_test, y_test)
            
            # Save
            self.save_model(model, feature_cols, metrics)
            
            total_time = time.time() - self.progress.start_time
            print("\n" + "="*70)
            print("[SUCCESS] Training Complete!")
            print("="*70)
            print(f"[TIME] Total time: {total_time:.1f} seconds ({total_time/60:.1f} minutes)")
            print(f"[SAVE] Model saved to: {os.path.join(self.model_dir, 'aqi_model.pkl')}")
            print(f"[SAVE] Metadata saved to: {os.path.join(self.model_dir, 'model_metadata.json')}")
            print("\n[READY] Model is ready to use!")
            
        except Exception as e:
            print(f"\n[ERROR] Error during training: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)

if __name__ == '__main__':
    trainer = AQIModelTrainerVerbose()
    trainer.train_full_pipeline()

