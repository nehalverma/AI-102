# Requirements
# Deploy GPT-4o model in Foundry
# Get the key and endpoint and update the code


import os
from dotenv import load_dotenv

# Add references
# Add references
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from openai import AzureOpenAI

def main(): 

    # Clear the console
    os.system('cls' if os.name=='nt' else 'clear')
        
    try: 
    
        # Get configuration settings 
        load_dotenv()
        project_endpoint = os.getenv("PROJECT_ENDPOINT")
        model_deployment =  os.getenv("MODEL_DEPLOYMENT")

        # update endpoint
        endpoint = "https://projectxxxxxxxxxxxx-resource.cognitiveservices.azure.com/"
        model_name = "gpt-4o"
        deployment = "gpt-4o"

        # update key
        subscription_key = "xxxxxxxxxxxxxxxxxxxxxxxx"
        api_version = "2024-12-01-preview"

        client = AzureOpenAI(
            api_version=api_version,
            azure_endpoint=endpoint,
            api_key=subscription_key,
        )

        # Initialize prompt with system message
        # Initialize prompt with system message
        prompt = [
                {"role": "system", "content": "You are a helpful AI assistant that answers questions."}
            ] 

        # Loop until the user types 'quit'
        while True:
            # Get input text
            input_text = input("Enter the prompt (or type 'quit' to exit): ")
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a prompt.")
                continue
            
            # Get a chat completion
            # Get a chat completion
            prompt.append({"role": "user", "content": input_text})
            response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=prompt)
            completion = response.choices[0].message.content
            print(completion)
            prompt.append({"role": "assistant", "content": completion})

    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()