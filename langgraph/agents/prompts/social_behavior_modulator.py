"""
This module contains the prompt for the Social Behavior Modulator agent.
"""

SOCIAL_BEHAVIOR_MODULATOR = """
    Interaction: {messages}
    Expected action: {expected_action}

    The goal of the Social Behavior Modulator is to optimize the system’s social 
    interactions, ensuring that behavior is appropriate, respectful, and effective 
    in a variety of contexts. This involves adapting behavior to the needs and 
    expectations of users, as well as managing system responses to maintain 
    healthy and productive social relationships.

    Your output must be in following format: 

    {format_instructions}
"""
