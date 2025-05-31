#!/usr/bin/env python3
"""
Final Comprehensive Test - Travel Advisory Bot with Timeout Fixes
Tests all components including AI connectivity with 120s timeout
"""

import sys
import os
import asyncio
import time

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """Test all critical imports"""
    print("🔍 Testing Imports...")
    try:
        from travel_bot.models.ai_models import DevstralModel, ModelFactory
        from travel_bot.models.data_models import InputType, ProcessedInput
        from travel_bot.travel_bot import TravelBot
        from travel_bot.agents.travel_agent import SmartTravelAgent
        print("✅ All imports successful")
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False

def test_model_availability():
    """Test AI model availability"""
    print("\n🤖 Testing AI Model Availability...")
    try:
        from travel_bot.models.ai_models import DevstralModel, ModelFactory
        
        # Test DevStral
        devstral = DevstralModel()
        available = devstral.is_available()
        print(f"   DevStral Available: {available}")
        
        # Test ModelFactory
        models = ModelFactory.get_available_models()
        print(f"   Available Models: {len(models)}")
        for model in models:
            status = "✅" if model['available'] else "❌"
            print(f"      {status} {model['name']}")
        
        return len([m for m in models if m['available']]) > 0
    except Exception as e:
        print(f"❌ Model availability error: {e}")
        return False

async def test_ai_response():
    """Test AI response generation with timeout fixes"""
    print("\n🧠 Testing AI Response Generation...")
    try:
        from travel_bot.models.ai_models import DevstralModel
        
        model = DevstralModel()
        if not model.is_available():
            print("❌ DevStral not available - skipping AI response test")
            return False
        
        print("   Generating AI response (with 120s timeout)...")
        start_time = time.time()
        
        prompt = "Suggest a weekend getaway near San Francisco for families with young children."
        response = await model.generate_response(prompt)
        
        elapsed = time.time() - start_time
        print(f"   ✅ Response generated in {elapsed:.1f} seconds")
        print(f"   📝 Response length: {len(response)} characters")
        print(f"   🎯 Response preview: {response[:150]}...")
        
        return len(response) > 50  # Basic validation
    except Exception as e:
        print(f"❌ AI response error: {e}")
        return False

def test_travel_bot():
    """Test TravelBot initialization"""
    print("\n🎒 Testing TravelBot...")
    try:
        from travel_bot.travel_bot import TravelBot
        
        bot = TravelBot(model_type="devstral")
        print("✅ TravelBot initialized successfully")
        return True
    except Exception as e:
        print(f"❌ TravelBot error: {e}")
        return False

def test_streamlit_imports():
    """Test Streamlit app imports"""
    print("\n🌐 Testing Streamlit App Imports...")
    try:
        from travel_bot.ui.streamlit_app import StreamlitTravelApp
        print("✅ Streamlit app imports successful")
        return True
    except Exception as e:
        print(f"❌ Streamlit app import error: {e}")
        return False

async def main():
    """Run all tests"""
    print("🚀 Travel Advisory Bot - Final Comprehensive Test")
    print("=" * 60)
    
    tests = [
        ("Imports", test_imports),
        ("Model Availability", test_model_availability),
        ("AI Response", test_ai_response),
        ("TravelBot", test_travel_bot),
        ("Streamlit Imports", test_streamlit_imports)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            if asyncio.iscoroutinefunction(test_func):
                result = await test_func()
            else:
                result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} test failed: {e}")
            results.append((test_name, False))
    
    print("\n" + "=" * 60)
    print("📊 Test Results Summary:")
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"   {status} {test_name}")
        if result:
            passed += 1
    
    print(f"\n🎯 Overall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED! Travel Advisory Bot is ready to use!")
        print("\n📋 To start the application:")
        print("   streamlit run src/travel_bot/ui/streamlit_app.py --server.port 8501")
    else:
        print("⚠️  Some tests failed. Check the errors above.")
    
    return passed == total

if __name__ == "__main__":
    asyncio.run(main())
