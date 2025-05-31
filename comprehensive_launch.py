#!/usr/bin/env python3
"""
Travel Advisory Bot - Comprehensive Launch and Test Script
This script tests all components and launches the application
"""

import sys
import os
import subprocess
import time
import requests
import json
from pathlib import Path

# Add src to Python path
project_root = Path(__file__).parent
src_path = project_root / "src"
sys.path.insert(0, str(src_path))

def print_header(title):
    """Print a formatted header"""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)

def test_ollama_connection():
    """Test Ollama connection and Devstral availability"""
    print_header("TESTING OLLAMA & DEVSTRAL")
    
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json().get('models', [])
            devstral_found = any('devstral' in model.get('name', '') for model in models)
            
            print("✅ Ollama is running")
            print(f"📊 Available models: {len(models)}")
            
            if devstral_found:
                print("✅ Devstral model is available")
                return True
            else:
                print("❌ Devstral model not found")
                print("Available models:")
                for model in models:
                    print(f"  - {model.get('name', 'Unknown')}")
                return False
        else:
            print(f"❌ Ollama responded with status {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Cannot connect to Ollama: {e}")
        print("Please ensure Ollama is running on http://localhost:11434")
        return False

def test_imports():
    """Test all critical imports"""
    print_header("TESTING IMPORTS")
    
    try:
        print("Importing AI models...")
        from travel_bot.models.ai_models import DevstralModel, AIModelManager, InputType, ProcessedInput
        print("✅ AI Models imported successfully")
        
        print("Importing processors...")
        from travel_bot.processors.text_processor import TextProcessor
        from travel_bot.processors.image_processor import ImageProcessor  
        from travel_bot.processors.audio_processor import AudioProcessor
        print("✅ Processors imported successfully")
        
        print("Importing main bot...")
        from travel_bot.travel_bot import TravelBot
        print("✅ TravelBot imported successfully")
        
        print("Importing Streamlit app...")
        from travel_bot.ui.streamlit_app import main
        print("✅ Streamlit app imported successfully")
        
        return True
        
    except Exception as e:
        print(f"❌ Import failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_ai_model():
    """Test AI model functionality"""
    print_header("TESTING AI MODEL")
    
    try:
        from travel_bot.models.ai_models import DevstralModel, AIModelManager
        
        # Test DevStral directly
        devstral = DevstralModel()
        print(f"DevStral available: {'✅' if devstral.is_available() else '❌'}")
        
        # Test AI Model Manager
        manager = AIModelManager()
        available_models = manager.get_available_models()
        print(f"Available models via manager: {available_models}")
        
        if manager.primary_model:
            print(f"✅ Primary model: {manager.primary_model.__class__.__name__}")
            return True
        else:
            print("❌ No primary model available")
            return False
            
    except Exception as e:
        print(f"❌ AI model test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_travel_bot():
    """Test TravelBot functionality"""
    print_header("TESTING TRAVEL BOT")
    
    try:
        from travel_bot.travel_bot import TravelBot
        from travel_bot.models.ai_models import InputType
        
        # Initialize bot
        bot = TravelBot()
        print("✅ TravelBot initialized")
        
        # Test simple text processing
        test_query = "I want to visit Japan for 2 weeks with a $3000 budget"
        print(f"Testing query: '{test_query}'")
        
        result = bot.process_input(test_query, InputType.TEXT)
        
        if result and isinstance(result, dict):
            print("✅ Text processing successful")
            print(f"Result keys: {list(result.keys())}")
            return True
        else:
            print(f"❌ Text processing failed: {result}")
            return False
            
    except Exception as e:
        print(f"❌ TravelBot test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def launch_streamlit():
    """Launch the Streamlit application"""
    print_header("LAUNCHING STREAMLIT APPLICATION")
    
    try:
        # Check if Streamlit is already running
        try:
            response = requests.get("http://localhost:8501", timeout=2)
            if response.status_code == 200:
                print("⚠️  Streamlit might already be running on port 8501")
                print("🌐 Application should be available at: http://localhost:8501")
                return True
        except:
            pass
        
        # Start Streamlit
        cmd = [
            sys.executable, 
            "-m", "streamlit", "run", 
            str(src_path / "travel_bot" / "ui" / "streamlit_app.py"),
            "--server.port", "8501",
            "--server.headless", "true"
        ]
        
        print(f"Starting command: {' '.join(cmd)}")
        print("🚀 Launching Streamlit...")
        
        # Start the process in background
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            cwd=str(project_root)
        )
        
        # Wait for startup
        print("⏳ Waiting for Streamlit to start...")
        startup_time = 0
        max_wait = 30  # seconds
        
        while startup_time < max_wait:
            try:
                response = requests.get("http://localhost:8501", timeout=1)
                if response.status_code == 200:
                    print("✅ Streamlit started successfully!")
                    print("🌐 Application available at: http://localhost:8501")
                    print("🎉 Travel Advisory Bot is now running!")
                    return True
            except:
                pass
            
            time.sleep(1)
            startup_time += 1
            
            # Check if process is still running
            if process.poll() is not None:
                print("❌ Streamlit process ended unexpectedly")
                output = process.stdout.read()
                print(f"Process output: {output}")
                return False
        
        print("❌ Streamlit failed to start within 30 seconds")
        process.terminate()
        return False
        
    except Exception as e:
        print(f"❌ Failed to launch Streamlit: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main execution function"""
    print("🚀 TRAVEL ADVISORY BOT - COMPREHENSIVE LAUNCH")
    print(f"📁 Project root: {project_root}")
    print(f"🐍 Python version: {sys.version}")
    
    # Change to project directory
    os.chdir(project_root)
    
    # Run all tests
    tests = [
        ("Ollama & Devstral", test_ollama_connection),
        ("Python Imports", test_imports),
        ("AI Model", test_ai_model),
        ("TravelBot", test_travel_bot),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            success = test_func()
            results.append((test_name, success))
        except Exception as e:
            print(f"❌ {test_name} test crashed: {e}")
            results.append((test_name, False))
    
    # Print test summary
    print_header("TEST RESULTS SUMMARY")
    passed = 0
    for test_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{test_name:.<30} {status}")
        if success:
            passed += 1
    
    print(f"\n📊 Overall: {passed}/{len(results)} tests passed")
    
    # Launch application if all tests pass
    if passed == len(results):
        print("\n🎯 All tests passed! Launching application...")
        if launch_streamlit():
            print("\n🎉 MISSION ACCOMPLISHED!")
            print("✨ Travel Advisory Bot is running successfully!")
            print("🌐 Open your browser to: http://localhost:8501")
            print("📱 You can now upload documents and ask travel questions!")
        else:
            print("\n❌ Failed to launch application")
            return 1
    else:
        print(f"\n⚠️  {len(results) - passed} tests failed. Please fix the issues above.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
