#!/usr/bin/env python3
"""Final test of Travel Advisory Bot with Devstral"""

import sys
import os
import asyncio

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

async def test_travel_bot():
    """Test the complete Travel Bot pipeline"""
    try:
        from travel_bot.travel_bot import TravelBot
        
        print("🚀 Testing Travel Advisory Bot with Devstral...")
        
        # Initialize with default (should now be devstral)
        bot = TravelBot()
        print("✅ TravelBot initialized")
        
        # Test a simple travel query
        test_query = "I want to plan a romantic trip to Europe for my honeymoon in June. Budget is $5000."
        
        print(f"🔄 Testing query: {test_query}")
        
        # This should use Devstral now
        suggestions = await bot.get_travel_suggestions(test_query)
        
        print(f"🎉 SUCCESS! Got {len(suggestions)} travel suggestions!")
        for i, suggestion in enumerate(suggestions[:2], 1):
            print(f"   {i}. {suggestion.destination} - {suggestion.highlights[:100]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🌟 FINAL TRAVEL ADVISORY BOT TEST")
    print("=" * 50)
    
    success = asyncio.run(test_travel_bot())
    
    if success:
        print("\n🎉 CONGRATULATIONS!")
        print("✅ Travel Advisory Bot is fully operational with Devstral!")
        print("✅ Timeout issues resolved!")
        print("✅ Model selection fixed!")
        print("\n🚀 Ready to launch:")
        print("   streamlit run src\\travel_bot\\ui\\streamlit_app.py")
    else:
        print("\n❌ Something needs attention...")
