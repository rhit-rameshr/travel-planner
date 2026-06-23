from praisonaiagents import Agent, Agents, MCP
from rich import print
import gradio as gr
import os


from dotenv import load_dotenv
load_dotenv()


research_agent = Agent(
    instructions="""
    Use tavily_search at most 2 times.

    After gathering information,
    produce a final answer with:
    - Top attractions
    - Best parks and gardens
    - Day trips
    - Family activities
    """,
    llm="groq/meta-llama/llama-4-scout-17b-16e-instruct",
    tools=MCP(
        "npx -y tavily-mcp",
        env={
            "TAVILY_API_KEY": os.getenv("TAVILY_API_KEY")
        }
    )
)

flight_agent = Agent(
    instructions="Search for available flights, compare prices, and recommend optimal flight choices",
    llm="groq/meta-llama/llama-4-scout-17b-16e-instruct",
    tools=MCP(
        "npx -y tavily-mcp",
        env={
            "TAVILY_API_KEY": os.getenv("TAVILY_API_KEY")
        }
    )
)

accommodation_agent = Agent(
    instructions="Search for available accommodations, compare prices, and recommend optimal options. Look for both hotels and Airbnb options. Make sure to compare both price and rating.",
    llm="groq/meta-llama/llama-4-scout-17b-16e-instruct",
    tools=MCP(
        "npx -y tavily-mcp",
        env={
            "TAVILY_API_KEY": os.getenv("TAVILY_API_KEY")
        }
    )
)

itinerary_agent = Agent(
    instructions="Create a detailed travel itinerary based on the user's preferences and the information gathered by the other agents.",
    llm="groq/meta-llama/llama-4-scout-17b-16e-instruct",
    tools=MCP(
        "npx -y tavily-mcp",
        env={
            "TAVILY_API_KEY": os.getenv("TAVILY_API_KEY")
        }
    )
)

from app.graph.graph import graph

result = graph.invoke(
    {
        "user_query": "Trip to Japan for 7 days under $3000"
    }
)

print(result)