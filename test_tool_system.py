from core.agent import Agent
from core.tool_registry import ToolRegistry
from tools.definitions import score_lead_tool


registry = ToolRegistry()

registry.register(score_lead_tool)

print("Registered tools:")
print(registry.list_tools())


agent = Agent(
    name="Lead Research Agent",
    system_prompt="""
You are a Lead Research Agent.

You help users analyze and qualify business leads.

When the user asks you to score a lead,
use the score_lead tool.

After receiving the tool result,
explain the result clearly.
""",
    tools=registry,
)


response = agent.run(
    """
Score this lead:

Company size: 25 employees
Website: yes
Business email: yes
"""
)

print("\nAgent response:")
print(response)