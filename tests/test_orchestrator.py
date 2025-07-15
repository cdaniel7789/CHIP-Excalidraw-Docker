import unittest
from unittest.mock import patch, MagicMock

from src.main import Orchestrator

class TestOrchestrator(unittest.TestCase):
    @patch("src.main.vertexai")
    @patch("src.main.load_dotenv")
    def setUp(self, mock_load_dotenv, mock_vertexai):
        with patch("src.main.MarketingAgent"), patch("src.main.SalesAgent"):
            self.orchestrator = Orchestrator()

    @patch("src.main.MarketingAgent")
    def test_run_marketing_agent(self, mock_marketing_agent):
        self.orchestrator.agents["marketing"] = mock_marketing_agent()
        self.orchestrator.agents["marketing"].run.return_value = "Marketing response"
        response = self.orchestrator.run("marketing: test prompt")
        self.assertEqual(response, "Marketing response")

    @patch("src.main.SalesAgent")
    def test_run_sales_agent(self, mock_sales_agent):
        self.orchestrator.agents["sales"] = mock_sales_agent()
        self.orchestrator.agents["sales"].run.return_value = "Sales response"
        response = self.orchestrator.run("sales: test prompt")
        self.assertEqual(response, "Sales response")

    def test_run_no_agent(self):
        response = self.orchestrator.run("unknown: test prompt")
        self.assertEqual(response, "No appropriate agent found for your request.")

    @patch("src.tools.web_search.requests.get")
    def test_run_web_search(self, mock_get):
        mock_response = MagicMock()
        mock_response.text = '<html><body><div class="BNeawe vvjwJb AP7Wnd">Search results</div></body></html>'
        mock_get.return_value = mock_response
        response = self.orchestrator.run("search: test query")
        self.assertEqual(response, "Search results")

if __name__ == "__main__":
    unittest.main()
