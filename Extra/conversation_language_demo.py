
from azure.ai.language.conversations import ConversationAnalysisClient
from azure.core.credentials import AzureKeyCredential

endpoint=""
key=""

client=ConversationAnalysisClient(endpoint=endpoint,credential=AzureKeyCredential(key))

utterance="Do you have free Wi-Fi and a swimming pool?"
project_name="TrainingProject"
deployment_name="TrainedModelDeployment"

response=client.analyze_conversation(
    task={
        "kind": "Conversation",
            "analysisInput": {
                "conversationItem": {
                    "participantId": "1",
                    "id": "1",
                    "modality": "text",
                    "language": "en",
                    "text": utterance 
                },
                "isLoggingEnabled": False
            },
            "parameters": {
                "projectName": project_name,
                "deploymentName": deployment_name
            }
    }
)

# print(response)

# To print the output in pretty way
result = response["result"]["prediction"]

print("\nUser Query:")
print("-", response["result"]["query"])

print("\nTop Intent:")
print("-", result["topIntent"])

print("\nIntent Confidence Scores:")
for intent in result["intents"]:
    print(f"  • {intent['category']}: {intent['confidenceScore']:.2f}")

if result["entities"]:
    print("\nEntities:")
    for entity in result["entities"]:
        print(f"  • {entity}")
else:
    print("\nEntities: None")
