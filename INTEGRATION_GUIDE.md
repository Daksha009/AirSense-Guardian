# 🔗 Frontend-Backend Integration Guide

## ✅ Integration Complete!

The frontend and backend are now fully integrated with the ML model working.

## 🚀 Quick Start

### Option 1: Start Both Servers (Recommended)

**Windows:**
```bash
start_all.bat
```

**Manual:**
1. Terminal 1 - Backend:
```bash
cd backend
python app.py
```

2. Terminal 2 - Frontend:
```bash
cd frontend
npm start
```

## 📡 API Endpoints

The frontend now calls these Flask endpoints:

- `GET /api/health` - Health check
- `GET /api/aqi/current?lat={lat}&lon={lon}` - Get current AQI data
- `GET /api/alerts?lat={lat}&lon={lon}` - Get pollution alerts
- `POST /api/aqi/predict` - Get predictions

## 🔧 Configuration

### Backend (Flask)
- **Port**: 5000
- **CORS**: Enabled for frontend
- **Model**: Auto-loads trained model or creates synthetic one

### Frontend (React)
- **Port**: 3000
- **API URL**: `http://localhost:5000/api` (configurable via `.env`)

### Environment Variables

Create `frontend/.env`:
```env
REACT_APP_API_URL=http://localhost:5000/api
REACT_APP_WEATHER_API_KEY=your_key_optional
```

## 🧠 ML Model Status

The predictor model:
- ✅ **Auto-initializes** on backend start
- ✅ **Loads trained model** if `backend/models/aqi_model.pkl` exists
- ✅ **Creates synthetic model** if no trained model found
- ✅ **Works immediately** - no training required for demo

## 📊 Data Flow

```
Frontend (React)
    ↓ fetch()
Backend (Flask) - Port 5000
    ↓
├─→ OpenAQ API (AQI data)
├─→ Weather API (optional)
├─→ ML Model (predictions)
├─→ Source Attribution
└─→ Action Engine
    ↓ JSON Response
Frontend (Display)
```

## 🐛 Troubleshooting

### Backend won't start
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend can't connect
1. Check backend is running on port 5000
2. Check CORS is enabled
3. Verify API URL in frontend

### Model errors
- Model auto-creates on first run
- Check `backend/models/` directory
- Model saves automatically after creation

## ✨ Features Working

- ✅ Real-time AQI data from OpenAQ
- ✅ ML-powered predictions (3-6 hours)
- ✅ Source attribution (Traffic, Industry, etc.)
- ✅ Action recommendations with impact estimates
- ✅ Pollution alerts
- ✅ Weather integration

## 🎯 Next Steps

1. **Train Model**: Run `python backend/run_training.py` for better predictions
2. **Add API Keys**: Set weather API key for real weather data
3. **Deploy**: Both can be deployed separately

---

**Status**: ✅ Fully Integrated and Working!

