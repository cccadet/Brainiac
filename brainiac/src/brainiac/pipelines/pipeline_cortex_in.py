from crewai import Pipeline
from crewai.project import PipelineBase
from ..crews.prefrontal_cortex_in.crew import PrefrontalCortexInCrew


@PipelineBase
class PrefrontalCortexInPipeline:
    def __init__(self):
        # Initialize crews
        self.cortex_in = PrefrontalCortexInCrew().crew()

    def create_pipeline(self):
        return Pipeline(
            stages=[
                self.cortex_in
            ]
        )
    
    async def kickoff(self, inputs):
        pipeline = self.create_pipeline()
        results = await pipeline.kickoff(inputs)
        return results


