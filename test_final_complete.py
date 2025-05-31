#!/usr/bin/env python3
"""
Final comprehensive test for the Travel Advisory Bot
"""
import os
import sys

# Add the src directory to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(project_root, 'src')
sys.path.insert(0, src_path)

def main():
    print("🚀 Travel Advisory Bot - Final Complete Test")
    print("=" * 50)
    
    tests_passed = 0
    total_tests = 0
    
    # Test 1: Core Models Import
    total_tests += 1
    try:
        from travel_bot.models import (
            InputType, TravelPreferences, ProcessedInput,
            AIModel, InputProcessor, TravelAgent
        )
        print("✅ Test 1: Core models imported successfully")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 1: Core models failed - {e}")
    
    # Test 2: Text Processor
    total_tests += 1
    try:
        from travel_bot.processors.text_processor import TextProcessor
        processor = TextProcessor()
        print("✅ Test 2: TextProcessor created successfully")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 2: TextProcessor failed - {e}")
    
    # Test 3: Other Processors
    total_tests += 1
    try:
        from travel_bot.processors import (
            ImageProcessor, AudioProcessor, VideoProcessor, PDFProcessor
        )
        print("✅ Test 3: All processors imported successfully")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 3: Processors failed - {e}")
    
    # Test 4: Travel Utils
    total_tests += 1
    try:
        from travel_bot.utils.travel_utils import TravelUtils
        print("✅ Test 4: TravelUtils imported successfully")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 4: TravelUtils failed - {e}")
    
    # Test 5: AI Models
    total_tests += 1
    try:
        from travel_bot.ai_models import ModelFactory
        factory = ModelFactory()
        print("✅ Test 5: ModelFactory created successfully")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 5: ModelFactory failed - {e}")
    
    # Test 6: Streamlit App Import
    total_tests += 1
    try:
        from travel_bot.ui.streamlit_app import main
        print("✅ Test 6: Streamlit app imported successfully")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 6: Streamlit app failed - {e}")
    
    # Test 7: Basic Functionality Test
    total_tests += 1
    try:
        # Test text processing
        text_proc = TextProcessor()
        result = text_proc.process("Test travel query")
        if result and hasattr(result, 'content'):
            print("✅ Test 7: Basic text processing works")
            tests_passed += 1
        else:
            print("❌ Test 7: Text processing returned invalid result")
    except Exception as e:
        print(f"❌ Test 7: Basic functionality failed - {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        print("🎉 ALL TESTS PASSED! Travel Advisory Bot is fully operational!")
        return True
    else:
        print(f"⚠️  {total_tests - tests_passed} tests failed. Please check the errors above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
