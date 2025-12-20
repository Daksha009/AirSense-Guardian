# 🌬️ AirSense Guardian

**"From Awareness to Action"**

AirSense Guardian is a community-driven air quality intelligence system that not only monitors and predicts pollution, but actively guides citizens and authorities to reduce it in real time.

## 🎯 Core Features

### 1. **Hyperlocal AQI Monitoring**
- Real-time air quality index (AQI) for any location
- PM2.5, PM10, and NO₂ measurements
- Weather data integration (wind speed, humidity, temperature)

### 2. **Source Attribution** 🔍
Instead of just showing AQI numbers, AirSense Guardian identifies the sources:
- 🚗 **Traffic**: Vehicle emissions (detected during high traffic + low wind)
- 🏭 **Industry**: Industrial activity (detected during night spikes)
- 🔥 **Open Burning**: Waste burning and stagnant air conditions
- 🌫️ **Other**: Additional sources

### 3. **Predictive Intelligence** 📊
- ML-powered AQI predictions for next 3-6 hours
- Uses Random Forest model trained on historical patterns
- Considers weather, traffic, and time-based factors

### 4. **Action Engine** 🚀
**This is what makes AirSense Guardian different!**

Instead of just saying "AQI = 210. Bad.", we provide actionable insights:

> "AQI is high because of traffic congestion + low wind speed.  
> If 15% people carpool in the next 2 hours → AQI can drop by ~12%."

The system generates specific, actionable recommendations with:
- Impact estimates (e.g., "12% AQI reduction")
- Time to impact (e.g., "2-3 hours")
- Feasibility ratings
- Real-time alerts for high-risk zones

## 🏗️ System Architecture

### Backend (Python Flask)
- **API Endpoints**: RESTful API for AQI data, predictions, and alerts
- **ML Model**: Random Forest regressor for AQI prediction
- **Data Sources**:
  - OpenAQ API for real AQI data
  - OpenWeatherMap API for weather data
  - Traffic density estimation (time-based heuristics)

### Frontend (React)
- Modern, responsive UI
- Real-time data visualization
- Interactive charts and graphs
- Action cards with recommendations

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm or yarn

### Model Training (Optional but Recommended)

Train the ML model with real data for better predictions:

```bash
cd backend
python run_training.py
```

This collects data from OpenAQ, AQICN, and EPA sources and trains the model. See [TRAINING_GUIDE.md](TRAINING_GUIDE.md) for detailed instructions.

**Note**: The system works with a pre-trained model if you skip this step.

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the backend directory (optional, for API keys):
```env
OPENAQ_API_KEY=your_openaq_key
WEATHER_API_KEY=your_openweathermap_key
GOOGLE_MAPS_API_KEY=your_google_maps_key
```

**Note**: The system works with mock data if API keys are not provided, perfect for demos!

5. Run the Flask server:
```bash
python app.py
```

The backend will run on `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

The frontend will run on `http://localhost:3000`

## 📡 API Endpoints

### `GET /api/health`
Health check endpoint

### `GET /api/aqi/current?lat={latitude}&lon={longitude}`
Get current AQI data, source attribution, predictions, and actions for a location

**Response:**
```json
{
  "current": {
    "aqi": 120,
    "pm25": 45.2,
    "pm10": 80.5,
    "no2": 30.1,
    "timestamp": "2024-01-15T10:30:00",
    "location": {"lat": 28.6139, "lon": 77.2090}
  },
  "weather": {
    "wind_speed": 5.2,
    "humidity": 65,
    "temperature": 25.5
  },
  "sources": {
    "traffic": 55.0,
    "industry": 30.0,
    "open_burning": 15.0,
    "other": 0.0
  },
  "predictions": [...],
  "actions": [...]
}
```

### `POST /api/aqi/predict`
Get AQI predictions for multiple hours ahead

### `GET /api/alerts?lat={latitude}&lon={longitude}`
Get pollution alerts and warnings

## 🎨 Key Differentiators

1. **Source Attribution**: Not just numbers, but understanding WHY pollution is high
2. **Actionable Insights**: Specific recommendations with impact estimates
3. **Predictive Intelligence**: Forecast pollution before it happens
4. **Community-Driven**: Designed to engage citizens and authorities

## 🛠️ Technology Stack

- **Backend**: Python, Flask, scikit-learn, pandas, numpy
- **Frontend**: React, Axios, Recharts
- **ML**: Random Forest Regressor with hyperparameter tuning
- **APIs**: OpenAQ, OpenWeatherMap, AQICN, EPA AirNow
- **Training**: Grid search, cross-validation, train/validation/test split

## 📝 Project Structure

```
.
├── backend/
│   ├── app.py                 # Flask API server
│   ├── data_collector.py     # Data collection from OpenAQ/AQICN/EPA
│   ├── train_model.py        # Model training pipeline
│   ├── run_training.py       # Complete training script
│   ├── models/
│   │   ├── predictor.py       # ML prediction model
│   │   ├── source_attribution.py
│   │   └── action_engine.py
│   ├── data/                  # Training data storage
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── components/
│   │   │   ├── AQICard.js
│   │   │   ├── SourceAttribution.js
│   │   │   ├── PredictionsChart.js
│   │   │   ├── ActionCards.js
│   │   │   └── AlertsPanel.js
│   │   └── ...
│   └── package.json
└── README.md
```

## 🎯 Hackathon Pitch Points

1. **Problem**: Air quality apps only show numbers, not solutions
2. **Solution**: AirSense Guardian provides actionable insights with impact estimates
3. **Innovation**: Source attribution + predictive ML + action engine
4. **Impact**: Real-time guidance to reduce pollution, not just monitor it
5. **Scalability**: Uses open APIs, no hardware needed

## 📄 License

This project is created for the Jaipuria Hack hackathon.

---

**Built with ❤️ for cleaner air and healthier communities**

