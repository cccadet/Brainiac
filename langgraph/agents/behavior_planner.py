"""
Agente que processa informações vindas do cortex pré-frontal e planeja o comportamento.
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
    """Esssa função é responsável por gerar um plano de comportamento para o agente
    
    Args:
        state (dict): Dicionário com informações sobre o estado atual do agente

    Returns:
        dict: Dicionário com informações sobre o plano de comportamento gerado
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
