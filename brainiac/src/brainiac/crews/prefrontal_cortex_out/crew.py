import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel
from langchain_openai import ChatOpenAI

model_name = os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini")
llm = ChatOpenAI(temperature=0.2, model_name=model_name)

@CrewBase
class ClassifierCrew:
    """Email Classifier Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def decision_maker(self) -> Agent:
        return Agent(
            config=self.agents_config["decision_maker"],
            verbose=True,
            llm=llm,
			allow_delegation=False,
        )
    
    def prefrontal_manager(self) -> Agent:
        return Agent(
            config=self.agents_config["prefrontal_manager"],
            verbose=True,
            llm=llm,
			allow_delegation=True,
        )

    @task
    def decision_making(self) -> Task:
        return Task(
            config=self.tasks_config["decision_making"],
            agent=self.decision_maker(),
        )
    
    @task
    def prefrontal_management(self) -> Task:
        return Task(
            config=self.tasks_config["prefrontal_management"],
            agent=self.prefrontal_manager(),
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Email Classifier Crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            llm=llm,
			memory=True,
			full_output=True,
			planning=True,
        )
