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

PREFRONTAL_CORTEX_OUT = """
Interaction: {messages}

The Prefrontal Cortex has analyzed the input and distributed the tasks among the agents.
Here are the results:

Behavior Planner: 
- Actual Behavior: {actual_behavior}
- Alternative Behavior: {alternative_behavior}
- Control Mechanisms: {control_mechanisms}
- Contingency Plans: {contingency_plans}

Decision Maker:
- Available Decisions: {available_decisions}
- Implications: {implications}
- Optimal Decision: {optimal_decision}
- Decision Strategy: {decision_strategy}
- Decision Consistency: {decision_consistency}

Social Behavior Modulator:
- Social Behavior: {social_behavior}
- Guidelines: {guidelines}
- Modulator Examples: {examples_modulator}
- Social Estrategy: {social_estrategy}
- Social Consistency: {social_consistency}

Complex Thought Planner:
- Detailed Analysis: {detailed_analysis}
- Standard Relations: {standard_relations}
- Insights: {insights}
- Implications Scenarios: {implications_scenarios}
- Comprehensive Understanding: {comprehensive_understanding}

Personality Expression Planner:
- Personality: {personality}
- Guidelines: {guidelines_personality}
- Personality Examples: {examples_personality}
- Personality Estrategy: {personality_estrategy}
- Personality Consistency: {personality_consistency}

Based on this analysis, answer the interaction.

"""