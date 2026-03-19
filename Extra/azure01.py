from openai import OpenAI

endpoint = ""
deployment_name = "gpt-4o"
api_key = ""

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

completion = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France in one word?",
        }
    ],
)

print(completion.choices[0].message)