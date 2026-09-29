from core.tool_registry import ToolRegistry
from tools.lead_scoring import score_lead


registry = ToolRegistry()

registry.register(
    name="score_lead",
    description="Scores a business lead based on kronix tech  company size, website, and email availability.",
    function=score_lead,
)

print("Available tools:")
print(registry.list_tools())

print("\nTool result:")
print(
    registry.execute(
        "score_lead",
        company_size=25,
        has_website=True,
        has_email=True,
    )
)