from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint=""
key=""

client=TextAnalyticsClient(endpoint=endpoint,credential=AzureKeyCredential(key))

documents=[
     "The café served delicious meals, and the employees made us feel truly welcome throughout our visit.",
    "My order was damaged on arrival, and the support team offered no meaningful help when I contacted them.",
    "The analysis generated approximately one thousand distinct data entries."
]

response=client.analyze_sentiment(documents=documents)

for result in response:
    print(f"Sentiment: {result.sentences[0].sentiment} - Sentence: {result.sentences[0].text}")
    