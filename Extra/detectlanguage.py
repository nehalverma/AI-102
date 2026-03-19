from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint=""
key=""

client=TextAnalyticsClient(endpoint=endpoint,credential=AzureKeyCredential(key))

documents=[
    "I enjoy learning about cloud computing.",
    "Heute ist das Wetter sehr schön."
]

response=client.detect_language(documents=documents)

# print(response)

# output in pretty way
import json

pretty_output = []

for doc in response:
    pretty_output.append({
        "id": doc.id,
        "language": doc.primary_language.name,
        "language_code": doc.primary_language.iso6391_name,
        "confidence": doc.primary_language.confidence_score
    })

print(json.dumps(pretty_output, indent=2))
