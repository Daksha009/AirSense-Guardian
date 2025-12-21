# 🔧 SOLUTION: Connection Error Fix

## ❌ **The Problem**
You're seeing: **"Connection Error: Failed to fetch. Using demo data."**

**This means:** The backend server is not running on port 5000.

---

## ✅ **THE FIX - 3 Simple Steps**

### **Step 1: Start the Backend**

**Double-click this file:**
```
START_BACKEND_NOW.bat
```

**OR use the backend batch file:**
```
backend/run_server.bat
```

**OR manually:**
1. Open Command Prompt
2. Run:
   ```bash
   cd "C:\Users\iamda\OneDrive\Desktop\Jaipuria Hack\backend"
   python main.py
   ```

### **Step 2: Wait for Server to Start**

In the terminal window, you should see:
```
INFO:     Started server process [XXXX]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:5000 (Press CTRL+C to quit)
```

**⏰ Wait until you see "Uvicorn running on http://0.0.0.0:5000"**

### **Step 3: Refresh Your Browser**

1. Go to: **http://localhost:3001** (or whatever port your frontend is on)
2. **Press F5** or **Ctrl+R** to refresh
3. **The error should disappear!** ✅

---

## 🔍 **Verify Backend is Running**

### **Method 1: Test in Browser**
Open: **http://localhost:5000/api/health**

Should show:
```json
{
  "status": "healthy",
  "message": "AirSense Guardian API is running"
}
```

### **Method 2: Use Verification Script**
Double-click: **VERIFY_BACKEND.bat**

---

## 📋 **What You Need**

You need **TWO things running simultaneously:**

1. ✅ **Backend Server** (port 5000)
   - Start with: `START_BACKEND_NOW.bat`
   - Keep the terminal window open!

2. ✅ **Frontend** (port 3001)
   - Already running in your browser

---

## 🎯 **Quick Checklist**

- [ ] Backend terminal window is open
- [ ] You see "Uvicorn running on http://0.0.0.0:5000"
- [ ] http://localhost:5000/api/health works in browser
- [ ] Browser refreshed at http://localhost:3001
- [ ] No more "Connection Error" message

---

## 🐛 **Troubleshooting**

### **Backend Won't Start?**

**Check 1: Are you in the right directory?**
```bash
cd "C:\Users\iamda\OneDrive\Desktop\Jaipuria Hack\backend"
```

**Check 2: Are dependencies installed?**
```bash
cd backend
pip install -r requirements.txt
```

**Check 3: Is port 5000 already in use?**
```bash
netstat -ano | findstr :5000
```
If something is using it, close that program.

### **Still Getting Error After Starting Backend?**

1. **Wait 10 seconds** after starting backend
2. **Verify backend is running:** http://localhost:5000/api/health
3. **Hard refresh browser:** Ctrl+Shift+R (or Ctrl+F5)
4. **Check browser console** (F12) for any errors

---

## ✅ **Success Indicators**

When it's working, you should see:
- ✅ No "Connection Error" message
- ✅ Real AQI data (not "demo data")
- ✅ All features loading (predictions, sources, actions)
- ✅ Backend terminal shows incoming requests

---

## 🎉 **You're Done!**

Once the backend is running and you've refreshed your browser, your AirSense Guardian app will be fully functional!

**Backend:** http://localhost:5000  
**Frontend:** http://localhost:3001  
**Status:** ✅ Connected!

---

*Need more help? The backend terminal window will show any errors if something goes wrong.*


