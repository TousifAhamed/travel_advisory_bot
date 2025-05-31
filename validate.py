#!/usr/bin/env python3
"""
Basic validation script to check the project structure
"""

import os
import sys

def check_project_structure():
    """Check if all required files and directories exist"""
    base_dir = os.path.dirname(__file__)
    
    required_files = [
        'main.py',
        'pyproject.toml',
        'README.md',
        '.env.example',
        'start.bat'
    ]
    
    required_dirs = [
        'src',
        'src/travel_bot',
        'src/travel_bot/models',
        'src/travel_bot/processors',
        'src/travel_bot/agents',
        'src/travel_bot/utils',
        'src/travel_bot/ui',
        'config'
    ]
    
    print("🔍 Checking project structure...")
    
    # Check files
    missing_files = []
    for file in required_files:
        path = os.path.join(base_dir, file)
        if os.path.exists(path):
            print(f"✅ Found: {file}")
        else:
            print(f"❌ Missing: {file}")
            missing_files.append(file)
    
    # Check directories
    missing_dirs = []
    for dir in required_dirs:
        path = os.path.join(base_dir, dir)
        if os.path.exists(path) and os.path.isdir(path):
            print(f"✅ Found: {dir}/")
        else:
            print(f"❌ Missing: {dir}/")
            missing_dirs.append(dir)
    
    if not missing_files and not missing_dirs:
        print("\n🎉 All required files and directories are present!")
        return True
    else:
        print(f"\n⚠️ Missing {len(missing_files)} files and {len(missing_dirs)} directories")
        return False

def check_python_imports():
    """Check if we can import our modules"""
    print("\n🐍 Checking Python imports...")
    
    # Add src to path
    src_path = os.path.join(os.path.dirname(__file__), 'src')
    if src_path not in sys.path:
        sys.path.insert(0, src_path)
    
    try:
        # Test basic imports
        from travel_bot.models import InputType, TravelPreferences
        print("✅ Core data models imported successfully")
        
        from travel_bot.travel_bot import TravelBot
        print("✅ Main TravelBot class imported successfully")
        
        from travel_bot.agents.travel_agent import SmartTravelAgent
        print("✅ SmartTravelAgent imported successfully")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def check_config():
    """Check configuration files"""
    print("\n⚙️ Checking configuration...")
    
    env_example = os.path.join(os.path.dirname(__file__), '.env.example')
    if os.path.exists(env_example):
        print("✅ .env.example file exists")
        
        # Check if .env exists
        env_file = os.path.join(os.path.dirname(__file__), '.env')
        if os.path.exists(env_file):
            print("✅ .env file exists")
        else:
            print("⚠️ .env file not found (copy from .env.example and add your API keys)")
            
        return True
    else:
        print("❌ .env.example file missing")
        return False

def main():
    """Run all validation checks"""
    print("🚀 Travel Advisory Bot - Project Validation")
    print("=" * 50)
    
    checks = [
        check_project_structure,
        check_python_imports,
        check_config
    ]
    
    passed = 0
    total = len(checks)
    
    for check in checks:
        try:
            if check():
                passed += 1
        except Exception as e:
            print(f"❌ Check failed with error: {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 Results: {passed}/{total} checks passed")
    
    if passed == total:
        print("🎉 All checks passed! The project is ready to use.")
        print("\n📝 Next steps:")
        print("1. Copy .env.example to .env and add your API keys")
        print("2. Run: python main.py")
        print("3. Open browser to http://localhost:8501")
    else:
        print("⚠️ Some checks failed. Please review the errors above.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
