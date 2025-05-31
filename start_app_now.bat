@echo off
echo Starting Travel Advisory Bot...
cd /d "C:\DEV\Travel_Advisory_Bot\travel-advisory-bot"
echo Current directory: %CD%
echo.
echo Testing imports first...
python -c "from src.travel_bot.utils.travel_utils import TravelUtils; print('✅ TravelUtils OK')"
if errorlevel 1 (
    echo ❌ Import test failed
    pause
    exit /b 1
)
echo ✅ Import test passed
echo.
echo Starting Streamlit application...
python -m streamlit run src\travel_bot\ui\streamlit_app.py --server.port 8501
pause
