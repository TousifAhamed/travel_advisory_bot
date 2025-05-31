@echo off
cls
echo.
echo ========================================
echo    🤖 DEVSTRAL TRAVEL ADVISORY BOT 🌍
echo ========================================
echo.
echo This will start your Travel Advisory Bot
echo using your local Devstral model via Ollama
echo.
echo 🔍 Checking prerequisites...
echo.

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python not found. Please install Python first.
    pause
    exit /b 1
)
echo ✅ Python is available

REM Check if Ollama is running
echo 🔗 Testing Ollama connection...
curl -s http://localhost:11434/api/tags >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️ Ollama might not be running
    echo 💡 Try running: ollama serve
    echo.
    echo Continuing anyway (app will use fallback mode)...
) else (
    echo ✅ Ollama is running
)

echo.
echo 📦 Installing required packages...
pip install streamlit python-dotenv requests --quiet

echo.
echo 🚀 Starting Travel Advisory Bot...
echo 🌐 Your browser should open to: http://localhost:8501
echo 🤖 Using Devstral model for AI processing
echo ⏹️ Press Ctrl+C to stop the application
echo.
echo ========================================
echo.

REM Start the Streamlit application
streamlit run src\travel_bot\ui\streamlit_app.py --server.port 8501

echo.
echo 👋 Travel Advisory Bot stopped
pause
