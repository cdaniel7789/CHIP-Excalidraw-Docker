from .base import Agent
from vertexai.preview.generative_models import GenerativeModel

class MarketingAgent(Agent):
    """
    The marketing agent.
    """
    def __init__(self):
        """
        Initializes the marketing agent.
        """
        super().__init__(
            name="marketing",
            instructions="You are a marketing expert. Your goal is to create effective marketing campaigns."
        )
        self.model = GenerativeModel("gemini-1.0-pro")

    def run(self, prompt: str) -> str:
        """
        Runs the marketing agent with the given prompt.

        Args:
            prompt: The prompt to run the agent with.

        Returns:
            The response from the agent.
        """
        full_prompt = f"{self.instructions}\n\n{prompt}"
        response = self.model.generate_content(full_prompt)
        return response.text
