#!/usr/bin/env python3
"""
Streamlit Launcher for Travel Advisory Bot
Properly sets up Python paths and launches the Streamlit app
"""

import os
import sys
import subprocess
from pathlib import Path

def setup_paths():
    """Setup Python paths for the project"""
    # Get the absolute path to the project root
    project_root = Path(__file__).parent.absolute()
    src_dir = project_root / "src"
    
    # Add paths to Python path
    paths_to_add = [
        str(project_root),
        str(src_dir),
        str(project_root / "config"),
    ]
    
    for path in paths_to_add:
        if path not in sys.path:
            sys.path.insert(0, path)
    
    # Set environment variables for subprocess
    env = os.environ.copy()
    current_pythonpath = env.get('PYTHONPATH', '')
    new_pythonpath = os.pathsep.join(paths_to_add + [current_pythonpath] if current_pythonpath else paths_to_add)
    env['PYTHONPATH'] = new_pythonpath
    
    return env

def check_dependencies():
    """Check if required dependencies are available"""
    try:
        import streamlit
        import ollama
        print("✅ Core dependencies found")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please install dependencies with: pip install -e .")
        return False

def main():
    """Main launcher function"""
    print("🚀 Travel Advisory Bot - Streamlit Launcher")
    print("=" * 50)
    
    # Setup paths
    env = setup_paths()
    
    # Check dependencies
    if not check_dependencies():
        return 1
    
    # Get the path to the Streamlit app
    project_root = Path(__file__).parent.absolute()
    streamlit_app_path = project_root / "src" / "travel_bot" / "ui" / "streamlit_app.py"
    
    if not streamlit_app_path.exists():
        print(f"❌ Streamlit app not found at: {streamlit_app_path}")
        return 1
    
    print(f"📍 Project root: {project_root}")
    print(f"🎯 Launching app: {streamlit_app_path}")
    print("🌐 App will be available at: http://localhost:8501")
    print("-" * 50)
    
    # Launch Streamlit
    try:
        cmd = [
            sys.executable, "-m", "streamlit", "run", 
            str(streamlit_app_path),
            "--server.port", "8501",
            "--server.address", "localhost"
        ]
        
        result = subprocess.run(cmd, env=env, cwd=str(project_root))
        return result.returncode
        
    except KeyboardInterrupt:
        print("\n🛑 Shutting down gracefully...")
        return 0
    except Exception as e:
        print(f"❌ Error launching Streamlit: {e}")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
