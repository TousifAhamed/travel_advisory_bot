"""
Simple launcher for the Travel Advisory Bot
"""
import os
import sys
import subprocess

def main():
    print("🌍 Travel Advisory Bot Launcher")
    print("=" * 40)
    
    # Get the project directory
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)
    
    print(f"📁 Working directory: {project_dir}")
    
    # Check for Streamlit
    try:
        import streamlit
        print("✅ Streamlit found")
    except ImportError:
        print("⚠️ Installing Streamlit...")
        subprocess.run([sys.executable, "-m", "pip", "install", "streamlit", "python-dotenv", "--quiet"])
        print("✅ Streamlit installed")
    
    # Check for .env file
    if not os.path.exists(".env"):
        if os.path.exists(".env.example"):
            import shutil
            shutil.copy(".env.example", ".env")
            print("✅ Created .env file from template")
        else:
            print("⚠️ No .env file found")
    
    # Run the Streamlit app
    streamlit_file = os.path.join("src", "travel_bot", "ui", "streamlit_app.py")
    if os.path.exists(streamlit_file):
        print(f"🚀 Starting application...")
        print(f"🌐 Open your browser to: http://localhost:8501")
        print(f"⏹️ Press Ctrl+C to stop")
        print("-" * 40)
        
        try:
            subprocess.run([
                sys.executable, "-m", "streamlit", "run", 
                streamlit_file, 
                "--server.port", "8501",
                "--server.headless", "false"
            ])
        except KeyboardInterrupt:
            print("\n👋 Application stopped")
    else:
        print(f"❌ Streamlit app not found at: {streamlit_file}")

if __name__ == "__main__":
    main()
