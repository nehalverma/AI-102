# Final code (endpoint and key need to be updated)

# Requirements
# Deploy 2 models:
# - gpt-4o-mini-transcribe (key and endpoint)
# - gpt-4o (key and endpoint)


import os
import requests
from openai import AzureOpenAI

def main(): 
    os.system('cls' if os.name=='nt' else 'clear')
        
    try: 
        # --- Update these with your Foundry deployment details ---
        # Transcription model (e.g., gpt-4o-mini-transcribe or whisper-1)
        transcription_endpoint = "https://projectxxxxxxxxxxxx-resource.cognitiveservices.azure.com/openai/deployments/gpt-4o-mini-transcribe/audio/transcriptions?api-version=2025-03-01-preview"
        transcription_key = "YOUR_TRANSCRIPTION_KEY"
        transcription_api_version = "2024-12-01-preview"

        # Chat model (e.g., gpt-4o)
        chat_endpoint = "https://projectxxxxxxxxxxxxxx-resource.cognitiveservices.azure.com/"
        chat_key = "YOUR_CHAT_KEY"
        chat_api_version = "2024-12-01-preview"

        # Initialize separate clients
        transcription_client = AzureOpenAI(
            api_version=transcription_api_version,
            azure_endpoint=transcription_endpoint,
            api_key=transcription_key,
        )

        chat_client = AzureOpenAI(
            api_version=chat_api_version,
            azure_endpoint=chat_endpoint,
            api_key=chat_key,
        )

        system_message = "You are an AI assistant for a produce supplier company."

        # Download audio file
        file_url = "https://github.com/MicrosoftLearning/mslearn-ai-language/raw/refs/heads/main/Labfiles/09-audio-chat/data/avocados.mp3"
        audio_file = "avocados.mp3"
        response = requests.get(file_url)
        response.raise_for_status()
        with open(audio_file, "wb") as f:
            f.write(response.content)

        while True:
            prompt = input("\nAsk a question about the audio\n(or type 'quit' to exit)\n")
            if prompt.lower() == "quit":
                break
            elif len(prompt) == 0:
                print("Please enter a question.\n")
            else:
                print("Getting a response ...\n")

                # Step 1: Transcribe audio using transcription model
                with open(audio_file, "rb") as f:
                    transcription = transcription_client.audio.transcriptions.create(
                        model="gpt-4o-mini-transcribe",  # or "whisper-1"
                        file=f
                    )

                # Step 2: Use transcription text in chat model
                response = chat_client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": system_message},
                        {"role": "user", "content": f"{prompt}\n\nTranscribed audio: {transcription.text}"}
                    ]
                )

                print(response.choices[0].message.content)

    except Exception as ex:
        print(ex)


if __name__ == '__main__': 
    main()

