# 🌐 View Diagrams Online - Quick Guide

## ✅ **Diagrams Opened in Notepad**

I've opened all three DOT files in Notepad. You can:
1. **Copy the content** from each file
2. **Paste it online** to view as images

---

## 🚀 **Quick Online Viewing**

### **Step 1: Go to Online Viewer**
👉 **https://dreampuf.github.io/GraphvizOnline/**

### **Step 2: Copy & Paste**

#### **Confusion Matrix:**
- Open: `diagrams/confusion_matrix.dot`
- Copy all content (Ctrl+A, Ctrl+C)
- Paste into online viewer

#### **Deployment Pipeline:**
- Open: `diagrams/deployment_pipeline.dot`
- Copy all content
- Paste into online viewer

#### **System Flowchart:**
- Open: `diagrams/system_flowchart.dot`
- Copy all content
- Paste into online viewer

---

## 📊 **What Each Diagram Shows**

### **1. Confusion Matrix**
- AQI prediction accuracy by category
- Model metrics (R²: 0.73, RMSE: 10.56)
- True positive rates

### **2. Deployment Pipeline**
- 6-stage deployment process
- From data collection to production
- Complete ML pipeline

### **3. System Flowchart**
- Complete system architecture
- User journey and data flow
- All components and connections

---

## 💡 **Alternative: Install Graphviz**

To generate PNG images locally:

```bash
# Install Graphviz
choco install graphviz

# Then generate images
dot -Tpng diagrams/confusion_matrix.dot -o diagrams/confusion_matrix.png
dot -Tpng diagrams/deployment_pipeline.dot -o diagrams/deployment_pipeline.png
dot -Tpng diagrams/system_flowchart.dot -o diagrams/system_flowchart.png
```

---

**All diagrams are ready to view!** 🎉

