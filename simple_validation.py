import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

print("Starting validation...")

try:
    from travel_bot.processors.text_processor import TextProcessor
    print("SUCCESS: TextProcessor imported")
except Exception as e:
    print(f"ERROR: TextProcessor - {e}")

try:
    from travel_bot.processors import ProcessorFactory
    print("SUCCESS: ProcessorFactory imported")
except Exception as e:
    print(f"ERROR: ProcessorFactory - {e}")

try:
    from travel_bot.travel_bot import TravelBot
    print("SUCCESS: TravelBot imported")
except Exception as e:
    print(f"ERROR: TravelBot - {e}")

print("Validation complete!")
