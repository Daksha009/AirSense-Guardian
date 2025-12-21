@echo off
echo Checking if backend is running...
echo.
curl -s http://localhost:5000/api/health >nul 2>&1
if %errorlevel% == 0 (
    echo [SUCCESS] Backend IS running on port 5000!
    echo.
    echo Open in browser: http://localhost:5000/api/health
    echo.
) else (
    echo [ERROR] Backend is NOT running on port 5000
    echo.
    echo Please start the backend first:
    echo   1. Double-click: START_BACKEND_NOW.bat
    echo   2. Wait for "Uvicorn running" message
    echo   3. Then refresh your browser
    echo.
)
pause


