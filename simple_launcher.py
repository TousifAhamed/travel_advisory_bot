"""
Simple launcher for Travel Advisory Bot
Bypasses complex imports and starts directly
"""

import subprocess
import sys
import os
import time

def start_app():
    """Start the Streamlit application"""
    print("🚀 Starting Travel Advisory Bot...")
    print("=" * 50)
    
    # Change to the correct directory
    os.chdir(r"c:\DEV\Travel_Advisory_Bot\travel-advisory-bot")
    
    # Clear any cached imports
    if 'travel_bot' in sys.modules:
        del sys.modules['travel_bot']
    
    # Start Streamlit
    try:
        cmd = [
            sys.executable, 
            "-m", "streamlit", "run", 
            "src\\travel_bot\\ui\\streamlit_app.py",
            "--server.port", "8501",
            "--server.headless", "true"
        ]
        
        print(f"Running command: {' '.join(cmd)}")
        print("Starting Streamlit server...")
        print("Once started, open: http://localhost:8501")
        print("=" * 50)
        
        # Start the process
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        
        # Monitor output
        startup_complete = False
        for line in iter(process.stdout.readline, ''):
            print(line.strip())
            if "Local URL: http://localhost:8501" in line or "Network URL:" in line:
                startup_complete = True
                print("\n✅ Streamlit server started successfully!")
                print("🌐 Application available at: http://localhost:8501")
                break
            if process.poll() is not None:
                break
        
        if startup_complete:
            print("\n🎉 Travel Advisory Bot is now running!")
            print("Open your browser to http://localhost:8501 to use the application.")
            
            # Keep the process running
            try:
                process.wait()
            except KeyboardInterrupt:
                print("\n🛑 Shutting down...")
                process.terminate()
        else:
            print("❌ Failed to start the application. Check the output above for errors.")
            return process.returncode
        
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = start_app()
    sys.exit(exit_code)
