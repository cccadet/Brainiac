from crewai import Pipeline
from crewai.project import PipelineBase
from ..crews.behavior_planner.crew import BehaviorPlannerCrew


@PipelineBase
class BehaviorPipeline:
    def __init__(self):
        # Initialize crews
        self.behavior_crew = BehaviorPlannerCrew().crew()

    def create_pipeline(self):
        return Pipeline(
            stages=[
                self.behavior_crew
            ]
        )
    
    async def kickoff(self, inputs):
        pipeline = self.create_pipeline()
        results = await pipeline.kickoff(inputs)
        return results


