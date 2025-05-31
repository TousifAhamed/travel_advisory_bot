@echo off
echo ========================================
echo    🤖 Starting Travel Advisory Bot 🌍
echo ========================================
echo.

cd /d "%~dp0"
echo Current directory: %CD%

echo Installing dependencies...
pip install streamlit python-dotenv requests --quiet

echo.
echo Setting PYTHONPATH...
set PYTHONPATH=%CD%;%CD%\src;%PYTHONPATH%

echo.
echo Starting Streamlit application...
echo 🌐 Browser will open at: http://localhost:8501
echo 🤖 Using Devstral for AI processing
echo ⏹️ Press Ctrl+C to stop
echo.

python -m streamlit run src\travel_bot\ui\streamlit_app.py --server.port 8501

pause
