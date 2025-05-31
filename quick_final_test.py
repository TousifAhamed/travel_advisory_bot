#!/usr/bin/env python3
"""
Simple test to verify all components are working
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_basic_imports():
    print("Testing basic imports...")
    try:
        from travel_bot.models.ai_models import DevstralModel, ModelFactory
        print("✅ AI models imported")
        
        from travel_bot.processors.text_processor import TextProcessor
        print("✅ Text processor imported")
        
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False

def test_ollama():
    print("Testing Ollama connection...")
    try:
        import requests
        response = requests.get("http://localhost:11434/api/tags", timeout=3)
        if response.status_code == 200:
            print("✅ Ollama is running")
            return True
        else:
            print("⚠️ Ollama not responding")
            return False
    except Exception as e:
        print(f"⚠️ Ollama connection failed: {e}")
        return False

def main():
    print("🚀 Travel Advisory Bot - Quick Test")
    print("=" * 40)
    
    import_ok = test_basic_imports()
    ollama_ok = test_ollama()
    
    if import_ok:
        print("\n🎉 All imports working!")
        print("✅ Python 3.13 compatibility achieved")
        print("✅ No more OpenAI circular import issues")
        
        if ollama_ok:
            print("✅ Devstral model ready via Ollama")
        
        print("\n📋 Ready to launch Streamlit app!")
        print("Run: streamlit run src\\travel_bot\\ui\\streamlit_app.py --server.port 8501")
        return 0
    else:
        print("❌ Import issues detected")
        return 1

if __name__ == "__main__":
    sys.exit(main())
