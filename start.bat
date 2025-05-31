@echo off
echo Starting Travel Advisory Bot...
echo.

REM Check if uv is available
uv --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: uv is not installed or not in PATH
    echo Please install uv first: https://docs.astral.sh/uv/
    pause
    exit /b 1
)

REM Install dependencies if needed
echo Installing dependencies...
uv sync

REM Run the application
echo.
echo Starting the application...
python main.py

pause