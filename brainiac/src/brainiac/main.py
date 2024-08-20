#!/usr/bin/env python
import asyncio
from crewai.routers.router import Route
from crewai.routers.router import Router
from dotenv import load_dotenv

load_dotenv()

from brainiac.pipelines.pipeline_cortex_in import PrefrontalCortexInPipeline

async def run():
    """
    Run the pipeline.
    """
    inputs = [
       {
        "input": """
            Oi, meu nome é Cristian. Tudo certo?
        """
       }
    ]

    pipeline = PrefrontalCortexInPipeline().create_pipeline()

    

    results = await pipeline.kickoff(inputs)

    # Process and print results
    for result in results:
        print(f"Raw output: {result.raw}")
        if result.json_dict:
            print(f"JSON output: {result.json_dict}")
        print("\n")

def main():
    asyncio.run(run())

if __name__ == "__main__":
    main()