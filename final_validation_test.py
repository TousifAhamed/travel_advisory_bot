#!/usr/bin/env python3
"""
Final validation script for Travel Advisory Bot
Tests all components with Python 3.13 compatibility
"""
import sys
import os
import traceback

# Add src to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """Test all critical imports"""
    print("🔍 Testing imports...")
    
    try:
        # Test AI models import
        from travel_bot.models.ai_models import ModelFactory, DevstralModel
        print("✅ AI Models imported successfully")
        
        # Test processors
        from travel_bot.processors.text_processor import TextProcessor
        from travel_bot.processors.image_processor import ImageProcessor
        from travel_bot.processors.audio_processor import AudioProcessor
        from travel_bot.processors.pdf_processor import PDFProcessor
        print("✅ All processors imported successfully")
        
        # Test main app
        from travel_bot.travel_bot import TravelBot
        print("✅ Main TravelBot imported successfully")
        
        # Test Streamlit app
        from travel_bot.ui.streamlit_app import main
        print("✅ Streamlit app imported successfully")
        
        return True
        
    except Exception as e:
        print(f"❌ Import error: {e}")
        traceback.print_exc()
        return False

def test_ai_models():
    """Test AI model availability"""
    print("\n🤖 Testing AI models...")
    
    try:
        from travel_bot.models.ai_models import ModelFactory
        
        # Test DevStral availability
        model_factory = ModelFactory()
        best_model = model_factory.get_best_available_model()
        print(f"✅ Best available model: {type(best_model).__name__}")
        
        return True
        
    except Exception as e:
        print(f"❌ AI model error: {e}")
        traceback.print_exc()
        return False

def test_ollama_connection():
    """Test Ollama connection"""
    print("\n🦙 Testing Ollama connection...")
    
    try:
        import requests
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json().get('models', [])
            print(f"✅ Ollama connected, {len(models)} models available")
            for model in models:
                print(f"   - {model.get('name', 'Unknown')}")
            return True
        else:
            print(f"⚠️  Ollama responded with status {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Ollama connection error: {e}")
        return False

def main():
    """Run all validation tests"""
    print("🚀 Travel Advisory Bot - Final Validation")
    print("=" * 50)
    
    results = []
    results.append(test_imports())
    results.append(test_ai_models())
    results.append(test_ollama_connection())
    
    print("\n" + "=" * 50)
    if all(results):
        print("🎉 ALL TESTS PASSED!")
        print("\n📋 LAUNCH INSTRUCTIONS:")
        print("1. Open a new command prompt")
        print("2. Navigate to: cd c:\\DEV\\Travel_Advisory_Bot\\travel-advisory-bot")
        print("3. Set Python path: set PYTHONPATH=%cd%\\src")
        print("4. Run: streamlit run src\\travel_bot\\ui\\streamlit_app.py --server.port 8501")
        print("5. Open browser to: http://localhost:8501")
        print("\n🌟 Your Agentic AI Travel Planning Application is ready!")
        return 0
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
