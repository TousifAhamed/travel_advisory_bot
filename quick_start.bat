@echo off
echo Travel Advisory Bot - Quick Start
echo ===============================

cd /d "c:\DEV\Travel_Advisory_Bot\travel-advisory-bot"

echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo Testing imports...
python -c "import sys; sys.path.insert(0, 'src'); sys.path.insert(0, '.'); from travel_bot.travel_bot import TravelBot; print('✅ TravelBot imported successfully')"

if %ERRORLEVEL% NEQ 0 (
    echo ❌ Import test failed
    pause
    exit /b 1
)

echo ✅ Import test passed!
echo.
echo Starting Streamlit app...
python streamlit_launcher.py

pause
