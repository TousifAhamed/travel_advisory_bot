@echo off
echo ========================================
echo Travel Advisory Bot - Setup and Launch
echo ========================================

echo.
echo [1/4] Checking Python installation...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python not found. Please install Python 3.10+ first.
    pause
    exit /b 1
)

echo.
echo [2/4] Installing dependencies...
pip install streamlit python-dotenv requests pillow pypdf2 openai transformers torch langdetect googletrans opencv-python
if %errorlevel% neq 0 (
    echo WARNING: Some dependencies failed to install. Continuing anyway...
)

echo.
echo [3/4] Checking environment configuration...
if not exist .env (
    echo Creating .env file from template...
    copy .env.example .env
    echo.
    echo IMPORTANT: Please edit .env file with your API keys before using the application!
    echo.
)

echo.
echo [4/4] Starting the application...
echo Opening browser to http://localhost:8501
echo Press Ctrl+C to stop the application
echo.

streamlit run src\travel_bot\ui\streamlit_app.py --server.port 8501 --server.headless false

pause
