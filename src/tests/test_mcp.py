import asyncio
from fastmcp import Client

async def example():
    async with Client("http://localhost:8000/sse/") as client:
        await client.ping()

if __name__ == "__main__":
    asyncio.run(example())