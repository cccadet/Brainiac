"""
Agent for the personality expression planner.
"""

from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from .src.utils import clean_json
from .config.models import model
from .models.brain import PersonalityExpressionPlanner
from .prompts.personality_expression_planner import PERSONALITY_EXPRESSION_PLANNER

parser = PydanticOutputParser(pydantic_object=PersonalityExpressionPlanner)

def personality_expression_planner_agent(state):
    """
    This function processes the input messages and assigns tasks to the
    personality expression planner.

    Args:
        state (dict): Dictionary with information about the current state of the agent

    Returns:
        dict: Dictionary with information about the personality expression plan
    """
    prompt = PromptTemplate(
        template = PERSONALITY_EXPRESSION_PLANNER,
        input_variables=["messages"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )
    chain = prompt | model
    response = chain.invoke({"messages": state["messages"], "expected_action": state["personality_expression_planner"]})

    result_dict = clean_json(response)

    return {
        "personality": result_dict["personality"],
        "guidelines_personality": result_dict["guidelines_personality"],
        "examples_personality": result_dict["examples_personality"],
        "personality_estrategy": result_dict["personality_estrategy"],
        "personality_consistency": result_dict["personality_consistency"]
    }
