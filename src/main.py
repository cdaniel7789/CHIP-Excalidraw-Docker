import os
from dotenv import load_dotenv
import vertexai

from agents.marketing_agent import MarketingAgent
from agents.sales_agent import SalesAgent
from tools.web_search import search

class Orchestrator:
    """
    The main orchestrator for the AI agent system.
    """
    def __init__(self):
        """
        Initializes the orchestrator, loading the configuration and setting up the agents.
        """
        load_dotenv()
        self.project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
        self.location = os.getenv("GOOGLE_CLOUD_LOCATION")
        vertexai.init(project=self.project_id, location=self.location)
        self.agents = {}
        self._add_agents()
        self.tools = {"web_search": search}

    def _add_agents(self):
        """
        Adds the marketing and sales agents to the orchestrator.
        """
        self.add_agent(MarketingAgent())
        self.add_agent(SalesAgent())

    def add_agent(self, agent):
        """
        Adds an agent to the orchestrator.

        Args:
            agent: The agent to add.
        """
        self.agents[agent.name] = agent

    def run(self, prompt: str) -> str:
        """
        Runs the orchestrator with the given prompt.

        Args:
            prompt: The prompt to run the orchestrator with.

        Returns:
            The response from the orchestrator.
        """
        # Check if the prompt requires a tool
        if "search:" in prompt.lower():
            query = prompt.split("search:")[-1].strip()
            return self.tools["web_search"](query)

        # Simple routing mechanism
        if "marketing" in prompt.lower():
            agent = self.agents.get("marketing")
        elif "sales" in prompt.lower():
            agent = self.agents.get("sales")
        else:
            return "No appropriate agent found for your request."

        if agent:
            return agent.run(prompt)
        else:
            return "Agent not found."


if __name__ == "__main__":
    orchestrator = Orchestrator()
    print("Orchestrator is running... Enter 'quit' to exit.")
    while True:
        prompt = input("Enter your prompt: ")
        if prompt.lower() == "quit":
            break
        response = orchestrator.run(prompt)
        print(f"Response: {response}")
