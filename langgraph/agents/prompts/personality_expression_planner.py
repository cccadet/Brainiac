"""
This module contains the prompts for the Personality Expression Planner agent.
"""

PERSONALITY_EXPRESSION_PLANNER = """
    Interaction: {messages}
    Expected action: {expected_action}

    The goal of the Personality Express Planner is to create and maintain a personality 
    expression that resonates with users and aligns with the system’s values ​​and 
    goals. This involves adapting the personality across different situations and 
    interactions to ensure effective communication and a consistent presence.

    {format_instructions}
"""
