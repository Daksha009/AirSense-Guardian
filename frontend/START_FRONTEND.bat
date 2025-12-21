@echo off
title AirSense Guardian - Frontend Server
color 0A
cls
echo.
echo ============================================================
echo          AirSense Guardian - Frontend Server
echo ============================================================
echo.
echo Starting frontend server on port 3000...
echo.
echo IMPORTANT: Make sure backend is running on port 5000!
echo.
echo The frontend will be available at:
echo   http://localhost:3000
echo.
echo ============================================================
echo.
cd /d "%~dp0"
python server.py
echo.
echo Server stopped.
pause

