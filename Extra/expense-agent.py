# chatbot.py
# Before running:
#    pip install --pre azure-ai-projects>=2.0.0b4
#    pip install python-dotenv

import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Load environment variables from .env file if present
load_dotenv()

# Configure your endpoint (can also be set via .env)
my_endpoint = os.getenv("AZURE_PROJECT_ENDPOINT", "")

# Initialize project client
project_client = AIProjectClient(
    endpoint=my_endpoint,
    credential=DefaultAzureCredential(),
)

# Agent reference
my_agent = "ExpensesAgent"
my_version = "2"

# Get OpenAI client
openai_client = project_client.get_openai_client()

print("💬 Chatbot ready! Type 'exit' to quit.\n")

while True:
    # Get user input
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    # Send input to agent
    response = openai_client.responses.create(
        input=[{"role": "user", "content": user_input}],
        extra_body={
            "agent_reference": {
                "name": my_agent,
                "version": my_version,
                "type": "agent_reference"
            }
        },
    )

    # Print agent response
    print(f"Agent: {response.output_text}\n")