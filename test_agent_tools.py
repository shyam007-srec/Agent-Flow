import json

from core.agent import Agent
from core.tool_registry import ToolRegistry
from tools.lead_scoring import score_lead


registry = ToolRegistry()

registry.register(
    name="score_lead",
    description=(
        "Scores a business lead based on company size, "
        "website availability, and email availability."
    ),
    function=score_lead,
    parameters={
        "type": "object",
        "properties": {
            "company_size": {
                "type": "integer",
                "description": "Approximate number of employees.",
            },
            "has_website": {
                "type": "boolean",
                "description": "Whether the company has a website.",
            },
            "has_email": {
                "type": "boolean",
                "description": "Whether a business email is available.",
            },
        },
        "required": [
            "company_size",
            "has_website",
            "has_email",
        ],
    },
)


agent = Agent(
    name="Lead Research Agent",
    system_prompt="""
You are a Lead Research Agent.

You help users analyze and qualify business leads.

You have access to tools.

When a user asks you to score or qualify a lead,
use the appropriate tool instead of calculating the
score yourself.

Always explain the result after the tool executes.
""",
)


messages = [
    {
        "role": "system",
        "content": agent.system_prompt,
    },
    {
        "role": "user",
        "content": """
Score this lead:

Company size: 25 employees
Website: yes
Business email: yes
""",
    },
]


response = agent.llm.chat(
    messages,
    tools=registry.get_openai_tools(),
)


print("LLM response:")

print(response.content)

print("\nTool calls:")

if response.tool_calls:
    for tool_call in response.tool_calls:
        print(
            tool_call.function.name,
            tool_call.function.arguments,
        )