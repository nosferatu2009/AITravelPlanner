from AITravelPlanner.prompts import SYSTEM_PROMPT
from AITravelPlanner.mcp_context import build_travel_context

def travel_agent(llm, trip):
    context = build_travel_context(trip)

    prompt = f"""
    {SYSTEM_PROMPT}

    Context:
    {context}

    Task:
    Create a day-wise travel plan with a budget breakdown
    and practical travel tips.
    """

    response = llm(prompt)
    return response