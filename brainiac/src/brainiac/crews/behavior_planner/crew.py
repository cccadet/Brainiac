import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

model_name = os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini")
llm = ChatOpenAI(temperature=0.2, model_name=model_name)

class BehaviorPlanner(BaseModel):
    comportamento_atual: str = Field(..., description="Comportamento atual")
    comportamento_alternativo: str = Field(..., description="Comportamento alternativo")
    mecanismo_controle: str = Field(..., description="Mecanismo de controle e monitoramento")
    plano_contingencia: str = Field(..., description="Plano de contingência")


@CrewBase
class BehaviorPlannerCrew():
    """Behavior Planner Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def behavior_planner(self) -> Agent:
        return Agent(
            config=self.agents_config["behavior_planner"], 
            verbose=True,
            llm=llm,
			allow_delegation=False,
            )

    @task
    def behavior_planning(self) -> Task:
        return Task(
            config=self.tasks_config["behavior_planning"],
            agent=self.behavior_planner(),
            output_pydantic=BehaviorPlanner
        )

    @crew
    def crew(self) -> Crew:
        """Generate behavior for Brainiac"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            llm=llm,
			memory=False,
        )
