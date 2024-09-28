"""
This module contains the Social Behavior Modulator agent.
"""

from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from .src.utils import clean_json
from .config.models import model
from .models.brain import SocialBehaviorModulator
from .prompts.social_behavior_modulator import SOCIAL_BEHAVIOR_MODULATOR

parser_social_behavior_modulator = PydanticOutputParser(pydantic_object=SocialBehaviorModulator)

def social_behavior_modulator_agent(state):
    """Social Behavior Modulator Agent"""
    prompt = PromptTemplate(
        template = SOCIAL_BEHAVIOR_MODULATOR,
        input_variables=["messages"],
        partial_variables={"format_instructions": parser_social_behavior_modulator.get_format_instructions()}
    )
    chain = prompt | model
    response = chain.invoke({"messages": state["messages"], "expected_action": state["social_behavior_modulator"]})

    result_dict = clean_json(response)

    return {
        "social_behavior": result_dict["social_behavior"],
        "guidelines": result_dict["guidelines"],
        "examples_modulator": result_dict["examples_modulator"],
        "social_estrategy": result_dict["social_estrategy"],
        "social_consistency": result_dict["social_consistency"]
    }