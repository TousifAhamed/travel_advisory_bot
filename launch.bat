@echo off
setlocal EnableDelayedExpansion

echo.
echo ========================================
echo    🤖 Travel Advisory Bot Launcher 🌍  
echo ========================================
echo.

REM Change to script directory
cd /d "%~dp0"
echo 📍 Project Directory: %CD%
echo.

REM Check if Python is available
python --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo ❌ Python not found in PATH
    echo Please install Python or add it to your PATH
    pause
    exit /b 1
)

echo ✅ Python found: 
python --version

REM Install core dependencies
echo.
echo 📦 Installing/updating dependencies...
pip install streamlit python-dotenv requests ollama --quiet --upgrade

REM Set Python path for imports
echo.
echo 🔧 Setting up Python paths...
set PYTHONPATH=%CD%;%CD%\src;%PYTHONPATH%
echo PYTHONPATH configured

REM Test imports
echo.
echo 🧪 Testing imports...
python -c "import sys; sys.path.insert(0, 'src'); sys.path.insert(0, '.'); from travel_bot.travel_bot import TravelBot; print('✅ Core imports successful')" 2>nul
if %ERRORLEVEL% equ 0 (
    set APP_FILE=src\travel_bot\ui\streamlit_app.py
    echo ✅ Full application ready
) else (
    set APP_FILE=minimal_app.py
    echo ⚠️  Using minimal app due to import issues
)

REM Check if Streamlit is available
echo.
echo 🌐 Checking Streamlit...
python -c "import streamlit; print('✅ Streamlit version:', streamlit.__version__)" 2>nul
if %ERRORLEVEL% neq 0 (
    echo ❌ Streamlit not available
    echo Installing Streamlit...
    pip install streamlit
)

REM Check Devstral status
echo.
echo 🤖 Checking Devstral status...
python -c "import ollama; client = ollama.Client(); models = client.list(); devstral_available = any('devstral' in m['name'] for m in models['models']); print('✅ Devstral ready' if devstral_available else '⚠️  Devstral not found - install with: ollama pull devstral')" 2>nul || echo "⚠️  Ollama not running - start with: ollama serve"

REM Launch application
echo.
echo 🚀 Starting Travel Advisory Bot...
echo ┌─────────────────────────────────────┐
echo │  🌐 URL: http://localhost:8501     │
echo │  🤖 AI: Devstral (Local)           │
echo │  ⏹️  Stop: Ctrl+C                   │
echo └─────────────────────────────────────┘
echo.

REM Start Streamlit
python -m streamlit run !APP_FILE! --server.port 8501 --server.address localhost

echo.
echo 📊 Application stopped
pause
