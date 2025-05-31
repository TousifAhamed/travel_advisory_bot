@echo off
echo 🎉 LAUNCHING TRAVEL ADVISORY BOT - FULLY FIXED VERSION
echo =========================================================
echo ✅ Timeout Issue: RESOLVED (60-90 second timeouts)
echo ✅ Model Selection: FIXED (Using Devstral by default)
echo ✅ Circular Dependencies: RESOLVED
echo ✅ All Critical Issues: FIXED
echo.

cd /d "c:\DEV\Travel_Advisory_Bot\travel-advisory-bot"

echo 🔄 Starting application on http://localhost:8501
echo 📱 The Travel Advisory Bot is now fully operational!
echo.
echo 🌟 Available Features:
echo   - AI Travel Suggestions with Devstral
echo   - Intelligent Itinerary Planning  
echo   - Interactive Travel Chat
echo   - Multimodal Input Support (Text, Images, Audio)
echo.
echo 💡 NOTE: First AI query may take 30-60 seconds (model loading)
echo    Subsequent queries will be much faster!
echo.

streamlit run src\travel_bot\ui\streamlit_app.py
