#!/usr/bin/env python3
"""
Debug import issues step by step
"""

import sys
import os

# Add paths
current_dir = os.path.dirname(__file__)
src_dir = os.path.join(current_dir, 'src')
sys.path.insert(0, src_dir)

print("Testing imports step by step...")

try:
    print("1. Testing travel_bot.models imports...")
    from travel_bot.models import InputType, ProcessedInput
    print("✅ Basic models imported successfully")
except Exception as e:
    print(f"❌ Basic models import failed: {e}")
    sys.exit(1)

try:
    print("2. Testing ModelFactory import...")
    from travel_bot.models.ai_models import ModelFactory
    print("✅ ModelFactory imported successfully")
except Exception as e:
    print(f"❌ ModelFactory import failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

try:
    print("3. Testing processors imports...")
    from travel_bot.processors import ProcessorFactory
    print("✅ ProcessorFactory imported successfully")
except Exception as e:
    print(f"❌ ProcessorFactory import failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

try:
    print("4. Testing TravelBot import...")
    from travel_bot.travel_bot import TravelBot
    print("✅ TravelBot imported successfully")
except Exception as e:
    print(f"❌ TravelBot import failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n🎉 All imports successful! The issue is resolved.")
