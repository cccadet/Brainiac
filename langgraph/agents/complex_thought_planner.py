"""
Agent that processes complex thought from the prefrontal cortex.
"""

from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from .src.utils import clean_json
from .config.models import model
from .models.brain import ComplexThoughtPlanner
from .prompts.complex_thought_planner import COMPLEX_TOUGHT_PLANNER

parser = PydanticOutputParser(pydantic_object=ComplexThoughtPlanner)

def complex_thought_planner_agent(state):
    """
    This function processes the input messages and assigns tasks to the 
    complex thinking planner.
    
    Args:
        state (dict): Dictionary with information about the current state of the agent
        
    Returns:
        dict: Dictionary with information about the generated behavior plan
    """
    prompt = PromptTemplate(
        template = COMPLEX_TOUGHT_PLANNER,
        input_variables=["messages"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )
    chain = prompt | model
    response = chain.invoke({"messages": state["messages"], "expected_action": state["complex_thought_planner"]})

    result_dict = clean_json(response)

    return {
        "detailed_analysis": result_dict["detailed_analysis"],
        "standard_relations": result_dict["standard_relations"],
        "insights": result_dict["insights"], 
        "implications_scenarios": result_dict["implications_scenarios"],
        "comprehensive_understanding": result_dict["comprehensive_understanding"]
    }