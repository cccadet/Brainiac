from crewai import Pipeline
from crewai.project import PipelineBase
from ..crews.prefrontal_cortex_in.crew import PrefrontalCortexInCrew
from ..crews.behavior_planner.crew import BehaviorPlannerCrew
from ..crews.complex_thought_planner.crew import ComplexThoughtPlannerCrew

@PipelineBase
class PrefrontalCortexInPipeline:
    def __init__(self):
        # Initialize crews
        self.cortex_in = PrefrontalCortexInCrew().crew()
        self.behavior_crew = BehaviorPlannerCrew().crew()
        self.complex_thought_crew = ComplexThoughtPlannerCrew().crew()

    def create_pipeline(self):
        return Pipeline(
            stages=[
                self.cortex_in,
                [self.behavior_crew, self.complex_thought_crew]
            ]
        )
    
    async def kickoff(self, inputs):
        pipeline = self.create_pipeline()
        results = await pipeline.kickoff(inputs)
        return results


