#!/usr/bin/env python3
"""
Dependency Status Check - Final Validation
"""
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

print("🔍 Checking Travel Advisory Bot Dependencies...")
print("=" * 50)

# Core dependencies
try:
    import streamlit
    print("✅ Streamlit:", streamlit.__version__)
except ImportError as e:
    print("❌ Streamlit:", str(e))

try:
    import requests
    print("✅ Requests:", requests.__version__)
except ImportError as e:
    print("❌ Requests:", str(e))

# AI/ML dependencies
try:
    import torch
    print("✅ PyTorch:", torch.__version__)
except ImportError as e:
    print("❌ PyTorch:", str(e))

try:
    import transformers
    print("✅ Transformers:", transformers.__version__)
except ImportError as e:
    print("❌ Transformers:", str(e))

# Audio processing
try:
    import speech_recognition
    print("✅ SpeechRecognition:", speech_recognition.__version__)
except ImportError as e:
    print("❌ SpeechRecognition:", str(e))

try:
    import pydub
    print("✅ Pydub:", pydub.version)
except ImportError as e:
    print("❌ Pydub:", str(e))

try:
    import whisper
    print("✅ Whisper: Available")
except ImportError as e:
    print("⚠️  Whisper:", str(e))

# Image processing
try:
    from PIL import Image
    print("✅ Pillow (PIL):", Image.__version__)
except ImportError as e:
    print("❌ Pillow (PIL):", str(e))

try:
    import cv2
    print("✅ OpenCV:", cv2.__version__)
except ImportError as e:
    print("❌ OpenCV:", str(e))

# Text processing
try:
    import langdetect
    print("✅ Language Detection: Available")
except ImportError as e:
    print("❌ Language Detection:", str(e))

try:
    import googletrans
    print("✅ Google Translate:", googletrans.__version__)
except ImportError as e:
    print("❌ Google Translate:", str(e))

# PDF processing
try:
    import pypdf
    print("✅ pypdf:", pypdf.__version__)
except ImportError as e:
    print("❌ pypdf:", str(e))

print("\n" + "=" * 50)

# Test our modules
print("🧪 Testing Travel Bot Modules...")
try:
    from travel_bot.travel_bot import TravelBot
    print("✅ TravelBot class imported successfully")
    
    from travel_bot.models.ai_models import DevstralModel
    print("✅ DevstralModel imported successfully")
    
    from travel_bot.processors import ProcessorFactory
    print("✅ ProcessorFactory imported successfully")
    
    from travel_bot.agents.travel_agent import SmartTravelAgent
    print("✅ SmartTravelAgent imported successfully")
    
except ImportError as e:
    print(f"❌ Module import error: {e}")

print("\n🎉 Dependency check complete!")
print("🌐 Streamlit app should be running at: http://localhost:8501")
