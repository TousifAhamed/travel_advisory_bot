import sys
import os

# Add the project root and src directory to the Python path
current_dir = os.path.dirname(__file__)
project_root = os.path.join(current_dir, '.')
src_dir = os.path.join(project_root, 'src')
sys.path.insert(0, project_root)
sys.path.insert(0, src_dir)

print("Testing imports...")

try:
    from travel_bot.models import InputType, TravelPreferences
    print("✅ Basic models imported")
except Exception as e:
    print(f"❌ Basic models failed: {e}")

try:
    from travel_bot.models.ai_models import ModelFactory
    print("✅ ModelFactory imported")
except Exception as e:
    print(f"❌ ModelFactory failed: {e}")

try:
    from travel_bot.travel_bot import TravelBot
    print("✅ TravelBot imported")
except Exception as e:
    print(f"❌ TravelBot failed: {e}")

print("Import test complete!")
