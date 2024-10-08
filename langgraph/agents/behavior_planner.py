"""
Agent that processes information from the prefrontal cortex and plans behavior.
"""

from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from .src.utils import clean_json
from .models.brain import BehaviorPlanner
from .prompts.behavior_planner import BEHAVIOR_PLANNER
from .config.models import model

# Inicializa o parser para o objeto PrefrontalCortex
parser = PydanticOutputParser(pydantic_object=BehaviorPlanner)

def behavior_planner_agent(state):
    """
    This function is responsible for generating a behavior plan for the agent.
    
    Args:
        state (dict): Dictionary with information about the current state of the agent

    Returns:
        dict: Dictionary with information about the generated behavior plan
    """
    prompt = PromptTemplate(
        template = BEHAVIOR_PLANNER,
        input_variables=["messages"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )
    chain = prompt | model
    response = chain.invoke({"messages": state["messages"], "expected_action": state["behavior_planner"]})

    result_dict = clean_json(response)

    return {
        "actual_behavior": result_dict["actual_behavior"], 
        "alternative_behavior": result_dict["alternative_behavior"], 
        "control_mechanisms": result_dict["control_mechanisms"], 
        "contingency_plans": result_dict["contingency_plans"]
    }
