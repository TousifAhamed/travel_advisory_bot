@echo off
echo 🔄 Travel Advisory Bot - Status Check and Restart
echo ================================================

cd /d "%~dp0"

echo.
echo 📊 Checking current status...
python check_status.py

echo.
echo 🔧 Installing missing dependencies...
pip install openai-whisper langdetect "googletrans==4.0.0rc1" transformers torch PyPDF2 Pillow opencv-python --quiet --upgrade

echo.
echo 🧹 Clearing Python cache...
if exist "src\travel_bot\__pycache__" rmdir /s /q "src\travel_bot\__pycache__"
if exist "src\travel_bot\processors\__pycache__" rmdir /s /q "src\travel_bot\processors\__pycache__"
if exist "src\travel_bot\models\__pycache__" rmdir /s /q "src\travel_bot\models\__pycache__"

echo.
echo 🚀 Restarting application...
echo 🌐 Opening browser at: http://localhost:8501
echo.

timeout /t 2 >nul

REM Kill any existing Streamlit processes
taskkill /f /im python.exe /fi "WINDOWTITLE eq *streamlit*" >nul 2>&1

REM Set Python path and start Streamlit
set PYTHONPATH=%CD%;%CD%\src;%PYTHONPATH%
python -m streamlit run src\travel_bot\ui\streamlit_app.py --server.port 8501 --server.address localhost

pause
