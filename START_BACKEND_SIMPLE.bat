@echo off
title AirSense Guardian Backend Server
color 0A
echo.
echo ============================================================
echo          AirSense Guardian - Backend Server
echo ============================================================
echo.
echo Starting FastAPI server...
echo.
echo Server will be available at:
echo   - API: http://localhost:5000
echo   - Docs: http://localhost:5000/docs
echo.
echo Keep this window open while using the application!
echo.
echo ============================================================
echo.
cd /d "%~dp0backend"
python app.py
echo.
echo Server stopped. Press any key to exit...
pause >nul

