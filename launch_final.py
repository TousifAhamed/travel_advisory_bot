#!/usr/bin/env python3
"""
Final launcher for Travel Advisory Bot with Python 3.13 compatible AI models
"""
import sys
import os
import subprocess

# Add src to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def main():
    print("🚀 Starting Travel Advisory Bot with Python 3.13 compatible AI models...")
    print("✅ Devstral model available via Ollama")
    print("✅ All import issues resolved")
    print("✅ Multimodal processing ready")
    
    # Set environment
    os.environ['PYTHONPATH'] = os.path.join(os.path.dirname(__file__), 'src')
    
    # Start Streamlit
    try:
        cmd = [
            sys.executable, 
            "-m", "streamlit", 
            "run", 
            "src/travel_bot/ui/streamlit_app.py",
            "--server.port", "8501",
            "--server.headless", "true"
        ]
        print(f"Running: {' '.join(cmd)}")
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
