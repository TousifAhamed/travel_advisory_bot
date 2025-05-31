#!/usr/bin/env python3
"""
Direct Streamlit Launcher - Alternative to batch script
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    """Launch the Streamlit app directly"""
    
    # Set up paths
    project_root = Path(__file__).parent.absolute()
    src_dir = project_root / "src"
    
    # Set environment variables
    env = os.environ.copy()
    pythonpath = f"{project_root};{src_dir}"
    if 'PYTHONPATH' in env:
        pythonpath += f";{env['PYTHONPATH']}"
    env['PYTHONPATH'] = pythonpath
    
    # Add to sys.path as well
    sys.path.insert(0, str(project_root))
    sys.path.insert(0, str(src_dir))
    
    print("🤖 Starting Travel Advisory Bot 🌍")
    print("=" * 40)
    print(f"Project root: {project_root}")
    print(f"Python path: {pythonpath}")
    print()
    
    # Install dependencies
    print("📦 Installing dependencies...")
    try:
        subprocess.run([
            sys.executable, "-m", "pip", "install", 
            "streamlit", "python-dotenv", "requests", "--quiet"
        ], check=True)
        print("✅ Dependencies installed")
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Warning: Could not install dependencies: {e}")
    
    # Launch Streamlit
    streamlit_app = project_root / "src" / "travel_bot" / "ui" / "streamlit_app.py"
    
    if not streamlit_app.exists():
        print(f"❌ Streamlit app not found: {streamlit_app}")
        return 1
    
    print("🚀 Starting Streamlit application...")
    print("🌐 Browser will open at: http://localhost:8501")
    print("🤖 Using Devstral for AI processing")
    print("⏹️ Press Ctrl+C to stop")
    print()
    
    try:
        cmd = [
            sys.executable, "-m", "streamlit", "run",
            str(streamlit_app),
            "--server.port", "8501",
            "--server.address", "localhost"
        ]
        
        subprocess.run(cmd, env=env, cwd=str(project_root))
        
    except KeyboardInterrupt:
        print("\n🛑 Shutting down gracefully...")
        return 0
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1

if __name__ == "__main__":
    exit_code = main()
    input("Press Enter to exit...")
    sys.exit(exit_code)
