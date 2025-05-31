@echo off
echo 🚀 Travel Advisory Bot - Smart Launcher
echo ======================================

cd /d "c:\DEV\Travel_Advisory_Bot\travel-advisory-bot"

echo Checking environment...
if not exist ".venv\Scripts\python.exe" (
    echo ❌ Virtual environment not found
    echo Please run: python -m venv .venv
    pause
    exit /b 1
)

echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo Checking if dependencies are installed...
python -c "import streamlit" 2>nul || (
    echo Installing core dependencies...
    pip install streamlit python-dotenv ollama
)

echo Testing imports...
python -c "import sys; sys.path.insert(0, 'src'); sys.path.insert(0, '.'); from travel_bot.travel_bot import TravelBot; print('✅ Full app ready')" 2>nul && (
    echo 🎉 Full application is ready!
    echo Starting main Streamlit app...
    python streamlit_launcher.py
) || (
    echo ⚠️  Some dependencies missing, starting minimal app...
    echo This will show the interface and help identify any remaining issues.
    echo.
    streamlit run minimal_app.py --server.port 8501
)

pause
