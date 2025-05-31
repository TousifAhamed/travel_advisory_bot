import os
import sys

print("Python executable:", sys.executable)
print("Python version:", sys.version)
print("Current working directory:", os.getcwd())

# Add paths
current_dir = os.path.dirname(__file__)
project_root = os.path.join(current_dir, '.')
src_dir = os.path.join(project_root, 'src')
sys.path.insert(0, project_root)
sys.path.insert(0, src_dir)

print("Python path:", sys.path[:3])
print("=" * 50)

# Test 1: Basic enum import
print("Test 1: Basic enum import")
try:
    from travel_bot.models import InputType
    print("✅ InputType imported successfully")
    print("Available types:", [t.value for t in InputType])
except Exception as e:
    print("❌ InputType import failed:", str(e))
    import traceback
    traceback.print_exc()

print("=" * 50)

# Test 2: ModelFactory import
print("Test 2: ModelFactory import")
try:
    from travel_bot.models.ai_models import ModelFactory
    print("✅ ModelFactory imported successfully")
except Exception as e:
    print("❌ ModelFactory import failed:", str(e))
    import traceback
    traceback.print_exc()

print("=" * 50)

# Test 3: Complete app import
print("Test 3: TravelBot import")
try:
    from travel_bot.travel_bot import TravelBot
    print("✅ TravelBot imported successfully")
except Exception as e:
    print("❌ TravelBot import failed:", str(e))
    import traceback
    traceback.print_exc()

print("✅ All tests completed!")
