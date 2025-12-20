import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from datetime import datetime, timedelta
import pickle
import os
import json

class AQIPredictor:
    def __init__(self):
        self.model = None
        self.feature_cols = None
        self.metadata = None
        # Model path - save in backend/models directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.model_path = os.path.join(script_dir, 'aqi_model.pkl')
        self.metadata_path = os.path.join(script_dir, 'model_metadata.json')
        self._initialize_model()
    
    def _initialize_model(self):
        """Initialize or load the prediction model"""
        if os.path.exists(self.model_path):
            try:
                with open(self.model_path, 'rb') as f:
                    self.model = pickle.load(f)
                
                # Load metadata if available
                if os.path.exists(self.metadata_path):
                    with open(self.metadata_path, 'r') as f:
                        self.metadata = json.load(f)
                        self.feature_cols = self.metadata.get('feature_columns', None)
                
                print("Loaded trained model from file")
            except Exception as e:
                print(f"Error loading model: {e}. Creating new model...")
                self.model = self._create_model()
                self._train_with_synthetic_data()
        else:
            print("No trained model found. Creating model with synthetic data...")
            self.model = self._create_model()
            self._train_with_synthetic_data()
    
    def _create_model(self):
        """Create a new Random Forest model"""
        return RandomForestRegressor(
            n_estimators=100,
            max_depth=10,
            random_state=42,
            n_jobs=-1
        )
    
    def _train_with_synthetic_data(self):
        """Train model with synthetic data (for demo purposes)"""
        # Generate synthetic training data
        np.random.seed(42)
        n_samples = 1000
        
        # Features: past_aqi, wind_speed, humidity, traffic_density, hour, day_of_week
        X = np.random.rand(n_samples, 6)
        X[:, 0] = X[:, 0] * 300  # past_aqi: 0-300
        X[:, 1] = X[:, 1] * 20   # wind_speed: 0-20 km/h
        X[:, 2] = X[:, 2] * 100  # humidity: 0-100%
        X[:, 3] = X[:, 3]        # traffic_density: 0-1
        X[:, 4] = X[:, 4] * 24   # hour: 0-23
        X[:, 5] = X[:, 5] * 7    # day_of_week: 0-6
        
        # Target: future_aqi (with some logic)
        y = X[:, 0].copy()  # Start with past AQI
        
        # Apply effects
        y -= X[:, 1] * 2  # Higher wind reduces AQI
        y += (1 - X[:, 3]) * 30  # Higher traffic increases AQI
        y += np.sin(X[:, 4] * np.pi / 12) * 20  # Time of day effect
        
        # Add noise
        y += np.random.normal(0, 10, n_samples)
        y = np.clip(y, 0, 500)  # Clamp to valid AQI range
        
        # Train model
        self.model.fit(X, y)
        
        # Save model
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
        with open(self.model_path, 'wb') as f:
            pickle.dump(self.model, f)
    
    def _prepare_features(self, current_aqi, wind_speed, humidity, traffic_density, current_time, 
                         aqi_history=None):
        """
        Prepare features for prediction based on model's expected features
        """
        hour = current_time.hour
        day_of_week = current_time.weekday()
        month = current_time.month
        is_weekend = 1 if day_of_week >= 5 else 0
        
        # If we have feature columns from trained model, use them
        if self.feature_cols:
            # Create feature vector matching trained model
            features = {}
            
            # Current AQI and lags
            features['aqi'] = current_aqi
            if aqi_history and len(aqi_history) >= 3:
                features['aqi_lag1'] = aqi_history[-1] if len(aqi_history) > 0 else current_aqi
                features['aqi_lag2'] = aqi_history[-2] if len(aqi_history) > 1 else current_aqi
                features['aqi_lag3'] = aqi_history[-3] if len(aqi_history) > 2 else current_aqi
            else:
                features['aqi_lag1'] = current_aqi
                features['aqi_lag2'] = current_aqi
                features['aqi_lag3'] = current_aqi
            
            # Rolling means
            if aqi_history and len(aqi_history) >= 3:
                features['aqi_rolling_mean_3h'] = np.mean(aqi_history[-3:])
            else:
                features['aqi_rolling_mean_3h'] = current_aqi
            
            if aqi_history and len(aqi_history) >= 6:
                features['aqi_rolling_mean_6h'] = np.mean(aqi_history[-6:])
            else:
                features['aqi_rolling_mean_6h'] = current_aqi
            
            # Time features
            features['hour'] = hour
            features['day_of_week'] = day_of_week
            features['month'] = month
            features['is_weekend'] = is_weekend
            
            # Weather features
            features['wind_speed'] = wind_speed
            features['humidity'] = humidity
            features['temperature'] = 25  # Default if not available
            features['pressure'] = 1013  # Default if not available
            
            # Build feature array in correct order
            feature_array = []
            for col in self.feature_cols:
                if col in features:
                    feature_array.append(features[col])
                else:
                    # Default value for missing features
                    feature_array.append(0)
            
            return np.array([feature_array])
        else:
            # Fallback to simple features (for backward compatibility)
            return np.array([[
                current_aqi,
                wind_speed,
                humidity,
                traffic_density,
                hour,
                day_of_week
            ]])
    
    def predict(self, current_aqi, wind_speed, humidity, traffic_density, current_time, aqi_history=None):
        """Predict AQI for next 3 hours"""
        predictions = []
        current_aqi_val = current_aqi
        
        for i in range(1, 4):
            # Prepare features
            features = self._prepare_features(
                current_aqi_val, wind_speed, humidity, traffic_density, 
                current_time + timedelta(hours=i-1), aqi_history
            )
            
            # Predict
            pred_aqi = self.model.predict(features)[0]
            pred_time = current_time + timedelta(hours=i)
            
            predictions.append({
                'time': pred_time.isoformat(),
                'aqi': float(np.clip(pred_aqi, 0, 500)),
                'hours_ahead': i
            })
            
            # Update for next prediction
            current_aqi_val = pred_aqi
            if aqi_history is not None:
                aqi_history = list(aqi_history) + [pred_aqi]
        
        return predictions
    
    def predict_multiple_hours(self, current_aqi, wind_speed, humidity, traffic_density, current_time, hours=6, aqi_history=None):
        """Predict AQI for multiple hours ahead"""
        predictions = []
        current_aqi_val = current_aqi
        
        for i in range(1, hours + 1):
            # Prepare features
            features = self._prepare_features(
                current_aqi_val, wind_speed, humidity, traffic_density,
                current_time + timedelta(hours=i-1), aqi_history
            )
            
            # Predict
            pred_aqi = self.model.predict(features)[0]
            pred_time = current_time + timedelta(hours=i)
            
            # Update hour for next iteration
            next_hour = (current_time.hour + i) % 24
            
            predictions.append({
                'time': pred_time.isoformat(),
                'aqi': float(np.clip(pred_aqi, 0, 500)),
                'hours_ahead': i
            })
            
            # Use predicted AQI for next prediction
            current_aqi_val = pred_aqi
            if aqi_history is not None:
                aqi_history = list(aqi_history) + [pred_aqi]
        
        return predictions
