@echo off
title AirSense Guardian Backend Server
color 0A
cls
echo.
echo ============================================================
echo          AirSense Guardian - Backend Server
echo ============================================================
echo.
echo Starting server on port 5000...
echo.
echo IMPORTANT: Keep this window open!
echo.
echo Once you see "Running on http://127.0.0.1:5000"
echo the server is ready. Then refresh your browser!
echo.
echo ============================================================
echo.
cd /d "%~dp0backend"
python app.py
echo.
echo Server stopped.
pause

