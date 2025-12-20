# 🚀 Quick Start Guide

Get AirSense Guardian running in 5 minutes!

## Step 1: Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py
```

✅ Backend should now be running on `http://localhost:5000`

## Step 2: Frontend Setup

Open a **new terminal window** and:

```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Start the development server
npm start
```

✅ Frontend should now be running on `http://localhost:3000`

## Step 3: Test It!

1. Open your browser to `http://localhost:3000`
2. You should see the AirSense Guardian dashboard
3. The default location is set to Delhi (28.6139, 77.2090)
4. You can change the coordinates in the AQI card

## 🎯 What You'll See

- **Current AQI**: Real-time air quality with color-coded status
- **Source Attribution**: Breakdown of pollution sources (Traffic, Industry, etc.)
- **Predictions**: 3-6 hour AQI forecast
- **Action Cards**: Specific recommendations with impact estimates
- **Alerts**: Real-time warnings for high pollution zones

## 💡 Pro Tips

1. **No API Keys Needed**: The system works with mock data for demos
2. **Change Location**: Edit lat/lon in the AQI card to test different locations
3. **Auto-Refresh**: Data updates every 60 seconds automatically
4. **Responsive**: Works on mobile, tablet, and desktop

## 🐛 Troubleshooting

### Backend won't start
- Make sure Python 3.8+ is installed
- Check if port 5000 is already in use
- Verify all dependencies are installed: `pip install -r requirements.txt`

### Frontend won't start
- Make sure Node.js 14+ is installed
- Check if port 3000 is already in use
- Try deleting `node_modules` and running `npm install` again

### API Connection Error
- Make sure backend is running on port 5000
- Check browser console for CORS errors
- The system will use mock data if API calls fail (this is normal for demos!)

## 🎉 You're Ready!

Your AirSense Guardian is now running. Perfect for hackathon demos!

---

**Need help?** Check the main README.md for detailed documentation.

