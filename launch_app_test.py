import subprocess
import sys
import os
import time

def launch_streamlit():
    """Launch the Streamlit application"""
    
    # Set up environment
    os.chdir(r"C:\DEV\Travel_Advisory_Bot\travel-advisory-bot")
    
    print("🚀 Starting Travel Advisory Bot...")
    print(f"📁 Working directory: {os.getcwd()}")
    
    # Test imports first
    try:
        print("🔍 Testing imports...")
        from src.travel_bot.models import InputType
        from src.travel_bot.utils.travel_utils import TravelUtils
        print("✅ All imports successful!")
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False
    
    # Launch Streamlit
    try:
        cmd = [
            sys.executable, "-m", "streamlit", "run", 
            r"src\travel_bot\ui\streamlit_app.py",
            "--server.port", "8501"
        ]
        
        print(f"🔧 Command: {' '.join(cmd)}")
        
        # Start the process
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            universal_newlines=True
        )
        
        print(f"✅ Streamlit started with PID: {process.pid}")
        print("🌐 Application should be available at: http://localhost:8501")
        
        # Wait a moment to see if it starts successfully
        time.sleep(3)
        
        if process.poll() is None:
            print("🎉 Application is running!")
            return True
        else:
            stdout, stderr = process.communicate()
            print(f"❌ Process terminated. stdout: {stdout}, stderr: {stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Failed to start: {e}")
        return False

if __name__ == "__main__":
    success = launch_streamlit()
    if success:
        print("\n✅ LAUNCH SUCCESSFUL!")
        print("💡 Open http://localhost:8501 in your web browser")
        print("📝 The application is ready to use!")
    else:
        print("\n❌ Launch failed. Check the error messages above.")
