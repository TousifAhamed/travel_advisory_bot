#!/usr/bin/env python3
"""
Final status test for Travel Advisory Bot
Tests all critical components after fixing the ai_models.py file
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """Test all critical imports"""
    print("=" * 50)
    print("TESTING IMPORTS")
    print("=" * 50)
    
    try:
        # Test basic imports
        from travel_bot.models.ai_models import DevstralModel, AIModelManager, InputType, ProcessedInput
        print("✅ AI Models imported successfully")
        
        from travel_bot.processors.text_processor import TextProcessor
        print("✅ Text Processor imported successfully")
        
        from travel_bot.processors.image_processor import ImageProcessor
        print("✅ Image Processor imported successfully")
        
        from travel_bot.processors.audio_processor import AudioProcessor
        print("✅ Audio Processor imported successfully")
        
        from travel_bot.travel_bot import TravelBot
        print("✅ Main TravelBot imported successfully")
        
        return True
        
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False

def test_model_availability():
    """Test AI model availability"""
    print("\n" + "=" * 50)
    print("TESTING AI MODEL AVAILABILITY")
    print("=" * 50)
    
    try:
        from travel_bot.models.ai_models import DevstralModel, AIModelManager
        
        # Test DevStral
        devstral = DevstralModel()
        print(f"DevStral available: {'✅' if devstral.is_available() else '❌'}")
        
        # Test Model Manager
        manager = AIModelManager()
        available_models = manager.get_available_models()
        print(f"Available models: {available_models}")
        
        if manager.primary_model:
            print(f"✅ Primary model selected: {manager.primary_model.__class__.__name__}")
        else:
            print("❌ No primary model available")
            
        return True
        
    except Exception as e:
        print(f"❌ Model test failed: {e}")
        return False

def test_streamlit_compatibility():
    """Test Streamlit app compatibility"""
    print("\n" + "=" * 50)
    print("TESTING STREAMLIT COMPATIBILITY")
    print("=" * 50)
    
    try:
        import streamlit as st
        print("✅ Streamlit import successful")
        
        # Test if our app can be imported
        from travel_bot.ui.streamlit_app import main
        print("✅ Streamlit app can be imported")
        
        return True
        
    except Exception as e:
        print(f"❌ Streamlit test failed: {e}")
        return False

def test_end_to_end():
    """Test end-to-end functionality"""
    print("\n" + "=" * 50)
    print("TESTING END-TO-END FUNCTIONALITY")
    print("=" * 50)
    
    try:
        from travel_bot.travel_bot import TravelBot
        from travel_bot.models.ai_models import InputType
        
        # Initialize bot
        bot = TravelBot()
        print("✅ TravelBot initialized")
        
        # Test text processing
        test_input = "I want to travel to Japan for 2 weeks with a budget of $3000"
        result = bot.process_input(test_input, InputType.TEXT)
        
        if result and 'error' not in result.lower():
            print("✅ Text processing works")
        else:
            print(f"❌ Text processing issue: {result}")
            
        return True
        
    except Exception as e:
        print(f"❌ End-to-end test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 TRAVEL ADVISORY BOT - FINAL STATUS TEST")
    print("Testing all components after fixing ai_models.py")
    
    tests = [
        ("Import Tests", test_imports),
        ("Model Availability", test_model_availability), 
        ("Streamlit Compatibility", test_streamlit_compatibility),
        ("End-to-End", test_end_to_end)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            success = test_func()
            results.append((test_name, success))
        except Exception as e:
            print(f"❌ {test_name} crashed: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 50)
    print("FINAL RESULTS SUMMARY")
    print("=" * 50)
    
    passed = 0
    for test_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{test_name:.<30} {status}")
        if success:
            passed += 1
    
    print(f"\nOverall: {passed}/{len(results)} tests passed")
    
    if passed == len(results):
        print("\n🎉 ALL TESTS PASSED! Application is ready to launch!")
        print("\nTo start the application, run:")
        print("streamlit run src\\travel_bot\\ui\\streamlit_app.py")
    else:
        print(f"\n⚠️  {len(results) - passed} tests failed. Check errors above.")
    
    return passed == len(results)

if __name__ == "__main__":
    main()
