""

import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model_name = os.environ.get("OPENAI_MODEL_NAME")

if model_name:
    model = ChatOpenAI(model=model_name)
