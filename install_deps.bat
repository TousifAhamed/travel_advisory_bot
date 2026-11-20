@echo off
echo 📦 Installing Travel Advisory Bot Dependencies
echo ============================================

cd /d "%~dp0"

echo.
echo 🔧 Core dependencies...
pip install streamlit python-dotenv requests ollama --quiet --upgrade

echo.
echo 🧠 AI/ML dependencies...
pip install openai transformers torch torchvision --quiet --upgrade --index-url https://download.pytorch.org/whl/cpu

echo.
echo 🎥 Multimodal processing...
pip install openai-whisper opencv-python Pillow pypdf --quiet --upgrade

echo.
echo 🌐 Language processing...
pip install langdetect googletrans==4.0.0rc1 --quiet --upgrade

echo.
echo 📊 Data processing...
pip install numpy pandas aiofiles httpx pydantic --quiet --upgrade

echo.
echo 📋 Additional utilities...
pip install beautifulsoup4 folium plotly python-multipart --quiet --upgrade

echo.
echo ✅ All dependencies installed!
echo.
echo 🧪 Testing imports...
python -c "
import sys
sys.path.insert(0, 'src')
sys.path.insert(0, '.')

try:
    from travel_bot.travel_bot import TravelBot
    print('✅ TravelBot: OK')
except ImportError as e:
    print(f'❌ TravelBot: {e}')

try:
    import streamlit
    print(f'✅ Streamlit: {streamlit.__version__}')
except ImportError:
    print('❌ Streamlit: Failed')

try:
    import ollama
    print('✅ Ollama: OK')
except ImportError:
    print('❌ Ollama: Failed')

try:
    import whisper
    print('✅ Whisper: OK')
except ImportError:
    print('⚠️  Whisper: Not available (audio processing limited)')

try:
    from transformers import BlipProcessor
    print('✅ Transformers: OK')
except ImportError:
    print('⚠️  Transformers: Not available (image processing limited)')
"

echo.
echo 🚀 Ready to launch! Run: launch.bat
pause
