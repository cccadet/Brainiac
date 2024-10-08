from pydantic import BaseModel, Field

class PrefrontalCortex(BaseModel):
    """Modelo que representa a saída do primeiro processamento do brainiac"""
    expected_action: str = Field(..., description="Ação esperada para a entrada do humano")
    behavior_planner: str = Field(..., description="Informação necessária para o planejador de comportamento")
    decision_maker: str = Field(..., description="Informação necessária para o tomador de decisão")
    social_behavior_modulator: str = Field(..., description="Informação necessária para o modulador de comportamento social")
    complex_thought_planner: str = Field(..., description="Informação necessária para o planejador de pensamento complexo")
    personality_expression_planner: str = Field(..., description="Informação necessária para o planejador de expressão de personalidade")

class BehaviorPlanner(BaseModel):
    """Modelo que representa a saída do planejador de comportamento"""
    actual_behavior: str = Field(..., description="Comportamento atual")
    alternative_behavior: str = Field(..., description="Comportamento alternativo")
    control_mechanisms: str = Field(..., description="Mecanismo de controle e monitoramento")
    contingency_plans: str = Field(..., description="Planos de contingência")

class DecisionMaker(BaseModel):
    """Modelo que representa a saída do tomador de decisão"""
    available_decisions: str = Field(..., description="Decisões disponíveis para o Brainiac")
    implications: str = Field(..., description="Implicações das decisões disponíveis")
    optimal_decision: str = Field(..., description="Decisão ótima para o Brainiac")
    decision_strategy: str = Field(..., description="Estratégia de decisão do Brainiac")
    decision_consistency: str = Field(..., description="Mecanismos de consistência e autenticidade nas decisões do Brainiac")

class SocialBehaviorModulator(BaseModel):
    """Modelo que representa a saída do modulador de comportamento social"""
    social_behavior: str = Field(..., description="Comportamento social do Brainiac")
    guidelines: str = Field(..., description="Diretrizes para modulação do comportamento social")
    examples_modulator: str = Field(..., description="Exemplos de modulação do comportamento social")
    social_estrategy: str = Field(..., description="Estratégia de modulação do comportamento social")
    social_consistency: str = Field(..., description="Mecanismos de consistência e autenticidade na modulação do comportamento social")

class ComplexThoughtPlanner(BaseModel):
    """Modelo que representa a saída do planejador de pensamento complexo"""
    detailed_analysis: str = Field(..., description="Análise detalhada do problema")
    standard_relations: str = Field(..., description="Relações padrão entre os elementos")
    insights: str = Field(..., description="Insights profundos e soluções inovadoras")
    implications_scenarios: str = Field(..., description="Implicações de diferentes opções e cenários")
    comprehensive_understanding: str = Field(..., description="Compreensão abrangente do problema")

class PersonalityExpressionPlanner(BaseModel):
    """Modelo que representa a saída do planejador de expressão de personalidade"""
    personality: str = Field(..., description="Personalidade do Brainiac")
    guidelines_personality: str = Field(..., description="Diretrizes para expressão da personalidade")
    examples_personality: str = Field(..., description="Exemplos de expressão da personalidade")
    personality_estrategy: str = Field(..., description="Estratégia de expressão da personalidade")
    personality_consistency: str = Field(..., description="Mecanismos de consistência e autenticidade na expressão da personalidade")
