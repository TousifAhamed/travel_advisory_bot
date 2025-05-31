import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_devstral_availability():
    try:
        from travel_bot.models.ai_models import DevstralModel
        model = DevstralModel()
        available = model.is_available()
        print(f"✅ DevStral Model Available: {available}")
        return available
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    test_devstral_availability()
