#!/usr/bin/env python3
"""
Test AI connectivity with timeout fixes for Travel Advisory Bot
"""

import asyncio
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

async def test_ai_connectivity():
    """Test AI model connectivity with proper timeout handling"""
    print("🧪 Testing AI Model Connectivity with Timeout Fixes...")
    print("=" * 60)
    
    try:
        from travel_bot.models.ai_models import DevstralModel, ModelFactory
        
        print("✅ AI models imported successfully")
        
        # Test DevStral model
        print("\n🤖 Testing DevStral Model...")
        devstral = DevstralModel()
        
        print(f"📡 Checking DevStral availability...")
        is_available = devstral.is_available()
        print(f"   Available: {is_available}")
        
        if is_available:
            print("🔄 Testing AI response generation...")
            test_prompt = "Suggest a weekend getaway destination within 300 miles of San Francisco for a family with young children. Include budget considerations."
            
            try:
                response = await devstral.generate_response(test_prompt)
                print(f"✅ AI Response Generated Successfully!")
                print(f"📝 Response length: {len(response)} characters")
                print(f"📋 Response preview: {response[:200]}...")
                
                # Test the travel advisory specific functionality
                print("\n🧳 Testing Travel Advisory Analysis...")
                from travel_bot.models.data_models import ProcessedInput, InputType
                
                test_input = ProcessedInput(
                    input_type=InputType.TEXT,
                    content="Planning a 2-week vacation to Europe in July with a budget of $5000 for 2 people",
                    metadata={"urgency": "planning", "travelers": 2}
                )
                
                analysis = await devstral.analyze_input(test_input)
                print(f"✅ Travel Analysis Generated!")
                print(f"📊 Analysis keys: {list(analysis.keys())}")
                
            except Exception as e:
                print(f"❌ AI Response Error: {str(e)}")
                if "timeout" in str(e).lower():
                    print("⏰ This appears to be a timeout issue - the 120s timeout should resolve this")
                elif "connection" in str(e).lower():
                    print("🔌 Connection issue - ensure Ollama is running")
        else:
            print("❌ DevStral not available - ensure Ollama is running with DevStral model")
            print("💡 Run: ollama pull devstral")
        
        # Test ModelFactory
        print("\n🏭 Testing ModelFactory...")
        available_models = ModelFactory.get_available_models()
        print(f"📋 Available models: {len(available_models)}")
        for model in available_models:
            status = "✅" if model['available'] else "❌"
            print(f"   {status} {model['name']} ({model['type']}) - {model['specialization']}")
        
        best_model = ModelFactory.get_best_available_model()
        print(f"🏆 Best available model: {best_model.__class__.__name__}")
        
    except ImportError as e:
        print(f"❌ Import Error: {str(e)}")
        print("🔧 Check that all dependencies are properly installed")
    except Exception as e:
        print(f"❌ Unexpected Error: {str(e)}")
    
    print("\n" + "=" * 60)
    print("🎯 AI Connectivity Test Complete")

if __name__ == "__main__":
    asyncio.run(test_ai_connectivity())
