#!/usr/bin/env python3
"""
Clean restart script for the Travel Advisory Bot
"""
import os
import sys
import subprocess
import time

def main():
    # Change to the project directory
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)
    
    print("🚀 Starting Travel Advisory Bot...")
    print(f"📁 Working directory: {project_dir}")
    
    # Kill any existing Streamlit processes
    try:
        subprocess.run(["taskkill", "/F", "/IM", "python.exe"], 
                      capture_output=True, check=False)
        time.sleep(2)
    except:
        pass
    
    # Start Streamlit
    cmd = [
        sys.executable, "-m", "streamlit", "run", 
        "src/travel_bot/ui/streamlit_app.py",
        "--server.port", "8501",
        "--server.address", "localhost"
    ]
    
    print(f"🔧 Running command: {' '.join(cmd)}")
    
    try:
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        print("\n⏹️  Stopping application...")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
