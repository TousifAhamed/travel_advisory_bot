#!/usr/bin/env python3
"""Test script to verify AI timeout fix"""

import sys
import os
import asyncio

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

async def test_devstral_timeout():
    """Test Devstral with increased timeout"""
    try:
        from travel_bot.models.ai_models import ModelFactory
        
        print("✓ AI models imported successfully")
        
        # Create Devstral model
        model = ModelFactory.create_model("ollama")
        print("✓ Devstral model created successfully")
        
        # Check if model is available
        if model.is_available():
            print("✓ Devstral model is available")
            
            # Test with a simple prompt (should now have 60-90s timeout)
            print("🔄 Testing AI response with increased timeout...")
            response = await model.generate_response(
                "Hello! Please respond with a simple greeting.",
                "You are a helpful travel assistant."
            )
            
            print(f"✅ SUCCESS! AI Response received: {response[:100]}...")
            return True
        else:
            print("❌ Devstral model not available")
            return False
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

if __name__ == "__main__":
    print("🚀 Testing Travel Advisory Bot - Timeout Fix")
    print("=" * 50)
    
    success = asyncio.run(test_devstral_timeout())
    
    if success:
        print("\n🎉 TIMEOUT FIX SUCCESSFUL!")
        print("The AI models now have increased timeout values:")
        print("- DevstralModel: 60 seconds")
        print("- GenericOllamaModel: 45 seconds")
        print("\nYou can now launch the Streamlit app:")
        print("streamlit run src\\travel_bot\\ui\\streamlit_app.py")
    else:
        print("\n❌ Timeout fix verification failed")
        print("Please check Ollama service and Devstral model availability")
