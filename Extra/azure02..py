import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="",
    api_key="",
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "Which planet has higest number of moons in one line?",
        }
    ],
    max_tokens=4096,
    temperature=1.0,
    top_p=1.0,
    model="gpt-4o"
)

print(response.choices[0].message.content)