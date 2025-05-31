#!/usr/bin/env python3
"""
Quick test to verify AI models work correctly after fixing abstract method
"""
import sys
import os

# Add src to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_ai_models():
    print("🔍 Testing AI models after abstract method fix...")
    
    try:
        from travel_bot.models.ai_models import DevstralModel, HuggingFaceLocalModel, OllamaGenericModel, ModelFactory
        
        # Test DevstralModel
        print("Testing DevstralModel...")
        devstral = DevstralModel()
        print(f"✅ DevstralModel created, available: {devstral.is_available()}")
        
        # Test HuggingFaceLocalModel
        print("Testing HuggingFaceLocalModel...")
        hf_model = HuggingFaceLocalModel()
        print(f"✅ HuggingFaceLocalModel created, available: {hf_model.is_available()}")
        
        # Test OllamaGenericModel
        print("Testing OllamaGenericModel...")
        ollama_model = OllamaGenericModel()
        print(f"✅ OllamaGenericModel created, available: {ollama_model.is_available()}")
        
        # Test ModelFactory
        print("Testing ModelFactory...")
        factory = ModelFactory()
        best_model = factory.get_best_available_model()
        print(f"✅ Best available model: {type(best_model).__name__}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing AI models: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_travel_bot():
    print("\n🚀 Testing TravelBot creation...")
    
    try:
        from travel_bot.travel_bot import TravelBot
        
        # Test TravelBot initialization
        bot = TravelBot(model_type="devstral")
        print("✅ TravelBot created successfully!")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating TravelBot: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    print("🎯 Abstract Method Fix Validation")
    print("=" * 40)
    
    ai_test = test_ai_models()
    bot_test = test_travel_bot()
    
    if ai_test and bot_test:
        print("\n🎉 ALL TESTS PASSED!")
        print("✅ Abstract method implementations working")
        print("✅ TravelBot can be created")
        print("🚀 Ready to launch Streamlit app!")
        return 0
    else:
        print("\n❌ Some tests failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())
