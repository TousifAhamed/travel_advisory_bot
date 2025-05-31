#!/usr/bin/env python3
"""
Simple startup script for the Travel Advisory Bot
"""
import sys
import os
import subprocess

def main():
    print("🌍 Starting Travel Advisory Bot...")
    print("=" * 50)
    
    # Change to the project directory
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)
    
    # Add src to Python path
    src_path = os.path.join(project_dir, 'src')
    if src_path not in sys.path:
        sys.path.insert(0, src_path)
    
    print(f"📁 Project directory: {project_dir}")
    print(f"🐍 Python path: {src_path}")
    
    # Check if Streamlit is installed
    try:
        import streamlit
        print("✅ Streamlit is available")
    except ImportError:
        print("❌ Streamlit not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit", "python-dotenv"])
        print("✅ Streamlit installed")
    
    # Check if our modules can be imported
    try:
        from travel_bot.ui.streamlit_app import main as streamlit_main
        print("✅ Travel Bot modules imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import Travel Bot modules: {e}")
        print("⚠️ Running in demo mode...")
    
    # Start the Streamlit application
    print("\n🚀 Starting Streamlit application...")
    print("🌐 The application will open in your browser at: http://localhost:8501")
    print("⏹️ Press Ctrl+C to stop the application")
    print("\n" + "=" * 50)
    
    streamlit_app_path = os.path.join('src', 'travel_bot', 'ui', 'streamlit_app.py')
    
    try:
        # Use subprocess to run streamlit
        cmd = [sys.executable, "-m", "streamlit", "run", streamlit_app_path, "--server.port", "8501"]
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\n\n👋 Travel Advisory Bot stopped by user")
    except Exception as e:
        print(f"\n❌ Error starting application: {e}")
        print("🔧 Try running manually: streamlit run src/travel_bot/ui/streamlit_app.py")

if __name__ == "__main__":
    main()
