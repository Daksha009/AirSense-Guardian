@echo off
echo ========================================
echo   AirSense Guardian - Starting Preview
echo ========================================
echo.

echo [1/2] Starting FastAPI Backend...
cd /d "%~dp0"
start "AirSense Backend" cmd /k "cd /d %~dp0backend && if exist app.py (python app.py) else (echo ERROR: app.py not found! && pause)"
timeout /t 5 /nobreak >nul

echo [2/2] Starting React Frontend...
start "AirSense Frontend" cmd /k "cd /d %~dp0frontend && if exist package.json (npm start) else (echo ERROR: package.json not found! && pause)"
timeout /t 3 /nobreak >nul

echo.
echo ========================================
echo   Preview Starting!
echo ========================================
echo.
echo Backend API: http://localhost:5000
echo API Docs:    http://localhost:5000/docs
echo Frontend:    http://localhost:3000
echo.
echo The browser will open automatically!
echo.
pause

