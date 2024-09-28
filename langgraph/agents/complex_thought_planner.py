"""
This snippet is a part of the agent that processes the Complex Thought Planner prompt.
"""

from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from .src.utils import clean_json
from .config.models import model
from .models.brain import ComplexThoughtPlanner
from .prompts.complex_thought_planner import COMPLEX_TOUGHT_PLANNER

parser = PydanticOutputParser(pydantic_object=ComplexThoughtPlanner)

def complex_thought_planner_agent(state):
    """Esta função processa as mensagens de entrada e atribui tarefas ao planejador de pensamento complexo."""
    prompt = PromptTemplate(
        template = COMPLEX_TOUGHT_PLANNER,
        input_variables=["messages"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )
    chain = prompt | model
    response = chain.invoke({"messages": state["messages"], "expected_action": state["complex_thought_planner"]})

    result_dict = clean_json(response)

    state["detailed_analysis"] = result_dict["detailed_analysis"]
    state["standard_relations"] = result_dict["standard_relations"]
    state["insights"] = result_dict["insights"]
    state["implications_scenarios"] = result_dict["implications_scenarios"]
    state["comprehensive_understanding"] = result_dict["comprehensive_understanding"]

    return {"detailed_analysis": state["detailed_analysis"], "standard_relations": state["standard_relations"], "insights": state["insights"], "implications_scenarios": state["implications_scenarios"], "comprehensive_understanding": state["comprehensive_understanding"]}