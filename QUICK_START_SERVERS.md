# 🚀 Quick Start - Run Servers

## ✅ **Frontend Server is Already Running!**

The frontend server is running on port 3000. You can access it at:
**http://localhost:3000**

---

## 📋 **How to Run Servers**

### **Option 1: Use Batch Files (Easiest)**

**Backend:**
- Double-click: `RUN_BACKEND.bat`

**Frontend:**
- Double-click: `RUN_FRONTEND.bat`

---

### **Option 2: Manual Commands**

**Backend (from project root):**
```bash
cd backend
python app.py
```

**Frontend (from project root):**
```bash
cd frontend
python server.py
```

---

### **Option 3: Start Both at Once**

**Double-click:** `START_FULL_APP.bat`

---

## 🌐 **Access Your Application**

Once both servers are running:

**Open:** http://localhost:3000

---

## ✅ **Current Status**

- ✅ Frontend server: **Running on port 3000**
- ⚠️ Backend server: Check if running on port 5000

---

## 🔍 **Check Server Status**

**Backend:**
```bash
netstat -ano | findstr ":5000"
```

**Frontend:**
```bash
netstat -ano | findstr ":3000"
```

---

## 🛑 **To Stop Servers**

Press `Ctrl+C` in the terminal windows.

---

**Your frontend is ready! Make sure backend is also running.** 🎉

