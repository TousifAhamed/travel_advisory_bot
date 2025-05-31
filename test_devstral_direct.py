#!/usr/bin/env python3
"""Quick test to verify Devstral is working"""

import sys
import os
import asyncio

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

async def test_devstral():
    """Test Devstral directly"""
    try:
        from travel_bot.models.ai_models import DevstralModel
        
        print("🔄 Testing Devstral model directly...")
        model = DevstralModel()
        
        if model.is_available():
            print("✅ Devstral is available!")
            
            response = await model.generate_response(
                "What are the top 3 travel destinations in Europe for summer 2025?"
            )
            
            print(f"🎉 AI Response: {response[:150]}...")
            print("\n✅ SUCCESS! Devstral is working perfectly!")
            return True
        else:
            print("❌ Devstral not available")
            return False
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

if __name__ == "__main__":
    print("🚀 Testing Devstral Direct Communication")
    print("=" * 50)
    
    success = asyncio.run(test_devstral())
    
    if success:
        print("\n🎉 PERFECT! Your Travel Advisory Bot is ready!")
        print("Launch with: streamlit run src\\travel_bot\\ui\\streamlit_app.py")
    else:
        print("\n❌ Please check Ollama and Devstral setup")
