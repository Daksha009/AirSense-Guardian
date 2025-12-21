@echo off
title AirSense Guardian - Presentation Mode
color 0B
cls
echo.
echo ============================================================
echo       AirSense Guardian - Starting for Presentation
echo ============================================================
echo.
echo This will start both backend and frontend servers.
echo.
echo IMPORTANT: Keep both windows open during presentation!
echo.
echo ============================================================
echo.
echo Starting Backend Server (Port 5000)...
echo.
start "AirSense Guardian Backend" cmd /k "cd /d %~dp0backend && if exist app.py (python app.py) else (echo ERROR: app.py not found! && pause)"
timeout /t 5 /nobreak >nul
echo.
echo Starting Frontend Server (Port 3000)...
echo.
start "AirSense Guardian Frontend" cmd /k "cd /d %~dp0frontend && if exist package.json (npm start) else (echo ERROR: package.json not found! && echo Current directory: %CD% && pause)"
echo.
echo ============================================================
echo.
echo Both servers are starting!
echo.
echo Backend:  http://localhost:5000
echo API Docs: http://localhost:5000/docs
echo Frontend: http://localhost:3000
echo.
echo Wait for both servers to fully start, then open:
echo   http://localhost:3000
echo.
echo ============================================================
echo.
pause

