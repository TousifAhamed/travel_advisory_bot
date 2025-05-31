#!/usr/bin/env python3
"""
Launch script for Travel Advisory Bot
Tests imports and launches the Streamlit application
"""

import os
import sys
import subprocess

def setup_paths():
    """Setup Python paths"""
    current_dir = os.path.dirname(__file__)
    project_root = os.path.abspath(current_dir)
    src_dir = os.path.join(project_root, 'src')
    
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    if src_dir not in sys.path:
        sys.path.insert(0, src_dir)
    
    print(f"✅ Project root: {project_root}")
    print(f"✅ Source directory: {src_dir}")

def test_imports():
    """Test critical imports"""
    print("\n🔍 Testing imports...")
    
    try:
        from travel_bot.models import InputType, TravelPreferences
        print("✅ Basic models imported")
        
        from travel_bot.models.ai_models import ModelFactory
        print("✅ ModelFactory imported") 
        
        from travel_bot.travel_bot import TravelBot
        print("✅ TravelBot imported")
        
        print("🎉 All imports successful!")
        return True
        
    except Exception as e:
        print(f"❌ Import failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def launch_app():
    """Launch the Streamlit application"""
    print("\n🚀 Launching Travel Advisory Bot...")
    
    app_path = os.path.join("src", "travel_bot", "ui", "streamlit_app.py")
    
    if not os.path.exists(app_path):
        print(f"❌ App file not found: {app_path}")
        return False
    
    try:
        # Launch streamlit
        cmd = [sys.executable, "-m", "streamlit", "run", app_path, "--server.port", "8501"]
        print(f"🔧 Command: {' '.join(cmd)}")
        
        # Run the command
        process = subprocess.Popen(cmd)
        print(f"✅ Streamlit started with PID: {process.pid}")
        print("🌐 Open http://localhost:8501 in your browser")
        
        return True
        
    except Exception as e:
        print(f"❌ Failed to launch: {e}")
        return False

def main():
    print("🤖 Travel Advisory Bot Launcher")
    print("=" * 50)
    
    setup_paths()
    
    if test_imports():
        launch_app()
        print("\n✅ Launch complete! Check your browser at http://localhost:8501")
    else:
        print("\n❌ Import tests failed. Cannot launch application.")

if __name__ == "__main__":
    main()
