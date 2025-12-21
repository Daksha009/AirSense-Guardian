# 🚀 AirSense Guardian - Running Instructions

## ✅ **Application Status**

Your application should now be running! Here's how to access it:

---

## 🌐 **Access Points**

### **1. Frontend (User Interface)**
```
http://localhost:3000
```
- Open this in your web browser
- This is your main application interface
- Shows real-time AQI, predictions, sources, and actions

### **2. Backend API**
```
http://localhost:5000
```

### **3. Interactive API Documentation**
```
http://localhost:5000/docs
```
- FastAPI automatic documentation
- Test all API endpoints here
- See request/response schemas

### **4. Alternative API Docs**
```
http://localhost:5000/redoc
```

---

## 🔍 **Verify Servers Are Running**

### **Check Backend (Port 5000)**
Open in browser: http://localhost:5000/api/health

Expected response:
```json
{
  "status": "healthy",
  "message": "AirSense Guardian API is running"
}
```

### **Check Frontend (Port 3000)**
Open in browser: http://localhost:3000

You should see the AirSense Guardian interface with:
- Current AQI card
- Source attribution
- Predictions chart
- Action cards
- Alerts panel

---

## 🛠️ **Manual Start (If Needed)**

If servers didn't start automatically:

### **Start Backend:**
```bash
cd backend
python main.py
```

### **Start Frontend (in new terminal):**
```bash
cd frontend
npm start
```

---

## 📋 **API Endpoints**

### **Get Current AQI**
```
GET http://localhost:5000/api/aqi/current?lat=28.6139&lon=77.2090
```

### **Get Predictions**
```
POST http://localhost:5000/api/aqi/predict
Content-Type: application/json

{
  "lat": 28.6139,
  "lon": 77.2090,
  "hours": 6
}
```

### **Get Alerts**
```
GET http://localhost:5000/api/alerts?lat=28.6139&lon=77.2090
```

---

## 🎯 **Features Available**

✅ **Real-time AQI Monitoring**
- Current air quality index
- PM2.5, PM10, NO2 levels

✅ **Source Attribution**
- Traffic pollution
- Industrial sources
- Open burning
- Weather impact

✅ **Predictions**
- Next 3-6 hours forecast
- ML-powered predictions
- Trend analysis

✅ **Action Engine**
- Personalized recommendations
- Impact estimates
- Priority actions

✅ **Alerts**
- High pollution warnings
- Health advisories
- Prediction alerts

---

## 🛑 **Stop Servers**

1. **Close the terminal windows** where servers are running
2. **Or press `Ctrl+C`** in each terminal
3. **Or use Task Manager** to end Python/Node processes

---

## 🐛 **Troubleshooting**

### **Backend not starting?**
- Check if port 5000 is already in use
- Make sure you're in the `backend` directory
- Verify Python dependencies: `pip install -r requirements.txt`

### **Frontend not starting?**
- Check if port 3000 is already in use
- Make sure you're in the `frontend` directory
- Verify Node dependencies: `npm install`

### **Connection errors?**
- Make sure backend is running before frontend
- Check CORS settings in `backend/main.py`
- Verify API URL in `frontend/src/App.js`

---

## ✅ **Quick Test**

1. Open http://localhost:3000 in your browser
2. The app should automatically fetch AQI data for Delhi (default location)
3. You should see:
   - Current AQI value
   - Color-coded health status
   - Source breakdown
   - Prediction chart
   - Action recommendations
   - Alerts (if any)

---

## 🎉 **You're All Set!**

Your AirSense Guardian application is now running!

**Backend:** FastAPI on port 5000  
**Frontend:** React on port 3000  
**Model:** Trained and loaded  
**Status:** ✅ Ready to use!

---

*Happy coding! 🚀*

