#!/usr/bin/env python3
"""
Debug Streamlit App for Travel Advisory Bot
This version includes extensive debugging and path resolution
"""

import streamlit as st
import os
import sys
from pathlib import Path
import traceback

def setup_paths():
    """Setup Python paths with debugging"""
    st.write("🔧 **Python Path Setup Debug**")
    
    current_file = Path(__file__).absolute()
    st.write(f"Current file: `{current_file}`")
    
    # Calculate paths
    project_root = current_file.parent.parent.parent.parent
    src_dir = project_root / "src"
    config_dir = project_root / "config"
    
    st.write(f"Project root: `{project_root}`")
    st.write(f"Src directory: `{src_dir}`")
    st.write(f"Config directory: `{config_dir}`")
    
    # Add to sys.path
    paths_to_add = [str(project_root), str(src_dir), str(config_dir)]
    
    for path in paths_to_add:
        if path not in sys.path:
            sys.path.insert(0, path)
    
    st.write("**Current sys.path:**")
    for i, path in enumerate(sys.path[:10]):  # Show first 10 paths
        st.write(f"{i}: `{path}`")
    
    return project_root, src_dir, config_dir

def test_imports():
    """Test imports with detailed error reporting"""
    st.write("🧪 **Import Testing**")
    
    imports_to_test = [
        ("travel_bot.travel_bot", "TravelBot"),
        ("travel_bot.models", "InputType"),
        ("travel_bot.models", "TravelPreferences"), 
        ("config.settings", "Config"),
    ]
    
    results = {}
    
    for module_name, class_name in imports_to_test:
        try:
            module = __import__(module_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            st.success(f"✅ {module_name}.{class_name}")
            results[f"{module_name}.{class_name}"] = True
        except Exception as e:
            st.error(f"❌ {module_name}.{class_name}: {str(e)}")
            results[f"{module_name}.{class_name}"] = False
            with st.expander(f"Error details for {module_name}.{class_name}"):
                st.code(traceback.format_exc())
    
    return results

def check_dependencies():
    """Check system dependencies"""
    st.write("📦 **Dependency Check**")
    
    deps_to_check = [
        "streamlit",
        "ollama", 
        "PyPDF2",
        "Pillow",
        "openai",
        "python-dotenv"
    ]
    
    for dep in deps_to_check:
        try:
            __import__(dep)
            st.success(f"✅ {dep}")
        except ImportError:
            st.error(f"❌ {dep} - Not installed")

def show_file_structure():
    """Show relevant file structure"""
    st.write("📁 **Project Structure Check**")
    
    current_file = Path(__file__).absolute()
    project_root = current_file.parent.parent.parent.parent
    
    important_files = [
        project_root / "src" / "travel_bot" / "__init__.py",
        project_root / "src" / "travel_bot" / "travel_bot.py",
        project_root / "src" / "travel_bot" / "models" / "__init__.py",
        project_root / "config" / "settings.py",
        project_root / ".env",
    ]
    
    for file_path in important_files:
        if file_path.exists():
            st.success(f"✅ {file_path.relative_to(project_root)}")
        else:
            st.error(f"❌ {file_path.relative_to(project_root)} - Missing")

def main():
    """Main debug application"""
    st.title("🔍 Travel Advisory Bot - Debug Mode")
    st.write("This debug version helps identify import and setup issues.")
    
    # Setup paths
    project_root, src_dir, config_dir = setup_paths()
    
    st.divider()
    
    # Check file structure
    show_file_structure()
    
    st.divider()
    
    # Check dependencies
    check_dependencies()
    
    st.divider()
    
    # Test imports
    import_results = test_imports()
    
    st.divider()
    
    # Summary
    st.write("📊 **Summary**")
    
    all_imports_successful = all(import_results.values())
    
    if all_imports_successful:
        st.success("🎉 All imports successful! The main app should work.")
        
        if st.button("🚀 Launch Main App"):
            st.write("Redirecting to main app...")
            # Import and run main app
            try:
                from travel_bot.travel_bot import TravelBot
                from travel_bot.models import InputType, TravelPreferences
                from config.settings import Config
                
                st.success("✅ Successfully imported all components!")
                st.write("The main Streamlit app should now work properly.")
                st.write("You can now run: `python streamlit_launcher.py`")
                
            except Exception as e:
                st.error(f"❌ Still having issues: {e}")
                st.code(traceback.format_exc())
    else:
        st.error("❌ Some imports failed. Please fix the issues above.")
        
        failed_imports = [k for k, v in import_results.items() if not v]
        st.write("**Failed imports:**")
        for failed in failed_imports:
            st.write(f"- {failed}")

if __name__ == "__main__":
    main()
