from core.agent import Agent
from core.tool_registry import ToolRegistry

from tools.definitions import (
    score_lead_tool,
    web_search_tool,
)


registry = ToolRegistry()

registry.register(score_lead_tool)
registry.register(web_search_tool)


agent = Agent(
    name="Lead Research Agent",
    system_prompt = """
You are a Lead Research Agent.

Your job is to research business leads using web_search.

IMPORTANT RULES:

1. Use web_search when external information is required.
2. Start with one broad search.
3. Use additional searches only when they provide genuinely
   missing information.
4. Do not repeatedly search the same company or website.
5. Do not search more than 3 times for a single user request.
6. Once you have enough information to answer the user's request,
   STOP using tools and provide the final answer.
7. Never invent company information.
8. Clearly distinguish information found in search results from
   information that could not be verified.

For a request for companies, return:

Company Name
Website
Relevant information found

Keep the final answer concise.
""",
    tools=registry,
)


response = agent.run(
    "Find roofing companies in Dallas, Texas. "
    "Give me the company names and websites."
)

print("\nFINAL RESPONSE:\n")
print(response)