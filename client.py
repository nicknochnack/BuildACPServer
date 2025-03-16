import asyncio

from acp import ClientSession
from acp.client.sse import sse_client


async def run_client():
    async with sse_client(url="http://localhost:8000/sse") as streams:
        async with ClientSession(*streams) as session:
            await session.initialize()

            # List agents
            resp = await session.list_agents()
            print("Available agents:", [agent.name for agent in resp.agents])

            # Run agent
            resp = await session.run_agent("hello-world", {"text": "Bee"})
            print("Agent:", resp.output["text"])


asyncio.run(run_client())
