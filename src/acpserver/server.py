from beeai_sdk.providers.agent import Server
from beeai_sdk.schemas.text import TextOutput, TextInput, Con
from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel, VisitWebpageTool

server = Server("randoagentserver")


@server.agent()
async def run_crewai_agent(input: TextInput) -> TextOutput:

    model = LiteLLMModel(
        model_id="ollama_chat/qwen2.5:14b",
        api_base="http://localhost:11434",
        api_key="your-api-key",
        num_ctx=8192,
    )

    agent = CodeAgent(tools=[DuckDuckGoSearchTool(), VisitWebpageTool()], model=model)

    response = agent.run(input.text)

    return TextOutput(text=str(response))
