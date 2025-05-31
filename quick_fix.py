#!/usr/bin/env python3
"""
Quick Fix for Travel Advisory Bot Import Issues
This script installs missing dependencies and restarts the app
"""

import subprocess
import sys
import os
from pathlib import Path

def install_dependencies():
    """Install missing dependencies"""
    print("📦 Installing missing dependencies...")
    
    # List of dependencies to install
    deps = [
        "openai-whisper",
        "langdetect", 
        "googletrans==4.0.0rc1",
        "transformers",
        "torch",
        "PyPDF2",
        "Pillow",
        "opencv-python"
    ]
    
    for dep in deps:
        try:
            print(f"   Installing {dep}...")
            subprocess.run([sys.executable, "-m", "pip", "install", dep, "--quiet"], 
                         check=True, capture_output=True)
            print(f"   ✅ {dep} installed")
        except subprocess.CalledProcessError as e:
            print(f"   ⚠️ Failed to install {dep}: {e}")

def clear_cache():
    """Clear Python cache files"""
    print("\n🧹 Clearing Python cache...")
    
    cache_dirs = [
        "src/travel_bot/__pycache__",
        "src/travel_bot/processors/__pycache__",
        "src/travel_bot/models/__pycache__",
        "src/travel_bot/agents/__pycache__",
        "src/travel_bot/utils/__pycache__",
        "config/__pycache__"
    ]
    
    for cache_dir in cache_dirs:
        cache_path = Path(cache_dir)
        if cache_path.exists():
            import shutil
            shutil.rmtree(cache_path)
            print(f"   ✅ Cleared {cache_dir}")

def test_imports():
    """Test if imports work now"""
    print("\n🧪 Testing imports...")
    
    # Setup paths
    project_root = Path(__file__).parent.absolute()
    src_dir = project_root / "src"
    sys.path.insert(0, str(project_root))
    sys.path.insert(0, str(src_dir))
    
    try:
        from travel_bot.travel_bot import TravelBot
        print("   ✅ TravelBot imports successfully")
        return True
    except Exception as e:
        print(f"   ❌ TravelBot import failed: {e}")
        return False

def restart_streamlit():
    """Restart Streamlit application"""
    print("\n🚀 Restarting Streamlit...")
    
    # Kill existing processes (Windows)
    try:
        subprocess.run(["taskkill", "/f", "/im", "python.exe", "/fi", "WINDOWTITLE eq *streamlit*"], 
                      capture_output=True)
    except:
        pass
    
    # Set environment
    env = os.environ.copy()
    project_root = Path(__file__).parent.absolute()
    env['PYTHONPATH'] = f"{project_root};{project_root}/src;{env.get('PYTHONPATH', '')}"
    
    # Start Streamlit
    streamlit_app = project_root / "src" / "travel_bot" / "ui" / "streamlit_app.py"
    
    print(f"   Starting Streamlit at: {streamlit_app}")
    print("   🌐 Browser will open at: http://localhost:8501")
    
    try:
        subprocess.Popen([
            sys.executable, "-m", "streamlit", "run", 
            str(streamlit_app),
            "--server.port", "8501",
            "--server.address", "localhost"
        ], env=env, cwd=str(project_root))
        
        print("   ✅ Streamlit started successfully")
        return True
    except Exception as e:
        print(f"   ❌ Failed to start Streamlit: {e}")
        return False

def main():
    """Main fix function"""
    print("🔧 Travel Advisory Bot - Quick Fix")
    print("=" * 40)
    
    # Install dependencies
    install_dependencies()
    
    # Clear cache
    clear_cache()
    
    # Test imports
    imports_ok = test_imports()
    
    if imports_ok:
        # Restart Streamlit
        restart_ok = restart_streamlit()
        
        if restart_ok:
            print("\n🎉 Fix completed successfully!")
            print("📱 Check your browser at: http://localhost:8501")
            print("🔄 If the page shows errors, refresh it.")
        else:
            print("\n⚠️ Imports fixed but Streamlit restart failed.")
            print("💡 Try running: python -m streamlit run src\\travel_bot\\ui\\streamlit_app.py")
    else:
        print("\n❌ Import issues persist.")
        print("💡 Try running the minimal app: python -m streamlit run minimal_app.py")
    
    print("\n🏁 Fix script completed.")

if __name__ == "__main__":
    main()
