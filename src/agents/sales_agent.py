from .base import Agent
from vertexai.preview.generative_models import GenerativeModel

class SalesAgent(Agent):
    """
    The sales agent.
    """
    def __init__(self):
        """
        Initializes the sales agent.
        """
        super().__init__(
            name="sales",
            instructions="You are a sales expert. Your goal is to close deals and increase revenue."
        )
        self.model = GenerativeModel("gemini-1.0-pro")

    def run(self, prompt: str) -> str:
        """
        Runs the sales agent with the given prompt.

        Args:
            prompt: The prompt to run the agent with.

        Returns:
            The response from the agent.
        """
        full_prompt = f"{self.instructions}\n\n{prompt}"
        response = self.model.generate_content(full_prompt)
        return response.text
