#!/usr/bin/env python3
"""
Quick test to verify ModelFactory import fix
"""

import sys
import os

# Add src to path
project_root = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(project_root, "src")
sys.path.insert(0, src_path)

def test_imports():
    """Test all critical imports including ModelFactory"""
    try:
        print("Testing ModelFactory import...")
        from travel_bot.models.ai_models import ModelFactory
        print("✅ ModelFactory imported successfully")
        
        print("Testing ModelFactory methods...")
        model = ModelFactory.get_best_available_model()
        print(f"✅ Best model: {model.__class__.__name__}")
        
        models_status = ModelFactory.list_available_models()
        print(f"✅ Available models: {models_status}")
        
        print("Testing other imports...")
        from travel_bot.models.ai_models import DevstralModel, AIModelManager
        from travel_bot.travel_bot import TravelBot
        print("✅ All imports successful")
        
        return True
        
    except Exception as e:
        print(f"❌ Import test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🧪 TESTING MODELFACTORY FIX")
    success = test_imports()
    if success:
        print("\n🎉 All tests passed! ModelFactory issue is resolved.")
    else:
        print("\n❌ Tests failed. Please check the errors above.")
