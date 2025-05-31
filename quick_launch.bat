@echo off
echo ========================================
echo   Travel Advisory Bot - Quick Launch
echo ========================================

cd /d "%~dp0"

echo [1/3] Installing Streamlit if needed...
python -m pip install streamlit python-dotenv --quiet

echo [2/3] Checking project structure...
if not exist "src\travel_bot\ui\streamlit_app.py" (
    echo ERROR: Streamlit app not found!
    pause
    exit /b 1
)

echo [3/3] Starting the application...
echo.
echo 🌐 Opening browser to: http://localhost:8501
echo ⏹️  Press Ctrl+C to stop the application
echo.

python -m streamlit run "src\travel_bot\ui\streamlit_app.py" --server.port 8501 --server.headless false

pause
