@echo off
cd /d "%~dp0"
echo Starting AirSense Guardian Frontend...
echo Current directory: %CD%
cd frontend
if not exist package.json (
    echo ERROR: package.json not found in frontend directory!
    echo Current path: %CD%
    pause
    exit /b 1
)
echo Starting React development server...
npm start
pause

