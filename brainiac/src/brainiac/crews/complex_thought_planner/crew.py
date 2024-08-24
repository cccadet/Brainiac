import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

model_name = os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini")
llm = ChatOpenAI(temperature=0.6, model_name=model_name)

class ComplexThoughtPlanner(BaseModel):
    analise_detalhada: str = Field(..., description="Análise detalhada de informações relevantes")
    padroes_relacoes: str = Field(..., description="Padrões e relações entre informações")
    insights: str = Field(..., description="Insights profundos e soluções inovadoras")
    implicacoes_cenarios: str = Field(..., description="Implicações de diferentes opções e cenários")
    compreensao_abrangente: str = Field(..., description="Compreensão abrangente do problema")

@CrewBase
class ComplexThoughtPlannerCrew():
    """Complex Thought Planner Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def complex_thought_planner(self) -> Agent:
        return Agent(
            config=self.agents_config["complex_thought_planner"],
            verbose=True,
            llm=llm,
			allow_delegation=False,
            )

    @task
    def complex_thought_planning(self) -> Task:
        return Task(
            config=self.tasks_config["complex_thought_planning"],
            agent=self.complex_thought_planner(),
            output_pydantic=ComplexThoughtPlanner
        )

    @crew
    def crew(self) -> Crew:
        """Generate complex thought for Brainiac"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            llm=llm,
			memory=False,
            planning=False,
        )
