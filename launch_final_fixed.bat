@echo off
echo 🚀 Starting Travel Advisory Bot - Final Launch
echo Python 3.13 Compatible Version with Devstral AI
echo ===============================================

cd /d "c:\DEV\Travel_Advisory_Bot\travel-advisory-bot"
set PYTHONPATH=%cd%\src

echo Setting up environment...
echo Python path: %PYTHONPATH%

echo Testing basic imports...
python -c "import sys; sys.path.append('src'); from travel_bot.models.ai_models import DevstralModel; print('✅ AI models ready')"

echo Starting Streamlit application...
streamlit run src\travel_bot\ui\streamlit_app.py --server.port 8501

pause
