# 🛠️ AirSense Guardian - Technology Stack

## Overview
AirSense Guardian is built with a modern, full-stack architecture using Python for the backend and React for the frontend, with machine learning capabilities for air quality prediction.

---

## 🎨 Frontend Stack

### Core Framework
- **React** `^18.2.0` - Modern UI library for building interactive user interfaces
- **React DOM** `^18.2.0` - React rendering for web browsers
- **React Scripts** `5.0.1` - Build tools and configuration for Create React App

### Styling & UI
- **Tailwind CSS** `^3.4.19` - Utility-first CSS framework for rapid UI development
- **PostCSS** `^8.5.6` - CSS transformation tool
- **Autoprefixer** `^10.4.23` - Automatic vendor prefixing for CSS

### Data Visualization
- **Recharts** `^2.10.0` - Composable charting library built on React and D3
  - Used for: AQI predictions area charts, trend visualizations

### Icons
- **Lucide React** `^0.294.0` - Beautiful, customizable icon library
  - Used for: Wind, Temperature, Humidity, Alerts, Trends, and other UI icons

### HTTP Client
- **Native Fetch API** - Modern browser API for HTTP requests (no external dependency needed)

### Development Tools
- **ESLint** - Code linting and quality assurance
- **Browserslist** - Share target browsers configuration

---

## ⚙️ Backend Stack

### Core Framework
- **FastAPI** `0.115.0` - Modern, fast web framework for building APIs with Python
  - Automatic interactive API documentation (Swagger UI)
  - Type validation with Pydantic
  - Async support
- **Uvicorn** `0.32.0` - Lightning-fast ASGI server
  - Standard workers for production deployment

### Alternative Backend (Legacy)
- **Flask** - Lightweight WSGI web framework (available in `app.py`)

### Machine Learning & Data Science
- **scikit-learn** `1.3.2` - Machine learning library
  - Random Forest Regressor for AQI prediction
  - Model training, validation, and evaluation
  - Grid search for hyperparameter tuning
- **NumPy** `1.24.3` - Numerical computing library
  - Array operations, mathematical functions
- **Pandas** `2.0.3` - Data manipulation and analysis
  - Data collection, processing, and cleaning
  - CSV handling for training data
- **SciPy** `1.11.4` - Scientific computing library
  - Statistical functions and algorithms

### HTTP & API Integration
- **Requests** `2.31.0` - HTTP library for making API calls
  - Used for: OpenAQ, OpenWeatherMap, AQICN, EPA APIs

### Configuration & Environment
- **python-dotenv** `1.0.0` - Load environment variables from `.env` files
- **Pydantic** `2.9.2` - Data validation using Python type annotations
  - Request/response validation
  - Type safety

### Utilities
- **python-multipart** `0.0.12` - Support for multipart form data

---

## 🤖 Machine Learning

### Model Type
- **Random Forest Regressor** - Ensemble learning method for AQI prediction
  - Multiple decision trees
  - Handles non-linear relationships
  - Feature importance analysis

### Training Pipeline
- **Grid Search** - Hyperparameter optimization
- **Cross-Validation** - Model validation technique
- **Train/Validation/Test Split** - Data partitioning for model evaluation

### Features Used
- Historical AQI data
- Weather parameters (wind speed, humidity, temperature)
- Time-based features (hour, day of week, season)
- Traffic patterns (estimated)
- Location data (latitude, longitude)

---

## 🌐 External APIs & Data Sources

### Air Quality Data
- **OpenAQ API** - Global air quality data
  - Real-time and historical measurements
  - PM2.5, PM10, NO₂, O₃, SO₂, CO
- **AQICN (World Air Quality Index)** - International air quality data
  - Coverage for multiple countries
- **EPA AirNow API** - US Environmental Protection Agency data
  - US-specific air quality monitoring

### Weather Data
- **OpenWeatherMap API** - Weather information
  - Wind speed, humidity, temperature
  - Weather forecasts

### Optional Services
- **Google Maps API** - Location services (optional)
  - Geocoding, reverse geocoding

---

## 🗄️ Data Storage

### File-Based Storage
- **CSV Files** - Training data storage (`backend/data/aqi_training_data.csv`)
- **Pickle Files** - Trained model persistence (`backend/models/aqi_model.pkl`)

### Data Collection
- Real-time API fetching
- Historical data aggregation
- Multi-source data fusion

---

## 🏗️ Architecture

### Backend Architecture
```
FastAPI Application
├── API Endpoints (/api/aqi/current, /api/alerts, etc.)
├── ML Models
│   ├── AQIPredictor (Random Forest)
│   ├── SourceAttribution (Rule-based)
│   └── ActionEngine (Recommendation system)
├── Data Collection
│   └── Multi-source AQI data fetching
└── CORS Middleware (for frontend integration)
```

### Frontend Architecture
```
React Application
├── Components
│   ├── AQICard (Main AQI display)
│   ├── SourceAttribution (Pollution sources)
│   ├── PredictionsChart (ML predictions)
│   ├── ActionCards (Recommendations)
│   └── AlertsPanel (Warnings)
├── Services (API integration)
└── Styling (Tailwind CSS)
```

---

## 🚀 Deployment & Development

### Development
- **React Development Server** - Hot reload, development tools
- **Uvicorn** - FastAPI development server with auto-reload
- **Environment Variables** - `.env` file for API keys

### Build Tools
- **Create React App** - React build configuration
- **Webpack** (via React Scripts) - Module bundling
- **Babel** (via React Scripts) - JavaScript transpilation

### Production Considerations
- **Static Frontend Build** - `npm run build` generates optimized production build
- **ASGI Server** - Uvicorn with multiple workers for production
- **CORS Configuration** - Configurable for production domains

---

## 📦 Package Management

### Frontend
- **npm** - Node Package Manager
- **package.json** - Dependency management

### Backend
- **pip** - Python Package Installer
- **requirements.txt** - Python dependencies

---

## 🎯 Key Technologies Summary

| Category | Technology | Purpose |
|----------|-----------|---------|
| **Frontend Framework** | React 18 | UI component library |
| **Styling** | Tailwind CSS | Utility-first CSS framework |
| **Charts** | Recharts | Data visualization |
| **Icons** | Lucide React | Icon library |
| **Backend Framework** | FastAPI | Modern Python web framework |
| **Server** | Uvicorn | ASGI server |
| **ML Library** | scikit-learn | Machine learning |
| **Data Processing** | Pandas, NumPy | Data manipulation |
| **HTTP Client** | Requests | API calls |
| **Validation** | Pydantic | Data validation |

---

## 🔧 Development Environment

### Required Versions
- **Python**: 3.8+
- **Node.js**: 14+
- **npm**: Latest stable

### Optional Tools
- **Git** - Version control
- **VS Code / Cursor** - Code editor
- **Postman / Insomnia** - API testing (FastAPI provides `/docs`)

---

## 📝 Additional Notes

- **No Database Required** - Uses file-based storage and real-time API fetching
- **Mock Data Support** - Works without API keys for demos
- **CORS Enabled** - Frontend can communicate with backend
- **Type Safety** - Pydantic models for backend, PropTypes for frontend
- **Responsive Design** - Mobile-first approach with Tailwind CSS
- **Modern ES6+** - JavaScript/TypeScript features throughout

---

**Last Updated**: December 2024
**Project Version**: 1.0.0
