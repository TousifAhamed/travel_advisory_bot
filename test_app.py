#!/usr/bin/env python3
"""
Simplified test application for Travel Advisory Bot
Tests core functionality without heavy dependencies
"""

import sys
import os
import asyncio
import json

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

class SimplifiedTravelBot:
    """Simplified version for testing without external API dependencies"""
    
    def __init__(self):
        self.model_type = "mock"
    
    async def chat_with_bot(self, message: str) -> str:
        """Simple mock chat response"""
        message_lower = message.lower()
        
        if any(word in message_lower for word in ["paris", "france"]):
            return """Paris is a wonderful destination! Here are some suggestions:
            
🗼 **Top Attractions:**
• Eiffel Tower - Iconic landmark with amazing views
• Louvre Museum - World's largest art museum
• Notre-Dame Cathedral - Gothic architecture masterpiece
• Champs-Élysées - Famous shopping street

🍽️ **Food & Dining:**
• Try authentic French pastries at local bakeries
• Visit traditional bistros for classic French cuisine
• Don't miss the wine tasting experiences

💰 **Budget Tips:**
• Visit museums on first Sunday mornings (often free)
• Use the metro for affordable transportation
• Picnic in parks like Luxembourg Gardens

✈️ **Best Time to Visit:**
April-June and September-October for pleasant weather and fewer crowds."""

        elif any(word in message_lower for word in ["japan", "tokyo"]):
            return """Japan offers an incredible mix of tradition and modernity!

🏯 **Cultural Highlights:**
• Visit ancient temples in Kyoto
• Experience traditional ryokan accommodations
• Witness cherry blossoms (March-May)
• Try authentic tea ceremonies

🍜 **Food Adventures:**
• Authentic sushi and sashimi
• Ramen shops on every corner
• Traditional kaiseki dining
• Street food in Tokyo markets

🚄 **Transportation:**
• JR Pass for unlimited train travel
• Efficient and clean public transport
• Bullet trains (shinkansen) between cities

📱 **Travel Tips:**
• Download translation apps
• Cash is still king in many places
• Bow as a greeting (don't shake hands)
• Remove shoes when entering homes"""

        elif any(word in message_lower for word in ["beach", "tropical", "island"]):
            return """Tropical paradise destinations await! 🏝️

🌴 **Top Beach Destinations:**
• Maldives - Luxury resorts and crystal waters
• Bali, Indonesia - Perfect blend of culture and beaches
• Santorini, Greece - Stunning sunsets and white buildings
• Hawaii, USA - Diverse islands with unique experiences

🏖️ **Beach Activities:**
• Snorkeling and diving
• Water sports (surfing, kayaking)
• Beach volleyball and relaxation
• Sunset cruises

☀️ **Packing Essentials:**
• Sunscreen (high SPF)
• Swimwear and cover-ups
• Waterproof phone case
• Light, breathable clothing"""

        elif any(word in message_lower for word in ["budget", "cheap", "affordable"]):
            return """Budget travel tips for amazing adventures! 💰

🏠 **Accommodation:**
• Hostels and guesthouses
• Airbnb shared rooms
• Couchsurfing
• House-sitting opportunities

🚗 **Transportation:**
• Public transport over taxis
• Walk or bike when possible
• Bus travel for longer distances
• Flight comparison websites

🍕 **Food & Dining:**
• Local markets and street food
• Cook your own meals
• Lunch specials instead of dinner
• Happy hour drinks

🎯 **Free Activities:**
• Walking tours (tip-based)
• Museums with free days
• Parks and hiking trails
• Beaches and public spaces"""

        else:
            return f"""I'd be happy to help with your travel plans! 

You asked: "{message}"

🌍 **I can help you with:**
• Destination recommendations
• Itinerary planning
• Budget travel tips
• Cultural information
• Food and dining suggestions
• Transportation options

Try asking me about:
• Specific destinations (e.g., "Tell me about Paris")
• Travel styles (e.g., "Budget travel tips")
• Activities (e.g., "Beach destinations")
• Cultural experiences

What specific aspect of travel planning interests you most?"""

    async def get_travel_suggestions(self, text: str) -> list:
        """Generate mock travel suggestions"""
        suggestions = [
            {
                "destination": "Paris, France",
                "description": "The City of Light offers world-class museums, iconic landmarks, and incredible cuisine.",
                "best_time": "April-June, September-October",
                "budget": "$100-200/day",
                "duration": "4-7 days",
                "highlights": ["Eiffel Tower", "Louvre Museum", "Seine River Cruise"]
            },
            {
                "destination": "Tokyo, Japan", 
                "description": "A fascinating blend of ultra-modern and traditional culture with amazing food.",
                "best_time": "March-May, September-November",
                "budget": "$80-150/day",
                "duration": "5-10 days",
                "highlights": ["Senso-ji Temple", "Shibuya Crossing", "Cherry Blossoms"]
            },
            {
                "destination": "Santorini, Greece",
                "description": "Stunning sunsets, white-washed buildings, and beautiful Mediterranean beaches.",
                "best_time": "April-October",
                "budget": "$70-120/day", 
                "duration": "3-5 days",
                "highlights": ["Oia Sunset", "Red Beach", "Wine Tasting"]
            }
        ]
        
        return suggestions

def demo_chat():
    """Interactive chat demo"""
    print("🤖 AI Travel Advisory Bot - Demo Mode")
    print("=" * 50)
    print("Type 'quit' to exit\n")
    
    bot = SimplifiedTravelBot()
    
    while True:
        user_input = input("💬 You: ")
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("👋 Thanks for using Travel Advisory Bot!")
            break
        
        print("\n🤖 Bot: ", end="")
        response = asyncio.run(bot.chat_with_bot(user_input))
        print(response)
        print("\n" + "-" * 50 + "\n")

def demo_suggestions():
    """Demo travel suggestions"""
    print("🎯 Travel Suggestions Demo")
    print("=" * 30)
    
    bot = SimplifiedTravelBot()
    suggestions = asyncio.run(bot.get_travel_suggestions("I want a romantic vacation"))
    
    for i, suggestion in enumerate(suggestions, 1):
        print(f"\n📍 Option {i}: {suggestion['destination']}")
        print(f"   Description: {suggestion['description']}")
        print(f"   Best Time: {suggestion['best_time']}")
        print(f"   Budget: {suggestion['budget']}")
        print(f"   Duration: {suggestion['duration']}")
        print(f"   Highlights: {', '.join(suggestion['highlights'])}")

def main():
    """Main demo function"""
    print("🌍 Welcome to AI Travel Advisory Bot Demo!")
    print("=" * 50)
    
    while True:
        print("\nWhat would you like to try?")
        print("1. Chat with the bot")
        print("2. Get travel suggestions")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            demo_chat()
        elif choice == "2":
            demo_suggestions()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()