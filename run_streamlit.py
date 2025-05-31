#!/usr/bin/env python3
"""
Streamlit launcher with proper path configuration
"""
import os
import sys

# Get the project root directory
project_root = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(project_root, 'src')

# Add both project root and src to Python path
sys.path.insert(0, project_root)
sys.path.insert(0, src_dir)

# Now import and run Streamlit
if __name__ == "__main__":
    import streamlit as st
    from streamlit.web import cli as stcli
    
    # Set the path to the Streamlit app
    streamlit_app_path = os.path.join('src', 'travel_bot', 'ui', 'streamlit_app.py')
    
    # Configure Streamlit to run our app
    sys.argv = [
        "streamlit",
        "run",
        streamlit_app_path,
        "--server.port=8501",
        "--server.headless=false"
    ]
    
    # Run Streamlit
    stcli.main()
