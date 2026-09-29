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

When the user asks you to score a lead,
use the score_lead tool.

After receiving the tool result,
explain the result clearly.
""",
    tools=registry,
)


result = agent.run(
    """
Score this lead:

Company size: 25 employees
Website: yes
Business email: yes
"""
)

print("\nFINAL AGENT RESPONSE:\n")
print(result)