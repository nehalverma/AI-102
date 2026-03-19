from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint=""
key=""

client=TextAnalyticsClient(endpoint=endpoint,credential=AzureKeyCredential(key))

documents = [
    "Artificial intelligence and machine learning are driving major changes across healthcare, finance, and education by improving efficiency and revealing deeper insights from data.",
    "AI and ML technologies are transforming how industries operate, from automating routine tasks to supporting smarter decision-making in areas like medicine, banking, and learning."
]

response=client.extract_key_phrases(documents=documents)[0]

for key_phrase in response.key_phrases:
    print(key_phrase)