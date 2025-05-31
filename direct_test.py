import sys
sys.path.insert(0, 'src')

try:
    print("1. Testing direct models import...")
    import travel_bot.models
    print("✅ Models module imported")
    
    print("2. Testing InputType...")
    from travel_bot.models import InputType
    print("✅ InputType imported")
    
    print("3. Testing ai_models...")
    import travel_bot.models.ai_models
    print("✅ ai_models module imported")
    
    print("4. Testing ModelFactory...")
    from travel_bot.models.ai_models import ModelFactory
    print("✅ ModelFactory imported")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
