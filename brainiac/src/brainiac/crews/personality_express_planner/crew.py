import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

model_name = os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini")
llm = ChatOpenAI(temperature=0.2, model_name=model_name)

class PersonalityExpressionPlanner(BaseModel):
    personality: str = Field(..., description="Personalidade do Brainiac")
    guidelines: str = Field(..., description="Diretrizes para expressão da personalidade")
    examples: str = Field(..., description="Exemplos de expressão da personalidade")
    estrategy: str = Field(..., description="Estratégia de expressão da personalidade")
    consistency: str = Field(..., description="Mecanismos de consistência e autenticidade na expressão da personalidade")


@CrewBase
class PersonalityExpressPlannerCrew():
    """Personality Express Planner Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def personality_express_planner(self) -> Agent:
        return Agent(
            config=self.agents_config["personality_express_planner"],
            verbose=True,
            llm=llm,
			allow_delegation=False,
        )

    @task
    def personality_expression_planning(self) -> Task:
        return Task(
            config=self.tasks_config["personality_expression_planning"],
            agent=self.personality_express_planner(),
            output_pydantic=PersonalityExpressionPlanner
        )

    @crew
    def crew(self) -> Crew:
        """Generate personality expression for Brain"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            llm=llm,
			memory=False,
            planning=False,
        )
