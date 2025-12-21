@echo off
title AirSense Guardian - Full Application
color 0B
cls
echo.
echo ============================================================
echo       AirSense Guardian - Starting Full Application
echo ============================================================
echo.
echo This will start both backend and frontend servers.
echo.
echo IMPORTANT: Keep both windows open!
echo.
echo ============================================================
echo.
echo Starting Backend Server (Port 5000)...
echo.
start "AirSense Guardian Backend" cmd /k "cd /d %~dp0backend && python app.py"
timeout /t 5 /nobreak >nul
echo.
echo Starting Frontend Server (Port 3000)...
echo.
start "AirSense Guardian Frontend" cmd /k "cd /d %~dp0frontend && python server.py"
echo.
echo ============================================================
echo.
echo Both servers are starting!
echo.
echo Backend:  http://localhost:5000
echo Frontend: http://localhost:3000
echo.
echo Wait for both servers to fully start, then open:
echo   http://localhost:3000
echo.
echo ============================================================
echo.
pause

