#!/usr/bin/env python3
"""
Simple test script to verify the Travel Advisory Bot setup
"""

import sys
import os
import asyncio

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """Test if all imports work correctly"""
    print("Testing imports...")
    
    try:
        from src.travel_bot.models import InputType, TravelPreferences
        print("✅ Models imported successfully")
    except Exception as e:
        print(f"❌ Models import failed: {e}")
        return False
    
    try:
        from src.travel_bot.processors.text_processor import TextProcessor
        print("✅ Text processor imported successfully")
    except Exception as e:
        print(f"❌ Text processor import failed: {e}")
        return False
    
    try:
        from src.travel_bot.models.ai_models import ModelFactory
        print("✅ AI models imported successfully")
    except Exception as e:
        print(f"❌ AI models import failed: {e}")
        return False
    
    try:
        from src.travel_bot.agents.travel_agent import SmartTravelAgent
        print("✅ Travel agent imported successfully")
    except Exception as e:
        print(f"❌ Travel agent import failed: {e}")
        return False
    
    try:
        from src.travel_bot.travel_bot import TravelBot
        print("✅ Travel bot imported successfully")
    except Exception as e:
        print(f"❌ Travel bot import failed: {e}")
        return False
    
    return True

def test_basic_functionality():
    """Test basic functionality without external dependencies"""
    print("\nTesting basic functionality...")
    
    try:
        from src.travel_bot.models import InputType, TravelPreferences
        from src.travel_bot.processors.text_processor import TextProcessor
        
        # Test text processor
        processor = TextProcessor()
        test_input = "I want to visit Paris for a romantic vacation"
        
        # Run async function
        result = asyncio.run(processor.process(test_input))
        
        print(f"✅ Text processing successful: {result.content[:50]}...")
        print(f"✅ Detected language: {result.language}")
        print(f"✅ Extracted entities: {result.extracted_entities}")
        
        return True
        
    except Exception as e:
        print(f"❌ Basic functionality test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_configuration():
    """Test configuration loading"""
    print("\nTesting configuration...")
    
    try:
        from config.settings import Config
        
        print(f"✅ Default model: {Config.DEFAULT_LLM_MODEL}")
        print(f"✅ Supported languages: {len(Config.SUPPORTED_LANGUAGES)}")
        print(f"✅ Max file size: {Config.MAX_FILE_SIZE_MB}MB")
        
        # Test config validation
        validation = Config.validate_config()
        print(f"✅ Configuration validation: {validation}")
        
        return True
        
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Running Travel Advisory Bot Tests")
    print("=" * 50)
    
    tests = [
        ("Import Test", test_imports),
        ("Configuration Test", test_configuration),
        ("Basic Functionality Test", test_basic_functionality)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n📋 {test_name}")
        print("-" * 30)
        
        if test_func():
            passed += 1
            print(f"✅ {test_name} PASSED")
        else:
            print(f"❌ {test_name} FAILED")
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The application is ready to use.")
        print("\n🚀 To start the application:")
        print("   • Web interface: python main.py")
        print("   • Console demo: python main.py --console")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")

if __name__ == "__main__":
    main()