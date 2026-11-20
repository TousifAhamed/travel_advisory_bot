#!/usr/bin/env python3
"""
Main entry point for the Travel Advisory Bot application
"""

import subprocess
import sys
import os
import asyncio

# Add the src directory to the Python path
project_root = os.path.dirname(__file__)
src_dir = os.path.join(project_root, 'src')
sys.path.insert(0, project_root)
sys.path.insert(0, src_dir)

from travel_bot import TravelBot, InputType, TravelPreferences

def run_streamlit():
    """Run the Streamlit web interface"""
    try:
        import streamlit as st
        subprocess.run([sys.executable, "-m", "streamlit", "run", os.path.join(os.path.dirname(__file__), 'src', 'travel_bot', 'ui', 'streamlit_app.py')])
    except ImportError:
        print("Streamlit not installed. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "streamlit"], check=True)
        subprocess.run([sys.executable, "-m", "streamlit", "run", os.path.join(os.path.dirname(__file__), 'src', 'travel_bot', 'ui', 'streamlit_app.py')])

def run_console_demo():
    """Run a simple console demo"""
    print("🌍 Welcome to AI Travel Advisory Bot!")
    print("=" * 50)
    
    # Initialize bot
    try:
        bot = TravelBot(model_type="ollama")  # Use Ollama as default fallback
        print("✅ Travel Bot initialized successfully!")
    except Exception as e:
        print(f"❌ Failed to initialize bot: {e}")
        return
    
    # Demo conversation
    while True:
        user_input = input("\n💬 Ask me about travel (or 'quit' to exit): ")
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("👋 Thanks for using Travel Advisory Bot!")
            break
        
        try:
            # Simple text processing
            response = asyncio.run(bot.chat_with_bot(user_input))
            print(f"\n🤖 Bot: {response}")
            
        except Exception as e:
            print(f"❌ Error: {e}")

def main():
    """Main entry point"""
    print("🚀 Starting Travel Advisory Bot...")
    
    if len(sys.argv) > 1 and sys.argv[1] == "--console":
        run_console_demo()
    else:
        print("🌐 Starting web interface...")
        run_streamlit()

if __name__ == "__main__":
    main()
