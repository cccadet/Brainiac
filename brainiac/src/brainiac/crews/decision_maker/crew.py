import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

model_name = os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini")
llm = ChatOpenAI(temperature=0.2, model_name=model_name)

class DecisionMaker(BaseModel):
    available_decisions: str = Field(..., description="Decisões disponíveis para o Brainiac")
    implications: str = Field(..., description="Implicações das decisões disponíveis")
    optimal_decision: str = Field(..., description="Decisão ótima para o Brainiac")
    decision_strategy: str = Field(..., description="Estratégia de decisão do Brainiac")
    decision_consistency: str = Field(..., description="Mecanismos de consistência e autenticidade nas decisões do Brainiac")

@CrewBase
class DecisionMakerCrew():
    """Social Behavior Modulator Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def decision_maker(self) -> Agent:
        return Agent(
            config=self.agents_config["decision_maker"],
            llm=llm,
			allow_delegation=False,
            verbose=True
        )

    @task
    def decision_making(self) -> Task:
        return Task(
            config=self.tasks_config["decision_making"],
            agent=self.decision_maker(),
            output_pydantic=DecisionMaker

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
