import asyncio

from acp.server.highlevel import Server, Context
from beeai_sdk.providers.agent import run_agent_provider
from beeai_sdk.schemas.text import TextOutput, TextInput


def main():
    server = Server("randoagentserver")

    @server.agent(
        "hello-world",
        "this is my hello world agent",
        input=TextInput,
        output=TextOutput,
    )
    async def run_crewai_agent(input: TextInput, ctx: Context) -> TextOutput:
        # Core logic for the "hello-world" agent
        return TextOutput(text=f"Wassup homeboy {input.text}!")

    asyncio.run(run_agent_provider(server))


if __name__ == "__main__":
    main()
