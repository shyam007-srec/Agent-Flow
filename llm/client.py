import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


class LLMClient:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("LLM_API_KEY"),
            base_url=os.getenv("LLM_BASE_URL"),
        )

        self.model = os.getenv(
            "LLM_MODEL",
            "llama-3.3-70b-versatile",
        )

    def chat(
        self,
        messages: list[dict],
        tools: list[dict] | None = None,
    ):
        request = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.2,
        }

        # Only add tool-related parameters when tools exist.
        if tools:
            request["tools"] = tools
            request["tool_choice"] = "auto"

        response = self.client.chat.completions.create(
            **request
        )

        return response.choices[0].message