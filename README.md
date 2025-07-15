# AI Agent Orchestrator

This project is an AI agent orchestrator that uses Vertex AI to lead marketing and sales AI agents.

## Features

- **Agent Orchestration:** The orchestrator can route tasks to the appropriate agent based on the input.
- **Marketing and Sales Agents:** The system includes two agents: a marketing agent and a sales agent.
- **Custom Tools:** The agents can use custom tools, such as a web search tool.
- **Vertex AI Integration:** The agents are integrated with Vertex AI's generative models.

## Getting Started

### Prerequisites

- Python 3.12 or later
- A Google Cloud project with the Vertex AI API enabled
- Application Default Credentials set up for your environment

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/your-repository.git
   ```
2. Create a virtual environment:
   ```
   python3 -m venv .venv
   ```
3. Activate the virtual environment:
   ```
   source .venv/bin/activate
   ```
4. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Create a `.env` file with the following content:
   ```
   GOOGLE_CLOUD_PROJECT="your-gcp-project-id"
   GOOGLE_CLOUD_LOCATION="your-gcp-location"
   ```

### Usage

To run the orchestrator, run the following command:
```
python src/main.py
```

## Testing

To run the unit tests, run the following command:
```
python -m unittest discover tests
```
