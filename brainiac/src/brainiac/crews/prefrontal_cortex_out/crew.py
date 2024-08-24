import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

model_name = os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini")
llm = ChatOpenAI(temperature=0.2, model_name=model_name)

@CrewBase
class PrefrontalCortexOutCrew():
    """Prefrontal Cortex Out Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def prefrontal_manager(self) -> Agent:
        return Agent(
            config=self.agents_config["prefrontal_manager"],
            verbose=True,
            llm=llm,
			allow_delegation=True,
        )
    
    @task
    def prefrontal_management(self) -> Task:
        return Task(
            config=self.tasks_config["prefrontal_management"],
            agent=self.prefrontal_manager(),
        )

    @crew
    def crew(self) -> Crew:
        """Generate social behavior for Brainiac"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            llm=llm,
			memory=False,
			full_output=True,
			planning=False,
        )
