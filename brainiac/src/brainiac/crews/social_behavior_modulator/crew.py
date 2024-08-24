import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

model_name = os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini")
llm = ChatOpenAI(temperature=0.2, model_name=model_name)

class SocialBehaviorModulator(BaseModel):
    social_behavior: str = Field(..., description="Comportamento social do Brainiac")
    guidelines: str = Field(..., description="Diretrizes para modulação do comportamento social")
    examples: str = Field(..., description="Exemplos de modulação do comportamento social")
    estrategy: str = Field(..., description="Estratégia de modulação do comportamento social")
    consistency: str = Field(..., description="Mecanismos de consistência e autenticidade na modulação do comportamento social")

@CrewBase
class SocialBehaviorModulatorCrew():
    """Social Behavior Modulator Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def social_behavior_modulator(self) -> Agent:
        return Agent(
            config=self.agents_config["social_behavior_modulator"], 
            llm=llm,
			allow_delegation=False,
            verbose=True
        )

    @task
    def social_behavior_modulation(self) -> Task:
        return Task(
            config=self.tasks_config["social_behavior_modulation"],
            agent=self.social_behavior_modulator(),
            output_pydantic=SocialBehaviorModulator

        )

    @crew
    def crew(self) -> Crew:
        """Generate social behavior for Brainiac"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            llm=llm,
			memory=False,
            planning=False,
        )
