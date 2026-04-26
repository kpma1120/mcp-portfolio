import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

from dotenv import load_dotenv
import os
import json

load_dotenv()

# Configuration
FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")

# Multi-server MCP client configuration
current_dir = os.path.dirname(os.path.abspath(__file__))
mcp_config_path = os.path.join(current_dir, "mcp.json")
mcp_json = json.load(open(mcp_config_path, 'r'))
mcp_json["firecrawl_server"]["env"] = {
    "FIRECRAWL_API_KEY": FIRECRAWL_API_KEY
}

async def main():
    client = MultiServerMCPClient(mcp_json)

    print(">>> Calling get_tools() ...")
    tools = await client.get_tools()
    print("\n📚 Available Tools:")
    for tool in tools:
        print(f"  • {tool.name}")
    print("\n>>> get_tools() test completed.")

if __name__ == "__main__":
    asyncio.run(main())
