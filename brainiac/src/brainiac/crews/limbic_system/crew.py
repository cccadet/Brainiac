import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

model_name = os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini")
llm = ChatOpenAI(temperature=0.2, model_name=model_name)

class Amygdala(BaseModel):
    immediate_recommendation: str = Field(..., description="Recomendação imediata")
    intensity: str = Field(..., description="Intensidade da emoção")
    action: str = Field(..., description="Ação a ser tomada")
    justification: str = Field(..., description="Justificativa da ação")

@CrewBase
class LimbicSystemCrew():
    """Limbic System Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def amygdala_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["amygdala_agent"],
            verbose=True,
            llm=llm,
			allow_delegation=False,
            )

    @task
    def stimulus_amygdala(self) -> Task:
        return Task(
            config=self.tasks_config["stimulus_amygdala"],
            agent=self.amygdala_agent(),
            output_pydantic=Amygdala
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
            planning=False,
        )
