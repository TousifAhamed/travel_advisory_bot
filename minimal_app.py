#!/usr/bin/env python3
"""
Minimal Travel Advisory Bot Streamlit App
This is a simplified version that focuses on getting the core functionality working
"""

import streamlit as st
import os
import sys
from pathlib import Path
import traceback

# Setup paths
def setup_paths():
    current_dir = Path(__file__).parent.absolute()
    project_root = current_dir
    src_dir = project_root / "src"
    config_dir = project_root / "config"
    
    # Add to Python path
    for path in [str(project_root), str(src_dir), str(config_dir)]:
        if path not in sys.path:
            sys.path.insert(0, path)

setup_paths()

# Try to import core components
try:
    from travel_bot.travel_bot import TravelBot
    from travel_bot.models import InputType, TravelPreferences
    from config.settings import Config
    IMPORTS_OK = True
    IMPORT_ERROR = None
except Exception as e:
    IMPORTS_OK = False
    IMPORT_ERROR = str(e)

def main():
    """Main Streamlit application"""
    st.set_page_config(
        page_title="🌍 AI Travel Advisory Bot",
        page_icon="✈️",
        layout="wide"
    )
    
    st.title("🌍 AI Travel Advisory Bot")
    st.markdown("*Powered by Devstral - Your Intelligent Travel Assistant*")
    
    # Check if imports are working
    if not IMPORTS_OK:
        st.error("❌ **Import Error Detected**")
        st.error(f"Error: {IMPORT_ERROR}")
        st.markdown("**Troubleshooting Steps:**")
        st.markdown("1. Run `complete_setup.bat` to install dependencies")
        st.markdown("2. Ensure virtual environment is activated")
        st.markdown("3. Check that all files are in place")
        
        with st.expander("🔧 Debug Information"):
            st.code(f"Python Path: {sys.path[:5]}")
            st.code(f"Current Working Directory: {os.getcwd()}")
            st.code(f"Import Error Details:\n{traceback.format_exc()}")
        return
    
    st.success("✅ **All imports successful!**")
    
    # Initialize session state
    if 'travel_bot' not in st.session_state:
        st.session_state.travel_bot = None
        st.session_state.conversation_history = []
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("🛠️ Configuration")
        
        # Model selection
        model_type = st.selectbox(
            "AI Model",
            ["ollama", "openai", "huggingface"],
            index=0,
            help="Select the AI model to use. Ollama with Devstral is recommended for local processing."
        )
        
        if st.button("🔄 Initialize Bot"):
            try:
                with st.spinner("Initializing Travel Bot..."):
                    st.session_state.travel_bot = TravelBot(model_type)
                st.success(f"✅ Travel Bot initialized with {model_type}")
            except Exception as e:
                st.error(f"❌ Failed to initialize: {str(e)}")
    
    # Main content tabs
    tab1, tab2, tab3 = st.tabs(["💬 Chat", "🗺️ Travel Suggestions", "📋 Itinerary Planning"])
    
    with tab1:
        st.header("💬 Travel Chat")
        
        if st.session_state.travel_bot is None:
            st.info("👈 Please initialize the Travel Bot in the sidebar first.")
        else:
            # Chat input
            user_input = st.text_input("Ask me anything about travel:", placeholder="Where should I visit in Japan?")
            
            if st.button("Send") and user_input:
                with st.spinner("Thinking..."):
                    try:
                        # For now, just echo the input with a simple response
                        response = f"Thank you for asking about: {user_input}. The Travel Bot is working! (This is a test response while we verify the full integration.)"
                        
                        # Add to conversation history
                        st.session_state.conversation_history.append({
                            "user": user_input,
                            "bot": response
                        })
                        
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            
            # Display conversation history
            for conv in reversed(st.session_state.conversation_history[-5:]):  # Show last 5
                st.markdown(f"**You:** {conv['user']}")
                st.markdown(f"**🤖 Travel Bot:** {conv['bot']}")
                st.divider()
    
    with tab2:
        st.header("🗺️ Travel Suggestions")
        
        if st.session_state.travel_bot is None:
            st.info("👈 Please initialize the Travel Bot in the sidebar first.")
        else:
            st.markdown("**Tell us about your travel preferences:**")
            
            col1, col2 = st.columns(2)
            
            with col1:
                destination = st.text_input("Destination (optional):", placeholder="e.g., Europe, Asia, Tropical")
                budget = st.selectbox("Budget Range:", ["Low ($)", "Medium ($$)", "High ($$$)", "Luxury ($$$$)"])
                travel_style = st.selectbox("Travel Style:", ["Adventure", "Cultural", "Relaxation", "Business", "Family"])
            
            with col2:
                duration = st.selectbox("Trip Duration:", ["Weekend (2-3 days)", "Week (4-7 days)", "Extended (1-2 weeks)", "Long-term (1+ months)"])
                season = st.selectbox("Preferred Season:", ["Spring", "Summer", "Fall", "Winter", "Flexible"])
                interests = st.multiselect("Interests:", ["Food", "History", "Nature", "Adventure", "Culture", "Nightlife", "Shopping", "Photography"])
            
            if st.button("🔍 Get Suggestions"):
                with st.spinner("Generating personalized travel suggestions..."):
                    # Placeholder for actual suggestion generation
                    st.success("✨ **Travel Suggestions Generated!**")
                    st.markdown("*Note: Full integration with Devstral AI in progress. This demonstrates the interface.*")
                    
                    # Mock suggestions for demonstration
                    suggestions = [
                        f"🌟 **Destination 1:** Perfect for {travel_style.lower()} travel in {season.lower()}",
                        f"🌟 **Destination 2:** Great {budget.lower()} options for {duration.lower()}",
                        f"🌟 **Destination 3:** Ideal for {', '.join(interests[:2]) if interests else 'your interests'}"
                    ]
                    
                    for suggestion in suggestions:
                        st.markdown(suggestion)
    
    with tab3:
        st.header("📋 Itinerary Planning")
        
        if st.session_state.travel_bot is None:
            st.info("👈 Please initialize the Travel Bot in the sidebar first.")
        else:
            st.markdown("**Create a detailed travel itinerary:**")
            
            # Itinerary inputs
            itinerary_destination = st.text_input("Destination:", placeholder="e.g., Tokyo, Japan")
            itinerary_days = st.number_input("Number of Days:", min_value=1, max_value=30, value=7)
            
            col1, col2 = st.columns(2)
            with col1:
                arrival_date = st.date_input("Arrival Date")
                accommodation = st.selectbox("Accommodation Type:", ["Hotel", "Hostel", "Airbnb", "Resort", "Guesthouse"])
            
            with col2:
                departure_date = st.date_input("Departure Date")
                transportation = st.selectbox("Primary Transportation:", ["Walking", "Public Transit", "Rental Car", "Taxi/Uber", "Tours"])
            
            if st.button("📋 Generate Itinerary"):
                with st.spinner("Creating your personalized itinerary..."):
                    st.success("📋 **Itinerary Created!**")
                    st.markdown("*Note: Full AI-powered itinerary generation with Devstral coming soon.*")
                    
                    # Mock itinerary for demonstration
                    st.markdown(f"## {itinerary_days}-Day Itinerary for {itinerary_destination}")
                    
                    for day in range(1, min(itinerary_days + 1, 4)):  # Show first 3 days
                        st.markdown(f"### Day {day}")
                        st.markdown(f"- **Morning:** Explore local attractions")
                        st.markdown(f"- **Afternoon:** {accommodation} check-in and local dining")
                        st.markdown(f"- **Evening:** Cultural activities via {transportation.lower()}")
                        st.divider()
    
    # Footer
    st.markdown("---")
    st.markdown("*🤖 Powered by Devstral AI | 🛠️ Built with Streamlit*")

if __name__ == "__main__":
    main()
