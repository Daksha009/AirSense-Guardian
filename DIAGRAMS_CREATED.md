# ✅ Graphviz Diagrams Created!

## 📊 **Three Diagrams Created**

I've created three comprehensive Graphviz diagrams for your AirSense Guardian project:

---

### 1. **Confusion Matrix** (`diagrams/confusion_matrix.dot`)
**Shows:**
- AQI prediction accuracy by category (Good, Moderate, Unhealthy, etc.)
- True Positive rates for each category
- Model performance metrics:
  - R² Score: 0.733 (73.3% variance explained)
  - RMSE: 10.56 AQI points
  - MAE: 8.39 AQI points
  - MAPE: 8.82%
- Overall accuracy breakdown

---

### 2. **Model Deployment Pipeline** (`diagrams/deployment_pipeline.dot`)
**Shows 6 stages:**

1. **Data Collection & Preparation**
   - OpenAQ API (AQI Data)
   - OpenWeatherMap (Weather Data)
   - Data Collector → CSV Storage

2. **Model Training**
   - Feature Engineering (Lags, Rolling Means, Time Features)
   - Train/Val/Test Split (70/15/15)
   - Hyperparameter Tuning (GridSearchCV)
   - Random Forest Training
   - Model Evaluation (R², RMSE, MAE)

3. **Model Persistence**
   - Save Model (aqi_model.pkl)
   - Save Metadata (model_metadata.json)

4. **Model Deployment**
   - Load Model (AQIPredictor)
   - Flask API (app.py)
   - API Endpoints (/current, /predict, /alerts)

5. **Production**
   - React Frontend
   - User Request → Real-time Data Fetch
   - AQI Prediction → JSON Response

6. **Monitoring & Updates**
   - Performance Monitoring
   - Periodic Retraining
   - Model Update (Version Control)

---

### 3. **System Flowchart** (`diagrams/system_flowchart.dot`)
**Shows complete system flow:**

- **User Journey:**
  - User Opens Application
  - React Frontend Loads
  - Default Location (Delhi)
  - User Input (Lat/Lon)

- **Backend Processing:**
  - API Request to Flask Backend
  - Fetch AQI Data (OpenAQ)
  - Fetch Weather Data (OpenWeatherMap)
  - Estimate Traffic Density

- **ML Models:**
  - Source Attribution (Traffic, Industry, Open Burning, Other)
  - AQI Predictor (Random Forest) - Predict Next 3-6 Hours
  - Action Engine (Generate Recommendations with Impact Estimates)

- **Response & Display:**
  - Alert Generation
  - Assemble JSON Response
  - Frontend Display:
    - AQI Card
    - Source Attribution Visualization
    - Predictions Chart
    - Action Cards
    - Alerts Panel

- **User Actions & Auto-refresh:**
  - Change Location
  - View Details
  - Auto-refresh Every 5 minutes

- **Error Handling:**
  - Fallback to Mock Data

---

## 🚀 **How to View/Generate Images**

### **Option 1: Online Tool (Easiest - No Installation)**
1. Go to: https://dreampuf.github.io/GraphvizOnline/
2. Copy the content from any `.dot` file
3. Paste into the online editor
4. View and download as PNG/SVG

### **Option 2: Install Graphviz (For Local Generation)**

**Windows:**
```bash
# Using Chocolatey
choco install graphviz

# Or download installer from:
# https://graphviz.org/download/
```

**Then generate images:**
```bash
# Confusion Matrix
dot -Tpng diagrams/confusion_matrix.dot -o diagrams/confusion_matrix.png

# Deployment Pipeline
dot -Tpng diagrams/deployment_pipeline.dot -o diagrams/deployment_pipeline.png

# System Flowchart
dot -Tpng diagrams/system_flowchart.dot -o diagrams/system_flowchart.png
```

**Or use the Python script:**
```bash
python generate_diagrams.py
```

### **Option 3: VS Code Extension**
Install "Graphviz Preview" extension in VS Code to view DOT files directly.

---

## 📁 **Files Created**

```
diagrams/
├── confusion_matrix.dot          # AQI prediction accuracy matrix
├── deployment_pipeline.dot        # Model deployment pipeline
├── system_flowchart.dot          # Complete system flowchart
└── README.md                     # Detailed documentation

generate_diagrams.py              # Python script to generate images
```

---

## 🎨 **Diagram Features**

- ✅ **Professional styling** with colors and shapes
- ✅ **Clear labels** and descriptions
- ✅ **Complete flow** from data to production
- ✅ **Error handling** paths shown
- ✅ **Model metrics** included
- ✅ **Easy to customize** (edit DOT files)

---

## 📊 **Use Cases**

These diagrams are perfect for:
- 📝 **Documentation** - Technical documentation
- 🎤 **Presentations** - Visual aids for demos
- 📋 **Reports** - Project reports and submissions
- 🎓 **Explanations** - Explaining system architecture
- 🔍 **Debugging** - Understanding data flow

---

## ✅ **Status**

All three diagrams are **ready to use**! 

You can:
1. View them online (no installation needed)
2. Install Graphviz to generate PNG/SVG images
3. Customize them by editing the DOT files

**Diagrams created successfully!** 🎉

---

*Created: 2025-12-20*

