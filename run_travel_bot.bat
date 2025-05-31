@echo off
echo ========================================
echo   Travel Advisory Bot Launcher
echo ========================================
echo.
echo Starting the application...
echo.

cd /d "c:\DEV\Travel_Advisory_Bot\travel-advisory-bot"

echo Checking Python version...
python --version

echo.
echo Checking Ollama status...
curl -s http://localhost:11434/api/tags | findstr "devstral" >nul
if %errorlevel%==0 (
    echo ✅ Devstral model is available
) else (
    echo ❌ Devstral model not found
    echo Please start Ollama and ensure Devstral is installed
    pause
    exit /b 1
)

echo.
echo Starting Streamlit application...
echo Application will be available at: http://localhost:8501
echo.
echo Press Ctrl+C to stop the application
echo ========================================

python -m streamlit run src\travel_bot\ui\streamlit_app.py --server.port 8501

pause
