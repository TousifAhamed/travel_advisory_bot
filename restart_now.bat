@echo off
echo Stopping any running Python processes...
taskkill /F /IM python.exe 2>nul

echo Waiting 2 seconds...
timeout /t 2 /nobreak >nul

echo Starting Travel Advisory Bot...
cd /d "c:\DEV\Travel_Advisory_Bot\travel-advisory-bot"
python -m streamlit run src/travel_bot/ui/streamlit_app.py --server.port 8501

pause
