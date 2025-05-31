@echo off
echo 🚀 Starting Travel Advisory Bot with Timeout Fixes
echo =====================================================
echo.

cd /d "c:\DEV\Travel_Advisory_Bot\travel-advisory-bot"

echo 📋 Current Directory: %CD%
echo.

echo 🔍 Checking Python and Streamlit...
python --version
streamlit --version
echo.

echo 🤖 Testing AI Model Availability...
python -c "import sys; sys.path.insert(0, 'src'); from travel_bot.models.ai_models import DevstralModel; model = DevstralModel(); print('DevStral Available:', model.is_available())" 2>nul || echo "Warning: Could not test DevStral availability"
echo.

echo 🌐 Starting Streamlit Travel Advisory Bot...
echo 📍 App will be available at: http://localhost:8501
echo 💡 Press Ctrl+C to stop the application
echo.

streamlit run src/travel_bot/ui/streamlit_app.py --server.port 8501 --server.headless true

pause
