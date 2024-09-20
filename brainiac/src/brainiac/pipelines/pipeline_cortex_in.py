from crewai import Pipeline
from crewai.project import PipelineBase
from ..crews.prefrontal_cortex_in.crew import PrefrontalCortexInCrew
from ..crews.behavior_planner.crew import BehaviorPlannerCrew
from ..crews.complex_thought_planner.crew import ComplexThoughtPlannerCrew
from ..crews.personality_express_planner.crew import PersonalityExpressPlannerCrew
from ..crews.social_behavior_modulator.crew import SocialBehaviorModulatorCrew
from ..crews.decision_maker.crew import DecisionMakerCrew
from ..crews.limbic_system.crew import LimbicSystemCrew
from ..crews.prefrontal_cortex_out.crew import PrefrontalCortexOutCrew


@PipelineBase
class PrefrontalCortexInPipeline:
    def __init__(self):
        # Initialize crews
        self.cortex_in = PrefrontalCortexInCrew().crew()
        self.behavior_crew = BehaviorPlannerCrew().crew()
        self.complex_thought_crew = ComplexThoughtPlannerCrew().crew()
        self.personality_express_crew = PersonalityExpressPlannerCrew().crew()
        self.social_behavior_crew = SocialBehaviorModulatorCrew().crew()
        self.decision_maker_crew = DecisionMakerCrew().crew()
        self.limbic_system_crew = LimbicSystemCrew().crew()
        self.cortex_out = PrefrontalCortexOutCrew().crew()

    def create_pipeline(self):
        return Pipeline(
            stages=[
                self.cortex_in,
                [self.behavior_crew, self.complex_thought_crew, self.personality_express_crew, self.social_behavior_crew],
                [self.decision_maker_crew, self.limbic_system_crew],
                self.cortex_out
            ]
        )

    async def kickoff(self, inputs):
        pipeline = self.create_pipeline()
        results = await pipeline.kickoff(inputs)
        return results
