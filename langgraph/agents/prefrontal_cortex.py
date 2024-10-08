"""
Agent that processes input information by simulating the prefrontal cortex
and assigning tasks to other parts of the system.
"""

from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from .src.utils import clean_json
from .models.brain import PrefrontalCortex
from .prompts.prefrontal_cortex import PREFRONTAL_CORTEX
from .config.models import model

# Inicializa o parser para o objeto PrefrontalCortex
parser = PydanticOutputParser(pydantic_object=PrefrontalCortex)

def prefrontal_cortex_agent(state):
    """
    Processes incoming messages and assigns tasks to different parts of the system.

    Args:
        state (dict): Current state containing input messages.

    Returns:
        dict: Dictionary with the tasks assigned to the different parts of the system.
    """
    # Cria o template do prompt com as instruções de formatação
    prompt = PromptTemplate(
        template=PREFRONTAL_CORTEX,
        input_variables=["messages"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )

    # Cria a cadeia de processamento
    chain = prompt | model

    # Invoca a cadeia de processamento com as mensagens de entrada
    response = chain.invoke({"messages": state["messages"]})

    # Limpa e converte a resposta em um dicionário
    result_dict = clean_json(response)

    # Retorna o dicionário com as tarefas atribuídas
    return {
        "behavior_planner": result_dict["behavior_planner"],
        "decision_maker": result_dict["decision_maker"],
        "social_behavior_modulator": result_dict["social_behavior_modulator"],
        "complex_thought_planner": result_dict["complex_thought_planner"],
        "personality_expression_planner": result_dict["personality_expression_planner"]
    }
