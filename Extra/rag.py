import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="",
    api_key="",
)

rag_params = {
    "data_sources": [
        {
            "type": "azure_search",
            "parameters": {
                "endpoint": "https://azureaisearch017.search.windows.net",
                "index_name": "dataindex",
                "authentication": {
                    "type": "api_key",
                    "key": "82MSUvbPOpzh4uY5P0arO2k4Bdz0c28dJqHgHFf0d6AzSeDYFmvl",
                }
            }
        }
    ],
}

response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What was the net profit in Q3 2025 in one line?",
        }
    ],
    max_tokens=4096,
    temperature=1.0,
    top_p=1.0,
    model="gpt-4o",
    extra_body=rag_params
)

print(response.choices[0].message.content)