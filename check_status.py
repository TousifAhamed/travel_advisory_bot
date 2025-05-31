#!/usr/bin/env python3
"""
Quick dependency check and app restart
"""

import sys
import os
from pathlib import Path

# Setup paths
project_root = Path(__file__).parent.absolute()
src_dir = project_root / "src"
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(src_dir))

def check_dependencies():
    """Check which dependencies are available"""
    deps = {}
    
    # Core dependencies
    try:
        import streamlit
        deps['streamlit'] = f"✅ {streamlit.__version__}"
    except ImportError:
        deps['streamlit'] = "❌ Missing"
    
    try:
        import ollama
        deps['ollama'] = "✅ Available"
    except ImportError:
        deps['ollama'] = "❌ Missing"
    
    # Multimodal processing
    try:
        import whisper
        deps['whisper'] = "✅ Available"
    except ImportError:
        deps['whisper'] = "⚠️ Missing (audio processing limited)"
    
    try:
        from transformers import BlipProcessor
        deps['transformers'] = "✅ Available"
    except ImportError:
        deps['transformers'] = "⚠️ Missing (image processing limited)"
    
    try:
        from langdetect import detect
        deps['langdetect'] = "✅ Available"
    except ImportError:
        deps['langdetect'] = "⚠️ Missing (language detection limited)"
    
    try:
        from googletrans import Translator
        deps['googletrans'] = "✅ Available"
    except ImportError:
        deps['googletrans'] = "⚠️ Missing (translation limited)"
    
    return deps

def test_imports():
    """Test travel bot imports"""
    try:
        from travel_bot.travel_bot import TravelBot
        return "✅ TravelBot imports successful"
    except Exception as e:
        return f"❌ TravelBot import failed: {e}"

def main():
    print("🔧 Travel Advisory Bot - Dependency Status")
    print("=" * 50)
    
    # Check dependencies
    deps = check_dependencies()
    for name, status in deps.items():
        print(f"{name:15}: {status}")
    
    print("\n🧪 Testing Core Imports")
    print("-" * 30)
    import_status = test_imports()
    print(import_status)
    
    # Count available vs missing
    available = sum(1 for status in deps.values() if status.startswith("✅"))
    total = len(deps)
    
    print(f"\n📊 Summary: {available}/{total} dependencies available")
    
    if "✅" in import_status:
        print("\n🎉 Core application is ready!")
        print("💡 Some optional features may be limited due to missing dependencies.")
        print("🚀 You can now run the application with: launch.bat")
    else:
        print("\n⚠️ Core imports still have issues.")
        print("💡 Try installing missing dependencies:")
        print("   pip install openai-whisper langdetect googletrans==4.0.0rc1")
    
    print("\n🌐 If the Streamlit app is running, refresh the browser page.")

if __name__ == "__main__":
    main()
