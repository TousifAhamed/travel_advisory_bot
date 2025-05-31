from typing import Dict, List, Optional
from ..models import TravelSuggestion, Itinerary

class TravelUtils:
    """Utility functions for travel-related operations"""
    
    @staticmethod
    def create_destination_map(suggestions: List[TravelSuggestion]):
        """Create destination map data (fallback without folium)"""
        destinations = []
        for suggestion in suggestions:
            destinations.append({
                "destination": suggestion.destination,
                "description": suggestion.description,
                "best_time": suggestion.best_time_to_visit,
                "budget": suggestion.estimated_budget
            })
        return {"destinations": destinations, "map_available": False}
    
    @staticmethod
    def create_budget_chart(itinerary: Itinerary) -> dict:
        """Create budget breakdown chart data"""
        if not itinerary.daily_plans:
            return {"error": "No daily plans available"}
        
        daily_costs = []
        total_cost = 0
        
        for plan in itinerary.daily_plans:
            cost_str = plan.get("estimated_cost", "50")
            try:
                cost = float(cost_str.replace("$", "").replace("USD", "").split("-")[0])
            except:
                cost = 50.0
            
            daily_costs.append({
                "Day": f"Day {plan.get('day', 1)}",
                "Cost": cost
            })
            total_cost += cost
        
        return {
            "daily_costs": daily_costs,
            "total_cost": total_cost
        }
    
    @staticmethod
    def format_itinerary_for_display(itinerary: Itinerary) -> Dict:
        """Format itinerary for better display"""
        formatted_daily_plans = []
        
        for plan in itinerary.daily_plans:
            formatted_plan = {
                "day": plan.get("day", 1),
                "date": plan.get("date", f"Day {plan.get('day', 1)}"),
                "schedule": {
                    "Morning": plan.get("morning", "Free time"),
                    "Afternoon": plan.get("afternoon", "Free time"),
                    "Evening": plan.get("evening", "Free time")
                },
                "meals": plan.get("meals", []),
                "estimated_cost": plan.get("estimated_cost", "Not specified")
            }
            formatted_daily_plans.append(formatted_plan)
        
        return {
            "destination": itinerary.destination,
            "duration": f"{itinerary.total_days} days",
            "budget": itinerary.total_budget or "Not specified",
            "daily_plans": formatted_daily_plans,
            "accommodation": itinerary.accommodation_details,
            "transportation": itinerary.transportation_details,
            "packing_list": itinerary.packing_list,
            "emergency_contacts": itinerary.emergency_contacts,
            "important_notes": itinerary.important_notes
        }
    
    @staticmethod
    def get_travel_tips_by_region(destination: str) -> List[str]:
        """Get region-specific travel tips"""
        regional_tips = {
            "europe": [
                "Check visa requirements for Schengen area",
                "Public transport is excellent in most cities",
                "Tipping is not mandatory but appreciated",
                "Many places close on Sundays"
            ],
            "asia": [
                "Respect local customs and dress codes",
                "Street food is generally safe and delicious",
                "Remove shoes when entering homes or temples",
                "Bargaining is common in markets"
            ],
            "americas": [
                "Tipping is expected in restaurants (15-20%)",
                "Distances can be vast - plan accordingly",
                "Check vaccination requirements",
                "Emergency services: 911"
            ]
        }
        
        destination_lower = destination.lower()
        
        if any(country in destination_lower for country in ["france", "italy", "spain", "germany", "uk"]):
            return regional_tips["europe"]
        elif any(country in destination_lower for country in ["japan", "china", "thailand", "india", "korea"]):
            return regional_tips["asia"]
        elif any(country in destination_lower for country in ["usa", "canada", "brazil", "mexico"]):
            return regional_tips["americas"]
        
        return [
            "Research local customs and etiquette",
            "Keep copies of important documents",
            "Check weather conditions before departure",
            "Learn basic phrases in local language"
        ]
    
    @staticmethod
    def validate_travel_preferences(preferences: dict) -> Dict[str, bool]:
        """Validate travel preferences input"""
        validation_results = {
            "budget_valid": True,
            "dates_valid": True,
            "group_size_valid": True,
            "preferences_complete": True
        }
        
        group_size = preferences.get("group_size", 1)
        if not isinstance(group_size, int) or group_size < 1 or group_size > 20:
            validation_results["group_size_valid"] = False
        
        required_fields = ["budget_range", "travel_style", "interests"]
        missing_fields = [field for field in required_fields if not preferences.get(field)]
        if missing_fields:
            validation_results["preferences_complete"] = False
            validation_results["missing_fields"] = missing_fields
        
        return validation_results
    
    @staticmethod
    def get_travel_style_descriptions() -> Dict[str, str]:
        """Get descriptions for different travel styles"""
        return {
            "adventure": "Thrilling activities, outdoor experiences, and off-the-beaten-path destinations",
            "cultural": "Museums, historical sites, local traditions, and authentic experiences",
            "relaxation": "Beaches, spas, resorts, and peaceful environments",
            "business": "Professional accommodations, meeting facilities, and efficient transportation",
            "budget": "Cost-effective options, hostels, local transport, and free activities",
            "luxury": "High-end accommodations, fine dining, and premium experiences",
            "family": "Kid-friendly activities, safe environments, and family accommodations",
            "romantic": "Intimate settings, couples activities, and romantic dining"
        }
