import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

print("Testing imports...")
try:
    from travel_bot.models import InputType
    print("✅ InputType imported")
    
    from travel_bot.travel_bot import TravelBot
    print("✅ TravelBot imported")
    
    print("✅ All imports successful!")
except Exception as e:
    print(f"❌ Error: {e}")
