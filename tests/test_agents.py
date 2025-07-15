import unittest
from unittest.mock import patch, MagicMock

from src.agents.base import Agent
from src.agents.marketing_agent import MarketingAgent
from src.agents.sales_agent import SalesAgent

class TestAgents(unittest.TestCase):
    def test_base_agent(self):
        with self.assertRaises(NotImplementedError):
            agent = Agent("test", "test instructions")
            agent.run("test prompt")

    @patch("src.agents.marketing_agent.GenerativeModel")
    @patch("vertexai.init")
    def test_marketing_agent(self, mock_vertexai, mock_model):
        mock_response = MagicMock()
        mock_response.text = "Marketing response"
        mock_model.return_value.generate_content.return_value = mock_response

        agent = MarketingAgent()
        response = agent.run("test prompt")
        self.assertEqual(response, "Marketing response")

    @patch("src.agents.sales_agent.GenerativeModel")
    @patch("vertexai.init")
    def test_sales_agent(self, mock_vertexai, mock_model):
        mock_response = MagicMock()
        mock_response.text = "Sales response"
        mock_model.return_value.generate_content.return_value = mock_response

        agent = SalesAgent()
        response = agent.run("test prompt")
        self.assertEqual(response, "Sales response")

if __name__ == "__main__":
    unittest.main()
