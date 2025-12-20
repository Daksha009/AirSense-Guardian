# 🎯 Model Training Guide

This guide explains how to train the AirSense Guardian AQI prediction model using real data from OpenAQ, AQICN, and EPA sources.

## 📊 Data Sources

The training pipeline collects data from:

1. **OpenAQ** (https://openaq.org) - Open air quality data platform
   - Free API access
   - Global coverage
   - Real-time and historical data

2. **AQICN/WAQI** (https://aqicn.org/data-platform/) - World Air Quality Index
   - Requires free API token registration
   - Covers 100+ countries
   - Historical data available

3. **EPA** (https://www.epa.gov/outdoor-air-quality-data) - US Environmental Protection Agency
   - US-focused data
   - AirNow API access

## 🚀 Quick Start

### Option 1: Full Pipeline (Recommended)

Run the complete training pipeline that collects data and trains the model:

```bash
cd backend
python run_training.py
```

This will:
1. Collect data from multiple sources
2. Preprocess and clean the data
3. Train the model with hyperparameter tuning
4. Validate and evaluate the model
5. Save the trained model

### Option 2: Step-by-Step

#### Step 1: Collect Data

```bash
cd backend
python data_collector.py
```

This collects AQI data and saves it to `backend/data/aqi_training_data.csv`

#### Step 2: Train Model

```bash
python train_model.py
```

This trains the model using the collected data and saves it to `backend/models/aqi_model.pkl`

## 📈 Model Features

The model uses the following features:

### Time-Based Features
- `hour` - Hour of day (0-23)
- `day_of_week` - Day of week (0-6)
- `month` - Month (1-12)
- `is_weekend` - Weekend indicator (0/1)

### AQI History Features
- `aqi` - Current AQI
- `aqi_lag1` - AQI 1 hour ago
- `aqi_lag2` - AQI 2 hours ago
- `aqi_lag3` - AQI 3 hours ago
- `aqi_rolling_mean_3h` - 3-hour rolling average
- `aqi_rolling_mean_6h` - 6-hour rolling average

### Weather Features
- `wind_speed` - Wind speed (km/h)
- `humidity` - Humidity (%)
- `temperature` - Temperature (°C)
- `pressure` - Atmospheric pressure (hPa)

### Target Variable
- `future_aqi` - AQI for the next hour

## 🔧 Hyperparameter Tuning

The training script automatically performs grid search to find optimal hyperparameters:

- **n_estimators**: [50, 100, 200]
- **max_depth**: [8, 10, 12, 15]
- **min_samples_split**: [2, 5, 10]
- **min_samples_leaf**: [1, 2, 4]

## 📊 Evaluation Metrics

The model is evaluated using:

- **MSE** (Mean Squared Error)
- **MAE** (Mean Absolute Error)
- **RMSE** (Root Mean Squared Error)
- **R² Score** (Coefficient of Determination)
- **MAPE** (Mean Absolute Percentage Error)

## 📁 Output Files

After training, you'll have:

1. **`backend/models/aqi_model.pkl`** - Trained model file
2. **`backend/models/model_metadata.json`** - Model metadata including:
   - Feature columns
   - Training date
   - Performance metrics
   - Best hyperparameters
3. **`backend/data/aqi_training_data.csv`** - Collected training data

## 🎛️ Customization

### Change Training Locations

Edit `backend/run_training.py` to add more locations:

```python
locations = [
    (28.6139, 77.2090, "Delhi"),      # Your location 1
    (19.0760, 72.8777, "Mumbai"),     # Your location 2
    # Add more locations...
]
```

### Adjust Data Collection Period

In `data_collector.py`, change the `days` parameter:

```python
openaq_df = collector.fetch_openaq_data(lat, lon, days=60)  # Collect 60 days
```

### Modify Model Parameters

Edit `train_model.py` to change:
- Train/validation/test split ratios
- Hyperparameter search space
- Model type (Random Forest, Gradient Boosting, etc.)

## 🔍 Understanding Results

### Good Model Performance Indicators:
- **R² Score > 0.7** - Model explains >70% of variance
- **MAPE < 15%** - Average prediction error < 15%
- **RMSE < 20** - Root mean squared error reasonable for AQI scale

### If Performance is Poor:
1. **Collect more data** - More training data = better model
2. **Add more features** - Weather, traffic, seasonal patterns
3. **Try different models** - Gradient Boosting, XGBoost, LSTM
4. **Feature engineering** - Create derived features

## 🐛 Troubleshooting

### "No data collected"
- Check internet connection
- Verify API endpoints are accessible
- OpenAQ API is free and doesn't require keys
- AQICN may require API token registration

### "Insufficient data for training"
- The script will automatically generate synthetic data
- For better results, collect more real data
- Try collecting from more locations

### "Model performance is low"
- This is normal with limited data
- The model will improve with more training data
- Synthetic data generation helps for demos

## 📝 Notes

- **First Run**: The model will use synthetic data if no real data is available
- **API Keys**: OpenAQ works without keys. AQICN and EPA may require registration
- **Data Quality**: Real-world AQI data can be sparse - the system handles this gracefully
- **Production**: For production use, collect data over weeks/months for best results

## 🎓 Next Steps

1. **Collect more data** - Run data collection regularly
2. **Retrain periodically** - Update model with new data
3. **Monitor performance** - Track prediction accuracy over time
4. **A/B testing** - Compare different model architectures

---

**Ready to train?** Run `python run_training.py` in the backend directory!

