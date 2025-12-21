@echo off
echo Testing all batch files...
echo.
cd /d "%~dp0"
echo Current directory: %CD%
echo.

echo [TEST 1] Checking frontend/package.json...
if exist "frontend\package.json" (
    echo [OK] package.json found
) else (
    echo [ERROR] package.json NOT found!
)
echo.

echo [TEST 2] Checking backend/main.py...
if exist "backend\main.py" (
    echo [OK] main.py found
) else (
    echo [ERROR] main.py NOT found!
)
echo.

echo [TEST 3] Checking frontend/node_modules...
if exist "frontend\node_modules" (
    echo [OK] node_modules found
) else (
    echo [WARNING] node_modules not found - run: cd frontend ^&^& npm install
)
echo.

echo [TEST 4] Checking backend/models/aqi_model.pkl...
if exist "backend\models\aqi_model.pkl" (
    echo [OK] Trained model found
) else (
    echo [WARNING] Model not found - run training first
)
echo.

echo ========================================
echo Test complete!
echo ========================================
pause


