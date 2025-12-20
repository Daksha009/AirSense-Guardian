# AirSense Guardian - Frontend

Pure JavaScript/React frontend with no backend required!

## 🚀 Features

- **No Flask Backend**: All logic runs in the browser
- **Direct API Calls**: Fetches data directly from OpenAQ, Weather APIs
- **Client-Side ML**: Predictions run in JavaScript
- **Zero Backend Dependencies**: Works as a static site

## 📦 Installation

```bash
npm install
```

## 🎯 Running

```bash
npm start
```

The app will run on `http://localhost:3000`

## 🔧 Configuration

### Optional: Weather API Key

For real weather data (instead of mock), create a `.env` file:

```env
REACT_APP_WEATHER_API_KEY=your_openweathermap_api_key
```

Get a free API key from: https://openweathermap.org/api

**Note**: The app works perfectly without this - it uses mock weather data.

## 📁 Project Structure

```
src/
├── services/           # All backend logic (pure JavaScript)
│   ├── aqiService.js      # OpenAQ data fetching
│   ├── sourceAttribution.js  # Source attribution logic
│   ├── predictor.js        # AQI prediction model
│   ├── actionEngine.js    # Action generation
│   └── index.js           # Main service exports
├── components/        # React components
│   ├── AQICard.js
│   ├── SourceAttribution.js
│   ├── PredictionsChart.js
│   ├── ActionCards.js
│   └── AlertsPanel.js
└── App.js            # Main app component
```

## 🌐 API Usage

### OpenAQ API
- **Free**: No API key required
- **Rate Limits**: Generous free tier
- **Documentation**: https://openaq.org/#/api

### Weather API (Optional)
- **Service**: OpenWeatherMap
- **Free Tier**: 60 calls/minute
- **Sign Up**: https://openweathermap.org/api

## 🎨 Technologies

- **React** - UI framework
- **Recharts** - Data visualization
- **Lucide React** - Icons
- **Fetch API** - HTTP requests (native browser API)

## 🚀 Deployment

This is a static React app - deploy anywhere:

- **Netlify**: `npm run build` then drag `build/` folder
- **Vercel**: Connect GitHub repo
- **GitHub Pages**: Use `gh-pages` package
- **Any Static Host**: Upload `build/` folder

## 📝 Notes

- All data fetching happens client-side
- No CORS issues (OpenAQ supports CORS)
- Works offline (with cached data)
- Fast and responsive

---

**No backend needed!** Everything runs in the browser. 🎉

