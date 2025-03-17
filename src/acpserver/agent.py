from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel, VisitWebpageTool

model = LiteLLMModel(
        model_id="ollama_chat/llama3.1:8b-beeai",
        api_base="http://localhost:11434",  # replace with remote open-ai compatible server if necessary
        api_key="your-api-key",  # replace with API key if necessary
        num_ctx=8192) 

agent = CodeAgent(tools=[DuckDuckGoSearchTool(), VisitWebpageTool()], model=model)

response = agent.run(
    "How tall is the Sydney Harbour Bridge in km?",
)

print(response) 