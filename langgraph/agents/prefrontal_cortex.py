"""
Agente que processa informações de entrada simulando o córtex pré-frontal 
e atribuindo tarefas às demais partes do sistema.
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
    Processa as mensagens de entrada e atribui tarefas às diferentes partes do sistema.

    Args:
        state (dict): Estado atual contendo as mensagens de entrada.

    Returns:
        dict: Dicionário com as tarefas atribuídas às diferentes partes do sistema.
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
