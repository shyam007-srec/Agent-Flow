from core.tool_registry import Tool
from tools.lead_scoring import score_lead
from tools.web_search import web_search


score_lead_tool = Tool(
    name="score_lead",
    description=(
        "Scores a business lead based on company size, "
        "website availability, and email availability."
    ),
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
    function=score_lead,
)

web_search_tool = Tool(
    name="web_search",
    description=(
        "Search the internet for information. "
        "You MUST provide a natural-language search query "
        "in the 'query' parameter. "
        "Example: 'roofing companies in Dallas Texas'."
    ),
    parameters={
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": (
                    "The exact natural-language search query. "
                    "Example: roofing companies in Dallas Texas."
                ),
            },
            "max_results": {
                "type": "integer",
                "description": "Number of search results to return.",
            },
        },
        "required": ["query"],
        "additionalProperties": False,
    },
    function=web_search,
)