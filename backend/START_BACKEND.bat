@echo off
echo ========================================
echo Starting AirSense Guardian Backend
echo ========================================
echo.
cd /d "%~dp0"
echo Current directory: %CD%
echo.
echo Starting Flask server on port 5000...
echo.
echo The server will be available at:
echo   - API: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.
python app.py
pause

