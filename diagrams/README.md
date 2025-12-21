# 📊 AirSense Guardian - Graphviz Diagrams

This directory contains Graphviz DOT files for visualizing the AirSense Guardian system architecture and model performance.

## 📁 Files

### 1. **confusion_matrix.dot**
- AQI prediction accuracy matrix
- Model performance metrics (R², RMSE, MAE, MAPE)
- Category-wise accuracy breakdown

### 2. **deployment_pipeline.dot**
- Complete model deployment pipeline
- From data collection to production
- 6 stages: Data → Training → Storage → Deployment → Production → Monitoring

### 3. **system_flowchart.dot**
- System architecture flowchart
- User journey from frontend to backend
- Data flow and processing steps
- Error handling paths

---

## 🚀 How to Generate Images

### **Prerequisites**
Install Graphviz:
```bash
# Windows (using Chocolatey)
choco install graphviz

# Or download from: https://graphviz.org/download/
```

### **Generate Images**

#### **Option 1: Using Command Line**
```bash
# Confusion Matrix
dot -Tpng diagrams/confusion_matrix.dot -o diagrams/confusion_matrix.png

# Deployment Pipeline
dot -Tpng diagrams/deployment_pipeline.dot -o diagrams/deployment_pipeline.png

# System Flowchart
dot -Tpng diagrams/system_flowchart.dot -o diagrams/system_flowchart.png
```

#### **Option 2: Using Python**
```python
import graphviz

# Confusion Matrix
with open('diagrams/confusion_matrix.dot', 'r') as f:
    dot_data = f.read()
graph = graphviz.Source(dot_data)
graph.render('diagrams/confusion_matrix', format='png')

# Deployment Pipeline
with open('diagrams/deployment_pipeline.dot', 'r') as f:
    dot_data = f.read()
graph = graphviz.Source(dot_data)
graph.render('diagrams/deployment_pipeline', format='png')

# System Flowchart
with open('diagrams/system_flowchart.dot', 'r') as f:
    dot_data = f.read()
graph = graphviz.Source(dot_data)
graph.render('diagrams/system_flowchart', format='png')
```

#### **Option 3: Online Tools**
- Copy the DOT file content
- Paste at: https://dreampuf.github.io/GraphvizOnline/
- Download the generated image

---

## 📊 Diagram Details

### **Confusion Matrix**
Shows:
- AQI category predictions (Good, Moderate, Unhealthy, etc.)
- True Positive rates for each category
- Overall model accuracy (R²: 0.73)
- Performance metrics (RMSE: 10.56, MAPE: 8.82%)

### **Deployment Pipeline**
Shows:
1. **Data Collection**: OpenAQ, OpenWeatherMap APIs
2. **Model Training**: Feature engineering, hyperparameter tuning
3. **Model Persistence**: Save model and metadata
4. **Deployment**: Flask API with endpoints
5. **Production**: React frontend integration
6. **Monitoring**: Performance tracking and retraining

### **System Flowchart**
Shows:
- User interaction flow
- API request/response cycle
- Data fetching from external APIs
- ML model processing (Source Attribution, Predictor, Action Engine)
- Frontend component rendering
- Error handling and auto-refresh

---

## 🎨 Customization

You can edit the DOT files to:
- Change colors (fillcolor attributes)
- Modify node shapes (shape attributes)
- Adjust layout (rankdir, rank attributes)
- Add/remove nodes and edges
- Update labels and text

---

## 📝 Notes

- All diagrams use Arial font for consistency
- Colors are chosen for clarity and accessibility
- Layout optimized for readability
- Can be exported to PNG, SVG, PDF, or other formats

---

*Generated for AirSense Guardian - 2025-12-20*

