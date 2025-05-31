import os
import sys

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

print("Testing Travel Bot imports...")

try:
    from travel_bot.models import InputType
    print("✅ InputType imported")
except Exception as e:
    print(f"❌ InputType failed: {e}")

try:
    from travel_bot.models import TravelPreferences
    print("✅ TravelPreferences imported")
except Exception as e:
    print(f"❌ TravelPreferences failed: {e}")

try:
    from travel_bot.processors.text_processor import TextProcessor
    print("✅ TextProcessor imported")
except Exception as e:
    print(f"❌ TextProcessor failed: {e}")

try:
    from travel_bot.ui.streamlit_app import main
    print("✅ Streamlit app imported")
except Exception as e:
    print(f"❌ Streamlit app failed: {e}")

print("Test complete!")
