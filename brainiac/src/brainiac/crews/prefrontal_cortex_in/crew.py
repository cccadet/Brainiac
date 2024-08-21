import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

model_name = os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini")
llm = ChatOpenAI(temperature=0.2, model_name=model_name)

class PrefrontalCortex(BaseModel):
    """Prefrontal Cortex"""
    acao_esperada: str = Field(..., description="Ação de esperada")
    behavior_planner: str = Field(..., description="Informação necessária para o planejador de comportamento")
    decision_maker: str = Field(..., description="Informação necessária para o tomador de decisão")
    social_behavior_modulator: str = Field(..., description="Informação necessária para o modulador de comportamento social")
    complex_thought_planner: str = Field(..., description="Informação necessária para o planejador de pensamento complexo")
@CrewBase
class PrefrontalCortexInCrew():
    """Prefrontal Cortex In Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def prefrontal_manager(self) -> Agent:
        return Agent(
            config=self.agents_config["prefrontal_manager"],
            verbose=True,
            llm=llm,
			allow_delegation=False,
        )

    @task
    def prefrontal_management(self) -> Task:
        return Task(
            config=self.tasks_config["prefrontal_management"],
            agent=self.prefrontal_manager(),
            output_pydantic=PrefrontalCortex
        )

    @crew
    def crew(self) -> Crew:
        """Prefrontal Cortex In Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            llm=llm,
			memory=False,
			full_output=False,
			planning=False,
        )
