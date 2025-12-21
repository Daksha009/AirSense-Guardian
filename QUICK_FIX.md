# ⚡ QUICK FIX - Connection Error

## 🎯 **The Problem**
Your frontend is showing: **"Connection Error: Failed to fetch. Using demo data."**

**Reason:** The backend server is not running on port 5000.

---

## ✅ **THE FIX (2 Steps)**

### **Step 1: Start the Backend**

**Easiest way - Double-click this file:**
```
backend/START_BACKEND.bat
```

**OR manually:**
1. Open a **NEW** terminal/command prompt
2. Run:
   ```bash
   cd "C:\Users\iamda\OneDrive\Desktop\Jaipuria Hack\backend"
   python main.py
   ```
3. **Keep this terminal open!** You should see:
   ```
   INFO: Uvicorn running on http://0.0.0.0:5000
   ```

### **Step 2: Refresh Your Browser**

1. Go to: http://localhost:3001
2. **Press F5** or **Ctrl+R** to refresh
3. The error should disappear! ✅

---

## 🔍 **Verify It's Working**

Open in a new browser tab:
- http://localhost:5000/api/health

Should show:
```json
{"status":"healthy","message":"AirSense Guardian API is running"}
```

---

## 📋 **What You Should See**

### **In the Backend Terminal:**
```
INFO:     Started server process [XXXX]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:5000 (Press CTRL+C to quit)
```

### **In Your Browser:**
- ✅ No more "Connection Error"
- ✅ Real AQI data (not demo data)
- ✅ All features working

---

## 🎉 **That's It!**

Once the backend is running, your app will work perfectly!

**Backend:** http://localhost:5000  
**Frontend:** http://localhost:3001  
**Status:** ✅ Connected!

---

*Need help? Check FIX_CONNECTION_ERROR.md for detailed troubleshooting.*

