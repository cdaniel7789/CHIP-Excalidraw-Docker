class Agent:
    """
    The base class for all agents.
    """
    def __init__(self, name: str, instructions: str):
        """
        Initializes the agent.

        Args:
            name: The name of the agent.
            instructions: The instructions for the agent.
        """
        self.name = name
        self.instructions = instructions

    def run(self, prompt: str) -> str:
        """
        Runs the agent with the given prompt.

        Args:
            prompt: The prompt to run the agent with.

        Returns:
            The response from the agent.
        """
        raise NotImplementedError
