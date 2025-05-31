@echo off
echo Starting Travel Advisory Bot with new AI models...
cd /d "c:\DEV\Travel_Advisory_Bot\travel-advisory-bot"
set PYTHONPATH=%cd%\src
streamlit run src/travel_bot/ui/streamlit_app.py --server.port 8501
pause
