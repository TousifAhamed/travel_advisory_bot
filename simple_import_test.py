import sys
import os

# Add paths
sys.path.insert(0, 'src')

try:
    print("Testing basic import...")
    from travel_bot.models import InputType
    print("✅ InputType import successful")
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
