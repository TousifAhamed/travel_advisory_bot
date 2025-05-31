#!/usr/bin/env python3
"""Validate that the indentation fix worked"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """Test all critical imports"""
    try:
        print("🔄 Testing imports after indentation fix...")
        
        # Test travel agent import
        from travel_bot.agents.travel_agent import SmartTravelAgent
        print("✅ SmartTravelAgent imported successfully")
        
        # Test travel bot import
        from travel_bot.travel_bot import TravelBot
        print("✅ TravelBot imported successfully")
        
        # Test Streamlit app components
        from travel_bot.ui.streamlit_app import StreamlitTravelApp
        print("✅ StreamlitTravelApp imported successfully")
        
        # Test model factory
        from travel_bot.models.ai_models import ModelFactory
        print("✅ ModelFactory imported successfully")
        
        # Test creating a TravelBot instance
        bot = TravelBot()
        print("✅ TravelBot instance created successfully")
        
        print("\n🎉 ALL IMPORTS SUCCESSFUL!")
        print("✅ Indentation error FIXED")
        print("✅ Application ready to launch")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🛠️  INDENTATION FIX VALIDATION")
    print("=" * 40)
    
    success = test_imports()
    
    if success:
        print("\n🚀 READY TO LAUNCH!")
        print("Run: streamlit run src\\travel_bot\\ui\\streamlit_app.py")
    else:
        print("\n❌ Still has issues - needs more debugging")
