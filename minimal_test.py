print("Starting basic test...")

import sys
import os

# Add paths
sys.path.insert(0, ".")
sys.path.insert(0, "src")

print("Testing imports...")

# Test 1
try:
    from travel_bot.models import InputType
    print("SUCCESS: InputType imported")
except Exception as e:
    print(f"FAILED: InputType - {e}")

# Test 2  
try:
    from travel_bot.models.ai_models import ModelFactory
    print("SUCCESS: ModelFactory imported")
except Exception as e:
    print(f"FAILED: ModelFactory - {e}")

print("Test complete.")
