import asyncio

from acp.server.highlevel import Server, Context
from beeai_sdk.providers.agent import run_agent_provider
from beeai_sdk.schemas.text import TextOutput, TextInput
from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel, VisitWebpageTool

def main():
    server = Server("randoagentserver")

    @server.agent(
        "hello-world",
        "this is my hello world agent",
        input=TextInput,
        output=TextOutput,
    )
    async def run_crewai_agent(input: TextInput, ctx: Context) -> TextOutput:
        
        model = LiteLLMModel(
                model_id="ollama_chat/llama3.1:8b-beeai",
                api_base="http://localhost:11434",  # replace with remote open-ai compatible server if necessary
                api_key="your-api-key",  # replace with API key if necessary
                num_ctx=8192) 

        agent = CodeAgent(tools=[DuckDuckGoSearchTool(), VisitWebpageTool()], model=model)

        response = agent.run(
            input.text
        )

        return TextOutput(text=response)

    asyncio.run(run_agent_provider(server))


if __name__ == "__main__":
    main()