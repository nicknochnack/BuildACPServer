from beeai_sdk.providers.agent import Server, Context
from beeai_sdk.schemas.text import TextOutput, TextInput
from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel, VisitWebpageTool

server = Server("randoagentserver")


@server.agent()
async def run_crewai_agent(input: TextInput, ctx: Context) -> TextOutput:

    model = LiteLLMModel(
        model_id="ollama_chat/qwen2.5:14b",
        api_base="http://host.docker.internal:11434",
        api_key="your-api-key",
        num_ctx=8192,
    )

    agent = CodeAgent(tools=[DuckDuckGoSearchTool(), VisitWebpageTool()], model=model)

    response = agent.run(input.text)

    return TextOutput(text=str(response))
