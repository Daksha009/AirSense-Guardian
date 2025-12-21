@echo off
cd /d "%~dp0"
echo Starting AirSense Guardian - Full Stack
echo Current directory: %CD%
echo.
echo Starting FastAPI Backend Server...
start "Backend Server" cmd /k "cd /d %~dp0backend && python app.py"
timeout /t 3 /nobreak >nul
echo.
echo Starting Frontend...
start "Frontend" cmd /k "cd /d %~dp0frontend && npm start"
echo.
echo Both servers are starting!
echo Backend: http://localhost:5000
echo API Docs: http://localhost:5000/docs
echo Frontend: http://localhost:3000
pause
