@echo off
title AirSense Guardian Backend - Port 5000
color 0A
cls
echo.
echo ============================================================
echo       AirSense Guardian - Backend Server Starting
echo ============================================================
echo.
echo Loading models and starting FastAPI server...
echo.
echo Once you see "Uvicorn running on http://0.0.0.0:5000"
echo the server is ready!
echo.
echo ============================================================
echo.
cd /d "%~dp0"
python app.py
echo.
echo Server stopped. Press any key to close...
pause >nul

