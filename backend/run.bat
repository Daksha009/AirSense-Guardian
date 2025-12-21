@echo off
cd /d "%~dp0"
echo Starting AirSense Guardian Backend (FastAPI)...
echo Current directory: %CD%
python app.py
pause

