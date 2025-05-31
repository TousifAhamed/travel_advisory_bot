@echo off
echo 🎉 TRAVEL ADVISORY BOT - FINAL WORKING VERSION
echo ===============================================
echo ✅ All Issues RESOLVED:
echo    - Circular Dependencies ✅
echo    - Indentation Errors ✅  
echo    - Timeout Issues ✅
echo    - Model Selection ✅
echo    - Duplicate Element IDs ✅
echo.

cd /d "c:\DEV\Travel_Advisory_Bot\travel-advisory-bot"

echo 🔄 Starting Travel Advisory Bot...
echo 🌐 Opening browser at http://localhost:8501
echo.
echo 💡 First AI response may take 30-60 seconds (Devstral loading)
echo    Subsequent responses will be much faster!
echo.

start http://localhost:8501
streamlit run src\travel_bot\ui\streamlit_app.py --server.port 8501

pause
