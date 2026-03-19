# Requirements
# GPT-4o model (key and endpoint)

# Expectation: This code will read image data from a URL or from a folder.

# Participants are requested to comment out the other block of code,
# e.g., comment the folder section when reading data from a URL, and vice versa.

import os
from urllib.request import urlopen, Request
import base64
from pathlib import Path
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
        endpoint = "https://projectxxxxxxxxxxxx-resource.cognitiveservices.azure.com/"
        model_name = "gpt-4o"
        deployment = "gpt-4o"

        subscription_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        api_version = "2024-12-01-preview"

        client = AzureOpenAI(
            api_version=api_version,
            azure_endpoint=endpoint,
            api_key=subscription_key,
        )

        # Initialize prompts
        system_message = "You are an AI assistant in a grocery store that sells fruit. You provide detailed answers to questions about produce."
        prompt = ""

        # Loop until the user types 'quit'
        while True:
            prompt = input("\nAsk a question about the image\n(or type 'quit' to exit)\n")
            if prompt.lower() == "quit":
                break
            elif len(prompt) == 0:
                    print("Please enter a question.\n")
            else:
                print("Getting a response ...\n")


                # Get a response to image input
                #---------- Read data from URL ( Comment this block if reading data from folder)
                # Get a response to image input - url 
                image_url = "https://github.com/MicrosoftLearning/mslearn-ai-vision/raw/refs/heads/main/Labfiles/gen-ai-vision/orange.jpeg"
                image_format = "jpeg"
                request = Request(image_url, headers={"User-Agent": "Mozilla/5.0"})
                image_data = base64.b64encode(urlopen(request).read()).decode("utf-8")
                data_url = f"data:image/{image_format};base64,{image_data}"

                response = client.chat.completions.create(
                    model= deployment,
                    messages=[
                        {"role": "system", "content": system_message},
                        { "role": "user", "content": [  
                            { "type": "text", "text": prompt},
                            { "type": "image_url", "image_url": {"url": data_url}}
                        ] } 
                    ]
                )
                print(response.choices[0].message.content)    
                

                #---------- Read data from folder ( Comment this block if reading data from URL)
                '''
                # Get a response to image input - read data from folder
                script_dir = Path(__file__).parent  # Get the directory of the script
                image_path = script_dir / 'mystery-fruit.jpeg'
                mime_type = "image/jpeg"

                # Read and encode the image file
                with open(image_path, "rb") as image_file:
                    base64_encoded_data = base64.b64encode(image_file.read()).decode('utf-8')

                # Include the image file data in the prompt
                data_url = f"data:{mime_type};base64,{base64_encoded_data}"
                response = client.chat.completions.create(
                        model=deployment,
                        messages=[
                            {"role": "system", "content": system_message},
                            { "role": "user", "content": [  
                                { "type": "text", "text": prompt},
                                { "type": "image_url", "image_url": {"url": data_url}}
                            ] } 
                        ]
                )
                print(response.choices[0].message.content)
                '''

    except Exception as ex:
        print(ex)


if __name__ == '__main__': 
    main()



