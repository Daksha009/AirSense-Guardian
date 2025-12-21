"""
Model Training Script for AirSense Guardian
Trains and validates AQI prediction model using real data
"""
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler
import pickle
import os
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class AQIModelTrainer:
    """Train and validate AQI prediction models"""
    
    def __init__(self, data_path: str = 'data/aqi_training_data.csv'):
        self.data_path = data_path
        self.model_dir = 'models'
        os.makedirs(self.model_dir, exist_ok=True)
        self.scaler = StandardScaler()
        self.best_model = None
        self.best_params = None
        
    def load_data(self) -> pd.DataFrame:
        """Load training data"""
        if not os.path.exists(self.data_path):
            print(f"Data file not found: {self.data_path}")
            print("Will generate synthetic training data...")
            return pd.DataFrame()  # Return empty DataFrame instead of None
        
        df = pd.read_csv(self.data_path)
        print(f"Loaded {len(df)} data points")
        return df
    
    def prepare_features(self, df: pd.DataFrame) -> tuple:
        """
        Prepare features and target for training
        Features: past_aqi, wind_speed, humidity, temperature, hour, day_of_week, month
        Target: future_aqi (next hour)
        """
        if df is None or df.empty:
            print("No data available for training. Generating synthetic data...")
            return self._generate_synthetic_features()
        
        # Ensure we have required columns
        required_cols = ['timestamp', 'aqi']
        if not all(col in df.columns for col in required_cols):
            print("Missing required columns. Generating synthetic data for training...")
            return self._generate_synthetic_features()
        
        # Convert timestamp
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
        df = df.dropna(subset=['timestamp'])
        df = df.sort_values('timestamp')
        
        # Create time-based features
        df['hour'] = df['timestamp'].dt.hour
        df['day_of_week'] = df['timestamp'].dt.dayofweek
        df['month'] = df['timestamp'].dt.month
        df['is_weekend'] = (df['day_of_week'] >= 5).astype(int)
        
        # Create lag features (past AQI values)
        df['aqi_lag1'] = df['aqi'].shift(1)
        df['aqi_lag2'] = df['aqi'].shift(2)
        df['aqi_lag3'] = df['aqi'].shift(3)
        
        # Create rolling averages
        df['aqi_rolling_mean_3h'] = df['aqi'].rolling(window=3, min_periods=1).mean()
        df['aqi_rolling_mean_6h'] = df['aqi'].rolling(window=6, min_periods=1).mean()
        
        # Create target: AQI for next hour
        df['future_aqi'] = df['aqi'].shift(-1)
        
        # Drop rows with NaN
        df = df.dropna()
        
        if len(df) < 100:
            print("Insufficient data. Generating synthetic data for training...")
            return self._generate_synthetic_features()
        
        # Select features
        feature_cols = [
            'aqi', 'aqi_lag1', 'aqi_lag2', 'aqi_lag3',
            'aqi_rolling_mean_3h', 'aqi_rolling_mean_6h',
            'hour', 'day_of_week', 'month', 'is_weekend'
        ]
        
        # Add weather features if available
        weather_cols = ['wind_speed', 'humidity', 'temperature', 'pressure']
        for col in weather_cols:
            if col in df.columns:
                feature_cols.append(col)
        
        # Fill missing values
        for col in feature_cols:
            if col in df.columns:
                df[col] = df[col].fillna(df[col].median())
        
        X = df[feature_cols].values
        y = df['future_aqi'].values
        
        # Remove any infinite or NaN values
        mask = np.isfinite(X).all(axis=1) & np.isfinite(y)
        X = X[mask]
        y = y[mask]
        
        print(f"Prepared {len(X)} samples with {X.shape[1]} features")
        return X, y, feature_cols
    
    def _generate_synthetic_features(self) -> tuple:
        """Generate synthetic training data when real data is insufficient"""
        print("Generating synthetic training data...")
        np.random.seed(42)
        n_samples = 5000
        
        # Generate realistic AQI patterns
        hours = np.random.randint(0, 24, n_samples)
        days = np.random.randint(0, 7, n_samples)
        months = np.random.randint(1, 13, n_samples)
        
        # Base AQI with time patterns
        base_aqi = 50 + 30 * np.sin(hours * np.pi / 12)  # Daily pattern
        base_aqi += 20 * np.sin(days * np.pi / 3.5)  # Weekly pattern
        base_aqi += np.random.normal(0, 15, n_samples)  # Random variation
        
        # Weather effects
        wind_speed = np.random.uniform(2, 15, n_samples)
        humidity = np.random.uniform(30, 90, n_samples)
        temperature = np.random.uniform(15, 35, n_samples)
        
        # Traffic effects (higher during rush hours)
        is_rush_hour = ((hours >= 7) & (hours <= 9)) | ((hours >= 17) & (hours <= 19))
        traffic_effect = np.where(is_rush_hour, 20, 5)
        
        # Future AQI
        future_aqi = base_aqi.copy()
        future_aqi -= wind_speed * 1.5  # Wind disperses pollution
        future_aqi += traffic_effect
        future_aqi += np.random.normal(0, 10, n_samples)
        future_aqi = np.clip(future_aqi, 0, 500)
        
        # Create lag features
        aqi_lag1 = np.roll(base_aqi, 1)
        aqi_lag2 = np.roll(base_aqi, 2)
        aqi_lag3 = np.roll(base_aqi, 3)
        
        # Rolling means
        aqi_rolling_mean_3h = (base_aqi + aqi_lag1 + aqi_lag2) / 3
        aqi_rolling_mean_6h = (base_aqi + aqi_lag1 + aqi_lag2 + aqi_lag3 + np.roll(base_aqi, 4) + np.roll(base_aqi, 5)) / 6
        
        is_weekend = (days >= 5).astype(int)
        
        X = np.column_stack([
            base_aqi, aqi_lag1, aqi_lag2, aqi_lag3,
            aqi_rolling_mean_3h, aqi_rolling_mean_6h,
            hours, days, months, is_weekend,
            wind_speed, humidity, temperature
        ])
        
        y = future_aqi
        
        feature_cols = [
            'aqi', 'aqi_lag1', 'aqi_lag2', 'aqi_lag3',
            'aqi_rolling_mean_3h', 'aqi_rolling_mean_6h',
            'hour', 'day_of_week', 'month', 'is_weekend',
            'wind_speed', 'humidity', 'temperature'
        ]
        
        return X, y, feature_cols
    
    def train_test_split_data(self, X: np.ndarray, y: np.ndarray, test_size: float = 0.2, val_size: float = 0.1):
        """Split data into train, validation, and test sets"""
        # First split: train+val vs test
        X_temp, X_test, y_temp, y_test = train_test_split(
            X, y, test_size=test_size, random_state=42, shuffle=False
        )
        
        # Second split: train vs val
        val_size_adjusted = val_size / (1 - test_size)
        X_train, X_val, y_train, y_val = train_test_split(
            X_temp, y_temp, test_size=val_size_adjusted, random_state=42, shuffle=False
        )
        
        print(f"Train set: {len(X_train)} samples")
        print(f"Validation set: {len(X_val)} samples")
        print(f"Test set: {len(X_test)} samples")
        
        return X_train, X_val, X_test, y_train, y_val, y_test
    
    def train_random_forest(self, X_train: np.ndarray, y_train: np.ndarray, 
                           X_val: np.ndarray, y_val: np.ndarray) -> RandomForestRegressor:
        """Train Random Forest model with hyperparameter tuning"""
        print("\n" + "="*60)
        print("Training Random Forest Model")
        print("="*60)
        
        # Hyperparameter grid
        param_grid = {
            'n_estimators': [50, 100, 200],
            'max_depth': [8, 10, 12, 15],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4]
        }
        
        # Base model
        base_model = RandomForestRegressor(random_state=42, n_jobs=-1)
        
        # Grid search with cross-validation
        print("Performing grid search for best hyperparameters...")
        grid_search = GridSearchCV(
            base_model,
            param_grid,
            cv=3,
            scoring='neg_mean_squared_error',
            n_jobs=-1,
            verbose=1
        )
        
        grid_search.fit(X_train, y_train)
        
        self.best_params = grid_search.best_params_
        self.best_model = grid_search.best_estimator_
        
        print(f"\nBest parameters: {self.best_params}")
        
        # Evaluate on validation set
        y_val_pred = self.best_model.predict(X_val)
        val_mse = mean_squared_error(y_val, y_val_pred)
        val_mae = mean_absolute_error(y_val, y_val_pred)
        val_r2 = r2_score(y_val, y_val_pred)
        
        print(f"\nValidation Set Performance:")
        print(f"  MSE: {val_mse:.2f}")
        print(f"  MAE: {val_mae:.2f}")
        print(f"  R² Score: {val_r2:.4f}")
        print(f"  RMSE: {np.sqrt(val_mse):.2f}")
        
        return self.best_model
    
    def evaluate_model(self, model, X_test: np.ndarray, y_test: np.ndarray):
        """Evaluate model on test set"""
        print("\n" + "="*60)
        print("Model Evaluation on Test Set")
        print("="*60)
        
        y_pred = model.predict(X_test)
        
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)
        
        # Calculate percentage error
        mape = np.mean(np.abs((y_test - y_pred) / (y_test + 1e-6))) * 100
        
        print(f"Test Set Performance:")
        print(f"  Mean Squared Error (MSE): {mse:.2f}")
        print(f"  Mean Absolute Error (MAE): {mae:.2f}")
        print(f"  Root Mean Squared Error (RMSE): {rmse:.2f}")
        print(f"  R² Score: {r2:.4f}")
        print(f"  Mean Absolute Percentage Error (MAPE): {mape:.2f}%")
        
        # Feature importance
        if hasattr(model, 'feature_importances_'):
            print(f"\nTop 5 Most Important Features:")
            importances = model.feature_importances_
            indices = np.argsort(importances)[::-1][:5]
            for i, idx in enumerate(indices, 1):
                print(f"  {i}. Feature {idx}: {importances[idx]:.4f}")
        
        return {
            'mse': mse,
            'mae': mae,
            'rmse': rmse,
            'r2': r2,
            'mape': mape
        }
    
    def save_model(self, model, feature_cols: list, metrics: dict):
        """Save trained model and metadata"""
        model_path = os.path.join(self.model_dir, 'aqi_model.pkl')
        
        # Save model
        with open(model_path, 'wb') as f:
            pickle.dump(model, f)
        
        # Save metadata
        metadata = {
            'feature_columns': feature_cols,
            'training_date': datetime.now().isoformat(),
            'metrics': metrics,
            'best_params': self.best_params
        }
        
        metadata_path = os.path.join(self.model_dir, 'model_metadata.json')
        import json
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        print(f"\nModel saved to {model_path}")
        print(f"Metadata saved to {metadata_path}")
    
    def train_full_pipeline(self):
        """Complete training pipeline"""
        print("="*60)
        print("AirSense Guardian - Model Training Pipeline")
        print("="*60)
        
        # Load data
        df = self.load_data()
        if df is None:
            return
        
        # Prepare features
        result = self.prepare_features(df)
        if result is None:
            return
        
        if len(result) == 3:
            X, y, feature_cols = result
        else:
            X, y = result
            feature_cols = [f'feature_{i}' for i in range(X.shape[1])]
        
        # Split data
        X_train, X_val, X_test, y_train, y_val, y_test = self.train_test_split_data(X, y)
        
        # Scale features (optional, but can help)
        # X_train_scaled = self.scaler.fit_transform(X_train)
        # X_val_scaled = self.scaler.transform(X_val)
        # X_test_scaled = self.scaler.transform(X_test)
        
        # Train model
        model = self.train_random_forest(X_train, y_train, X_val, y_val)
        
        # Evaluate on test set
        metrics = self.evaluate_model(model, X_test, y_test)
        
        # Save model
        self.save_model(model, feature_cols, metrics)
        
        print("\n" + "="*60)
        print("Training Complete!")
        print("="*60)


if __name__ == '__main__':
    trainer = AQIModelTrainer()
    trainer.train_full_pipeline()

