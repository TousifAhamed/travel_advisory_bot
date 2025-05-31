#!/usr/bin/env python3
"""
Test script to verify Devstral integration with the Travel Advisory Bot
"""

import sys
import os
import asyncio
import requests

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from travel_bot.models.ai_models import OllamaModel
from travel_bot.models import InputType, TravelPreferences, ProcessedInput

async def test_devstral_connection():
    """Test connection to local Devstral model"""
    print("🤖 Testing Devstral Connection")
    print("=" * 40)
    
    # Test basic Ollama API connection
    print("1. Testing Ollama API connection...")
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json().get('models', [])
            model_names = [model['name'] for model in models]
            print(f"✅ Ollama is running")
            print(f"📋 Available models: {', '.join(model_names)}")
            
            if any('devstral' in name.lower() for name in model_names):
                print("✅ Devstral model found!")
            else:
                print("⚠️ Devstral model not found. Available models:")
                for name in model_names:
                    print(f"   - {name}")
                print("\nTo install Devstral, run: ollama pull devstral")
        else:
            print(f"❌ Ollama API returned status: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to Ollama at http://localhost:11434")
        print("💡 Make sure Ollama is running: ollama serve")
        return False
    except Exception as e:
        print(f"❌ Error checking Ollama: {e}")
        return False
    
    # Test Devstral model initialization
    print("\n2. Testing Devstral model initialization...")
    try:
        devstral = OllamaModel("devstral")
        print("✅ Devstral model initialized")
    except Exception as e:
        print(f"❌ Failed to initialize Devstral: {e}")
        return False
    
    # Test simple response generation
    print("\n3. Testing response generation...")
    try:
        test_prompt = "Hello! I want to plan a 3-day trip to Paris. Can you help me?"
        response = await devstral.generate_response(test_prompt)
        print("✅ Response generated successfully")
        print(f"📝 Sample response (first 200 chars): {response[:200]}...")
    except Exception as e:
        print(f"❌ Failed to generate response: {e}")
        return False
    
    # Test travel-specific analysis
    print("\n4. Testing travel content analysis...")
    try:
        processed_input = ProcessedInput(
            type=InputType.TEXT,
            content="I'm planning a family vacation to Japan in spring 2025. We have a budget of $5000 and love cultural experiences and food.",
            metadata={"source": "user_input"}
        )
        
        analysis = await devstral.analyze_input(processed_input)
        print("✅ Travel analysis completed")
        print(f"📊 Analysis result: {str(analysis)[:200]}...")
    except Exception as e:
        print(f"❌ Failed to analyze travel content: {e}")
        return False
    
    print("\n" + "=" * 40)
    print("🎉 All Devstral tests passed!")
    return True

async def test_travel_bot_integration():
    """Test full Travel Bot integration with Devstral"""
    print("\n🚀 Testing Travel Bot Integration")
    print("=" * 40)
    
    try:
        from travel_bot.travel_bot import TravelBot
        
        # Initialize TravelBot with Ollama/Devstral
        travel_bot = TravelBot()
        print("✅ TravelBot initialized")
        
        # Test travel suggestions
        preferences = TravelPreferences(
            destinations=["Japan"],
            budget_range=(3000, 5000),
            travel_dates="Spring 2025",
            group_size=4,
            interests=["culture", "food", "history"]
        )
        
        suggestions = await travel_bot.get_travel_suggestions(preferences)
        print("✅ Travel suggestions generated")
        print(f"📋 Number of suggestions: {len(suggestions)}")
        
        if suggestions:
            print(f"🎯 Sample suggestion: {suggestions[0].title}")
        
        return True
        
    except Exception as e:
        print(f"❌ Travel Bot integration error: {e}")
        return False

def main():
    """Run all Devstral tests"""
    print("🌍 Travel Advisory Bot - Devstral Integration Test")
    print("=" * 60)
    
    # Run async tests
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    try:
        # Test Devstral connection
        devstral_ok = loop.run_until_complete(test_devstral_connection())
        
        if devstral_ok:
            # Test full integration
            integration_ok = loop.run_until_complete(test_travel_bot_integration())
            
            if integration_ok:
                print("\n🎉 SUCCESS: Your Travel Advisory Bot is ready to use Devstral!")
                print("\n🚀 Next steps:")
                print("1. Run: python run_bot.py")
                print("2. Open browser to: http://localhost:8501")
                print("3. Start planning your travels with local AI!")
            else:
                print("\n⚠️ Devstral works but integration needs attention")
        else:
            print("\n❌ Please fix Devstral connection first")
            
    except Exception as e:
        print(f"❌ Test error: {e}")
    finally:
        loop.close()

if __name__ == "__main__":
    main()
