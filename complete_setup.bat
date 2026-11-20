@echo off
echo Travel Advisory Bot - Complete Setup and Launch
echo ================================================

cd /d "c:\DEV\Travel_Advisory_Bot\travel-advisory-bot"

echo Step 1: Activating virtual environment...
call .venv\Scripts\activate.bat

echo Step 2: Installing/upgrading dependencies...
pip install -e .

if %ERRORLEVEL% NEQ 0 (
    echo ❌ Failed to install dependencies
    echo Trying alternative installation...
    pip install streamlit openai transformers torch torchvision Pillow pypdf python-multipart langdetect googletrans opencv-python requests beautifulsoup4 folium plotly python-dotenv aiofiles httpx pydantic numpy pandas
)

echo Step 3: Installing Ollama for Devstral...
python -c "import ollama; print('✅ Ollama available')" 2>nul || pip install ollama

echo Step 4: Testing core imports...
python -c "import sys; sys.path.insert(0, 'src'); sys.path.insert(0, '.'); from travel_bot.travel_bot import TravelBot; print('✅ TravelBot imported successfully')"

if %ERRORLEVEL% NEQ 0 (
    echo ❌ Core import test failed - checking individual components...
    python -c "import sys; sys.path.insert(0, 'src'); import travel_bot; print('✅ travel_bot package loaded')"
    python -c "import sys; sys.path.insert(0, 'src'); from travel_bot.models import InputType; print('✅ InputType loaded')"
    pause
)

echo Step 5: Checking Streamlit...
python -c "import streamlit; print('✅ Streamlit available')" || (
    echo ❌ Streamlit not available
    pause
    exit /b 1
)

echo Step 6: Checking Devstral status...
python -c "import ollama; client = ollama.Client(); models = client.list(); print('📋 Available models:', [m['name'] for m in models['models']]); print('✅ Devstral ready' if any('devstral' in m['name'] for m in models['models']) else '⚠️  Devstral not found')" 2>nul || echo "⚠️  Ollama not running - start it separately"

echo.
echo ✅ Setup complete! 
echo.
echo Starting Streamlit app...
echo App will be available at: http://localhost:8501
echo.
python streamlit_launcher.py

pause
