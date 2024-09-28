"""
This module contains the prompts for the Prefrontal Cortex agent.
"""

PREFRONTAL_CORTEX = """
Identificar a ação esperada para a entrada do humano: {messages}
O Prefrontal Cortex deve raciocinar sobre quais ações devem ser tomadas e como essas 
ações serão distribuídas entre os agentes. A tarefa envolve criar um plano estratégico 
que define claramente como cada agente contribuirá para o objetivo global.

A saída esperada é um plano estratégico para distribuir as tarefas entre os 
agentes:

{format_instructions}
"""
