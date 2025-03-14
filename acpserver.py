import asyncio

from acp.server.highlevel import Server, Context
from beeai_sdk.providers.agent import run_agent_provider
from beeai_sdk.schemas.text import TextOutput, TextInput


def run():
    server = Server("randoagentserver")

    @server.agent()
    async def run_crewai_agent(input: TextInput, ctx: Context) -> TextOutput:
        # Core logic for the "hello-world" agent
        return TextOutput(text=f"Hi there {input.text}")

    run_agent_provider(server)


if __name__ == "__main__":
    asyncio.run(run())
