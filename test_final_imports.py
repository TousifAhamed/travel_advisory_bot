#!/usr/bin/env python3
"""
Final import test to verify circular dependency resolution
"""

def test_imports():
    try:
        # Test basic model imports
        from src.travel_bot.models import InputType, TravelPreferences, ProcessedInput
        print("✅ Data models imported successfully")
        
        # Test abstract base class imports
        from src.travel_bot.models import AIModel, InputProcessor, TravelAgent
        print("✅ Abstract base classes imported successfully")
          # Test ModelFactory import (the main blocker)
        from src.travel_bot.models.ai_models import ModelFactory
        print("✅ ModelFactory imported successfully")
        
        # Test processor imports
        from src.travel_bot.processors import TextProcessor, PDFProcessor
        print("✅ Processors imported successfully")
        
        # Test enum values
        print(f"✅ Available InputTypes: {[t.value for t in InputType]}")
        
        # Test creating instances
        prefs = TravelPreferences()
        print(f"✅ TravelPreferences instance created: {prefs}")
        
        print("\n🎉 ALL IMPORTS SUCCESSFUL! Circular dependency issue RESOLVED!")
        return True
        
    except Exception as e:
        print(f"❌ Import failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_imports()
