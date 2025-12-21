# 🚀 How to Start the Backend Server

## ✅ **EASIEST WAY - Use the Batch File**

### **Option 1: Double-Click (Recommended)**
1. **Find this file in your project root:**
   ```
   START_BACKEND_SIMPLE.bat
   ```

2. **Double-click it**
   - A green terminal window will open
   - The server will start automatically
   - **Keep this window open!**

3. **Wait for this message:**
   ```
   INFO: Uvicorn running on http://0.0.0.0:5000
   ```

4. **Refresh your browser** at http://localhost:3001

---

## ✅ **Option 2: Manual Start**

### **Step 1: Open Terminal**
Open Command Prompt or PowerShell

### **Step 2: Navigate to Backend**
```bash
cd "C:\Users\iamda\OneDrive\Desktop\Jaipuria Hack\backend"
```

### **Step 3: Start Server**
```bash
python main.py
```

### **Step 4: Wait for Startup**
You should see:
```
INFO:     Started server process [XXXX]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:5000
```

### **Step 5: Keep Terminal Open**
**Don't close this terminal!** The server runs here.

---

## 🔍 **Verify It's Working**

### **Test 1: Health Check**
Open in browser: http://localhost:5000/api/health

Should show:
```json
{
  "status": "healthy",
  "message": "AirSense Guardian API is running"
}
```

### **Test 2: API Documentation**
Open in browser: http://localhost:5000/docs

Should show FastAPI interactive documentation.

---

## ✅ **After Backend Starts**

1. **Go to your frontend:** http://localhost:3001
2. **Press F5** to refresh
3. **The connection error should disappear!**
4. **You'll see real AQI data** instead of demo data

---

## 🎯 **What You Need Running**

You need **TWO things** running:

1. ✅ **Backend** (port 5000) - Start this now using the batch file above
2. ✅ **Frontend** (port 3001) - Already running

---

## 🐛 **Troubleshooting**

### **"python: can't open file" Error?**
You're in the wrong directory! Make sure you're in:
```
C:\Users\iamda\OneDrive\Desktop\Jaipuria Hack\backend
```

### **"Module not found" Error?**
Install dependencies:
```bash
cd backend
pip install -r requirements.txt
```

### **Port 5000 Already in Use?**
Something else is using port 5000. Find and close it:
```bash
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

---

## 📋 **Quick Checklist**

- [ ] Backend terminal window is open
- [ ] You see "Uvicorn running on http://0.0.0.0:5000"
- [ ] http://localhost:5000/api/health works
- [ ] Browser refreshed at http://localhost:3001
- [ ] No more "Connection Error" message

---

## 🎉 **Success!**

Once you see "Uvicorn running on http://0.0.0.0:5000" in the terminal, your backend is ready!

**Refresh your browser and enjoy your working application!** 🚀

---

*Need more help? Check FIX_CONNECTION_ERROR.md*

