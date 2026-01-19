def build_travel_context(trip):
    return {
        "role": "Travel Planner AI Agent",
        "destination": trip["destination"],
        "days": trip["days"],
        "budget": trip["budget"],
        "preferences": trip["preferences"],
        "planning_rules": [
            "Create a relaxed, realistic itinerary",
            "Do not exceed total budget",
            "Balance sightseeing and rest",
            "Avoid too many places in one day"
        ],
        "output_format": {
            "day_wise_plan": True,
            "budget_breakdown": True,
            "travel_tips": True
        }
    }