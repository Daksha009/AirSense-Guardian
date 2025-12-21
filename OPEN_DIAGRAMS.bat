@echo off
echo ========================================
echo Opening AirSense Guardian Diagrams
echo ========================================
echo.
echo Opening all diagram files in Notepad...
echo.
echo You can copy the content and paste it at:
echo   https://dreampuf.github.io/GraphvizOnline/
echo.
echo ========================================
echo.

start notepad "diagrams\confusion_matrix.dot"
timeout /t 1 /nobreak >nul

start notepad "diagrams\deployment_pipeline.dot"
timeout /t 1 /nobreak >nul

start notepad "diagrams\system_flowchart.dot"
timeout /t 1 /nobreak >nul

echo.
echo Opening online Graphviz viewer in browser...
start https://dreampuf.github.io/GraphvizOnline/

echo.
echo ========================================
echo All diagrams opened!
echo ========================================
echo.
echo Instructions:
echo 1. Copy content from each Notepad window
echo 2. Paste into the online viewer
echo 3. View and download as PNG/SVG
echo.
pause

