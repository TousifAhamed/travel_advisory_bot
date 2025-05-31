#!/usr/bin/env python3
"""
Final test to validate all fixes are working correctly.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """Test that all imports work correctly."""
    print("Testing imports...")
    
    try:
        from travel_bot.models.ai_models import ModelFactory, AIModel, DevstralModel
        print("✅ ModelFactory import successful")
        
        from travel_bot.ui.streamlit_app import TravelAdvisoryUI
        print("✅ Streamlit UI import successful")
        
        from travel_bot.travel_bot import TravelBot
        print("✅ TravelBot import successful")
        
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False

def test_modelfactory():
    """Test ModelFactory functionality."""
    print("\nTesting ModelFactory...")
    
    try:
        from travel_bot.models.ai_models import ModelFactory
        
        # Test static methods exist
        assert hasattr(ModelFactory, 'get_best_available_model')
        assert hasattr(ModelFactory, 'create_model')
        assert hasattr(ModelFactory, 'list_available_models')
        print("✅ ModelFactory methods exist")
        
        # Test method calls
        available_models = ModelFactory.list_available_models()
        print(f"✅ Available models: {available_models}")
        
        model = ModelFactory.get_best_available_model()
        print(f"✅ Best model: {type(model).__name__}")
        
        return True
    except Exception as e:
        print(f"❌ ModelFactory error: {e}")
        return False

def test_streamlit_ui():
    """Test Streamlit UI class can be instantiated."""
    print("\nTesting Streamlit UI...")
    
    try:
        from travel_bot.ui.streamlit_app import TravelAdvisoryUI
        
        ui = TravelAdvisoryUI()
        print("✅ TravelAdvisoryUI instantiated successfully")
        
        # Check that render_travel_preferences accepts context parameter
        import inspect
        sig = inspect.signature(ui.render_travel_preferences)
        params = list(sig.parameters.keys())
        assert 'context' in params, "context parameter missing from render_travel_preferences"
        print("✅ render_travel_preferences accepts context parameter")
        
        return True
    except Exception as e:
        print(f"❌ Streamlit UI error: {e}")
        return False

def main():
    """Run all tests."""
    print("🚀 Running final validation tests...\n")
    
    all_passed = True
    
    # Test imports
    if not test_imports():
        all_passed = False
    
    # Test ModelFactory
    if not test_modelfactory():
        all_passed = False
    
    # Test Streamlit UI
    if not test_streamlit_ui():
        all_passed = False
    
    print("\n" + "="*50)
    if all_passed:
        print("🎉 ALL TESTS PASSED! The application is ready to run.")
        print("\nTo launch the application, run:")
        print("python launch_final.py")
    else:
        print("❌ Some tests failed. Please check the errors above.")
    print("="*50)

if __name__ == "__main__":
    main()
