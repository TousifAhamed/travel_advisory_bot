#!/usr/bin/env python3
"""
Comprehensive Import Test and Path Resolution
"""

import os
import sys
from pathlib import Path
import traceback

def setup_paths():
    """Setup Python paths for the project"""
    print("🔧 Setting up Python paths...")
    
    # Get the absolute path to the project root (where this script is located)
    script_path = Path(__file__).absolute()
    project_root = script_path.parent
    src_dir = project_root / "src"
    config_dir = project_root / "config"
    
    print(f"Script location: {script_path}")
    print(f"Project root: {project_root}")
    print(f"Src directory: {src_dir}")
    print(f"Config directory: {config_dir}")
    
    # Check if directories exist
    print(f"Src exists: {src_dir.exists()}")
    print(f"Config exists: {config_dir.exists()}")
    
    # Add to sys.path
    paths_to_add = [str(project_root), str(src_dir), str(config_dir)]
    
    print("\nAdding to sys.path:")
    for path in paths_to_add:
        if path not in sys.path:
            sys.path.insert(0, path)
            print(f"  Added: {path}")
        else:
            print(f"  Already in path: {path}")
    
    return project_root, src_dir, config_dir

def check_file_structure(project_root):
    """Check if all required files exist"""
    print("\n📁 Checking file structure...")
    
    required_files = [
        "src/travel_bot/__init__.py",
        "src/travel_bot/travel_bot.py", 
        "src/travel_bot/models/__init__.py",
        "src/travel_bot/models/ai_models.py",
        "config/settings.py",
        ".env"
    ]
    
    all_exist = True
    for file_path in required_files:
        full_path = project_root / file_path
        if full_path.exists():
            print(f"  ✅ {file_path}")
        else:
            print(f"  ❌ {file_path} - MISSING")
            all_exist = False
    
    return all_exist

def test_individual_imports():
    """Test each import individually"""
    print("\n🧪 Testing individual imports...")
    
    results = {}
    
    # Test basic modules first
    test_cases = [
        ("os", None),
        ("sys", None),
        ("pathlib", "Path"),
        ("travel_bot", None),
        ("travel_bot.models", None),
        ("travel_bot.models", "InputType"),
        ("travel_bot.models", "TravelPreferences"),
        ("travel_bot.travel_bot", "TravelBot"),
        ("config", None),
        ("config.settings", "Config"),
    ]
    
    for module_name, class_name in test_cases:
        test_name = f"{module_name}" + (f".{class_name}" if class_name else "")
        try:
            if class_name:
                module = __import__(module_name, fromlist=[class_name])
                getattr(module, class_name)
            else:
                __import__(module_name)
            
            print(f"  ✅ {test_name}")
            results[test_name] = True
            
        except Exception as e:
            print(f"  ❌ {test_name}: {str(e)}")
            results[test_name] = False
            # Print detailed error for critical imports
            if module_name.startswith('travel_bot') or module_name.startswith('config'):
                print(f"     Error details: {traceback.format_exc()}")
    
    return results

def test_streamlit_import():
    """Test if Streamlit can be imported"""
    print("\n🌐 Testing Streamlit...")
    try:
        import streamlit as st
        print("  ✅ Streamlit imported successfully")
        return True
    except ImportError as e:
        print(f"  ❌ Streamlit import failed: {e}")
        return False

def main():
    """Main test function"""
    print("🚀 Travel Advisory Bot - Import Diagnostics")
    print("=" * 60)
    
    # Setup paths
    project_root, src_dir, config_dir = setup_paths()
    
    # Check file structure
    files_ok = check_file_structure(project_root)
    
    # Test imports
    import_results = test_individual_imports()
    
    # Test Streamlit
    streamlit_ok = test_streamlit_import()
    
    # Summary
    print("\n📊 SUMMARY")
    print("=" * 60)
    
    print(f"File structure: {'✅ OK' if files_ok else '❌ ISSUES'}")
    print(f"Streamlit: {'✅ OK' if streamlit_ok else '❌ ISSUES'}")
    
    successful_imports = sum(1 for v in import_results.values() if v)
    total_imports = len(import_results)
    print(f"Imports: {successful_imports}/{total_imports} successful")
    
    if successful_imports == total_imports and files_ok and streamlit_ok:
        print("\n🎉 ALL TESTS PASSED!")
        print("The Streamlit app should work. Try running:")
        print("  python streamlit_launcher.py")
    else:
        print("\n❌ ISSUES FOUND:")
        
        if not files_ok:
            print("  - Missing required files")
        
        if not streamlit_ok:
            print("  - Streamlit not available")
            
        failed_imports = [k for k, v in import_results.items() if not v]
        if failed_imports:
            print("  - Failed imports:")
            for failed in failed_imports:
                print(f"    * {failed}")

if __name__ == "__main__":
    main()
