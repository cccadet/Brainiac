"""
Agent to make decisions based on the current state of the environment.
"""

from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from .src.utils import clean_json
from .config.models import model
from .prompts.decision_maker import DECISION_MAKER
from .models.brain import DecisionMaker


parser = PydanticOutputParser(pydantic_object=DecisionMaker)

def decision_maker_agent(state):
    """
    This function takes in the current state of the environment and returns the 
    decision made by the agent.

    Args:
        state (dict): The current state of the environment
    
    Returns:
        dict: The decision made by the agent
    """
    prompt = PromptTemplate(
        template = DECISION_MAKER,
        input_variables=["messages"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )
    chain = prompt | model
    response = chain.invoke({"messages": state["messages"], "expected_action": state["decision_maker"]})

    result_dict = clean_json(response)

    return {
        "available_decisions": result_dict["available_decisions"],
        "implications": result_dict["implications"],
        "optimal_decision": result_dict["optimal_decision"],
        "decision_strategy": result_dict["decision_strategy"],
        "decision_consistency": result_dict["decision_consistency"]
    }
