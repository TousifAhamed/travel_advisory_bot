@echo off
cls
echo.
echo ========================================
echo   🔍 DEVSTRAL STATUS CHECK
echo ========================================
echo.

echo [1/5] Python Environment Check...
python --version
if %errorlevel% neq 0 (
    echo ❌ Python not found
    goto :end
) else (
    echo ✅ Python is available
)
echo.

echo [2/5] Ollama Service Check...
curl -s -m 5 http://localhost:11434/api/tags
if %errorlevel% neq 0 (
    echo ❌ Ollama not responding at localhost:11434
    echo 💡 Make sure Ollama is running: ollama serve
) else (
    echo ✅ Ollama is running
)
echo.

echo [3/5] Available Models Check...
ollama list
echo.

echo [4/5] Devstral Model Check...
ollama show devstral
if %errorlevel% neq 0 (
    echo ⚠️ Devstral model not found
    echo 💡 Install it with: ollama pull devstral
) else (
    echo ✅ Devstral model is available
)
echo.

echo [5/5] Project Structure Check...
if exist "src\travel_bot\ui\streamlit_app.py" (
    echo ✅ Streamlit app found
) else (
    echo ❌ Streamlit app missing
)

if exist ".env" (
    echo ✅ Environment configuration found
) else (
    echo ❌ .env file missing
)
echo.

echo ========================================
echo Status check complete!
echo.
echo 🚀 To start the bot: start_devstral.bat
echo 🧪 To test integration: python test_devstral.py
echo.

:end
pause
