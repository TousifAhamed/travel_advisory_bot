@echo off
echo 🚀 Starting Travel Advisory Bot with Timeout Fix
echo ================================================
cd /d "c:\DEV\Travel_Advisory_Bot\travel-advisory-bot"

echo ✓ Checking Python environment...
python -c "import sys; print('Python:', sys.version.split()[0])"

echo ✓ Checking Streamlit...
streamlit version

echo ✓ Starting application with increased AI timeouts...
echo   - DevstralModel: 60 seconds timeout
echo   - GenericOllamaModel: 45 seconds timeout

echo.
echo 🌐 Launching on http://localhost:8501
echo Press Ctrl+C to stop the application
echo.

streamlit run src\travel_bot\ui\streamlit_app.py
pause
