from AITravelPlanner.agent import travel_agent
from AITravelPlanner.llm import llm

def ask_text(question):
    return input(f"{question}\n👉 ").strip()

def ask_list(question):
    return [
        item.strip()
        for item in input(f"{question}\n👉 ").split(",")
        if item.strip()
    ]

def ask_choice(question, choices):
    print(question)
    for idx, choice in enumerate(choices, 1):
        print(f"{idx}. {choice}")

    while True:
        try:
            selection = int(input("👉 "))
            if 1 <= selection <= len(choices):
                return choices[selection - 1]
        except ValueError:
            pass
        print("Please select a valid option.")

def collect_trip_details():
    print("\n🌍 Welcome to AI Travel Planner\n")

    destination = ask_text("Where do you want to travel?")
    days = ask_text("How many days is your trip?")
    budget = ask_text("What is your total budget (INR)?")
    preferences = ask_list("What are your interests? (comma separated)")
    pace = ask_choice(
        "What travel pace do you prefer?",
        ["Slow", "Moderate", "Fast"]
    )

    return {
        "destination": destination,
        "days": days,
        "budget": budget,
        "preferences": preferences,
        "pace": pace
    }

if __name__ == "__main__":
    trip_details = collect_trip_details()

    print("\n🧠 Generating your travel plan...\n")
    result = travel_agent(llm, trip_details)

    print("📌 Your Travel Plan:\n")
    print(result)
