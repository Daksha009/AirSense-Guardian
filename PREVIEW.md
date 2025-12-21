# 🌬️ AirSense Guardian - Application Preview

## 🎨 UI Preview

### Main Dashboard Layout

```
┌─────────────────────────────────────────────────────────────┐
│  🌬️ AirSense Guardian                    [Live] 🟢         │
│  From Awareness to Action                                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  CURRENT AIR QUALITY                                  │  │
│  │  ┌────────────────────────────────────────────┐    │  │
│  │  │         AQI: 145                            │    │  │
│  │  │    Unhealthy for Sensitive 😷                │    │  │
│  │  └────────────────────────────────────────────┘    │  │
│  │                                                      │  │
│  │  PM2.5: 45.2 µg/m³  |  PM10: 80.5 µg/m³            │  │
│  │  Wind: 5.2 km/h     |  Humidity: 65%                │  │
│  │  Temperature: 25.5°C                                │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────┐  ┌──────────────────────┐      │
│  │  POLLUTION SOURCES    │  │  AQI PREDICTIONS      │      │
│  │                       │  │                       │      │
│  │  🚗 Traffic: 55%      │  │  [Chart showing      │      │
│  │  ████████████░░░░     │  │   next 3-6 hours]    │      │
│  │                       │  │                       │      │
│  │  🏭 Industry: 30%     │  │  Peak: 160 AQI       │      │
│  │  ██████░░░░░░░░░░     │  │  at 6 PM             │      │
│  │                       │  │                       │      │
│  │  🔥 Open Burning: 15% │  │                       │      │
│  │  ███░░░░░░░░░░░░░     │  │                       │      │
│  └──────────────────────┘  └──────────────────────┘      │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  🚀 RECOMMENDED ACTIONS                               │  │
│  │                                                       │  │
│  │  ┌──────────────┐  ┌──────────────┐  ┌────────────┐ │  │
│  │  │ 🚗 Carpool   │  │ 🚌 Public    │  │ ⚠️ Reduce  │ │  │
│  │  │              │  │    Transport │  │   Outdoor  │ │  │
│  │  │ Impact: 12% │  │ Impact: 15% │  │   Activity │ │  │
│  │  │ Time: 2-3h  │  │ Time: 1-2h  │  │ Immediate  │ │  │
│  │  └──────────────┘  └──────────────┘  └────────────┘ │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  ⚠️ ALERTS & WARNINGS                                 │  │
│  │                                                       │  │
│  │  🔴 HIGH: Current AQI is 145 - Unhealthy conditions │  │
│  │  🟡 MODERATE: High AQI (160) expected at 6 PM       │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## 🎯 Key Features Preview

### 1. **Current AQI Display**
- Large, color-coded AQI number
- Real-time status indicator
- Pollutant breakdown (PM2.5, PM10, NO₂)
- Weather information
- Location selector

### 2. **Source Attribution**
- Visual breakdown with icons
- Percentage bars
- Color-coded by source type
- Primary source highlighted

### 3. **Predictions Chart**
- Interactive line/area chart
- Shows next 3-6 hours
- Color-coded by AQI level
- Peak times highlighted

### 4. **Action Cards**
- Grid layout with cards
- Impact estimates
- Time to impact
- Feasibility indicators
- Hover effects

### 5. **Alerts Panel**
- Real-time warnings
- Severity levels (High/Moderate)
- Prediction alerts
- Timestamp information

## 🎨 Design Features

### Visual Elements:
- **Gradient Background**: Purple to pink gradient
- **Glass Morphism**: Frosted glass effect on cards
- **Smooth Animations**: Fade-in, slide-up effects
- **Responsive Design**: Works on mobile, tablet, desktop
- **Color Coding**: AQI levels with appropriate colors

### Interactive Elements:
- **Hover Effects**: Cards lift on hover
- **Live Updates**: Auto-refresh every 60 seconds
- **Location Input**: Change coordinates
- **API Testing**: Interactive docs at `/docs`

## 📊 Data Flow Preview

```
User Opens App
    ↓
Loading Screen (Animated Spinner)
    ↓
Fetch from FastAPI Backend
    ├─→ OpenAQ API (Real AQI Data)
    ├─→ Weather API (Optional)
    ├─→ ML Model (Predictions)
    ├─→ Source Attribution
    └─→ Action Engine
    ↓
Display Dashboard
    ├─→ AQI Card (Large Display)
    ├─→ Source Attribution (Side Panel)
    ├─→ Predictions Chart (Side Panel)
    ├─→ Action Cards (Grid)
    └─→ Alerts Panel (Full Width)
```

## 🚀 How to See the Preview

### Step 1: Start Backend
```bash
cd backend
python main.py
```
**Access**: `http://localhost:5000`
**API Docs**: `http://localhost:5000/docs` (Interactive!)

### Step 2: Start Frontend
```bash
cd frontend
npm start
```
**Access**: `http://localhost:3000`
**Auto-opens**: Browser opens automatically

### Step 3: Explore!

1. **Main Dashboard**: See all features
2. **API Docs**: Visit `http://localhost:5000/docs`
   - Test endpoints interactively
   - See request/response schemas
   - Try different locations

## 🎯 What You'll See

### On Load:
1. Beautiful gradient background
2. Animated loading spinner
3. Smooth fade-in of components
4. Real-time data display

### Interactive Features:
- **Change Location**: Edit lat/lon in AQI card
- **Hover Cards**: See hover effects
- **Live Updates**: Watch data refresh
- **API Testing**: Use `/docs` to test endpoints

## ✨ Highlights

- **Modern UI**: Glass morphism, gradients, animations
- **Real Data**: Fetches from OpenAQ API
- **ML Predictions**: 3-6 hour forecasts
- **Actionable Insights**: Specific recommendations
- **Interactive Docs**: Test API in browser

---

**Ready to preview!** Start both servers and see it in action! 🎉

