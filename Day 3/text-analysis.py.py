from dotenv import load_dotenv
import os

# Import namespaces
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient, ExtractiveSummaryAction


# -----------------------------
# Summarization Function
# -----------------------------
def summarize_text(ai_client, text):
    poller = ai_client.begin_analyze_actions(
        documents=[text],
        actions=[ExtractiveSummaryAction(max_sentence_count=3)]
    )

    results = poller.result()

    print("\nSummary:")
    for doc in results:
        for action_result in doc:
            for sentence in action_result.sentences:
                print("-", sentence.text)


# -----------------------------
# PII Detection Function
# -----------------------------
def detect_pii(ai_client, text):
    pii_result = ai_client.recognize_pii_entities(documents=[text])[0]

    print("\nPII Entities:")
    for entity in pii_result.entities:
        print(f"- {entity.text} ({entity.category})")


# -----------------------------
# Main Function
# -----------------------------
def main():
    try:
        # Get Configuration Settings
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')

        # Create client
        credential = AzureKeyCredential(ai_key)
        ai_client = TextAnalyticsClient(endpoint=ai_endpoint, credential=credential)

        # Analyze each text file
        reviews_folder = 'reviews'
        for file_name in os.listdir(reviews_folder):

            print('\n-------------\n' + file_name)
            text = open(os.path.join(reviews_folder, file_name), encoding='utf8').read()
            print('\n' + text)

            # Language
            detectedLanguage = ai_client.detect_language(documents=[text])[0]
            print('\nLanguage:', detectedLanguage.primary_language.name)

            # Sentiment
            sentimentAnalysis = ai_client.analyze_sentiment(documents=[text])[0]
            print("\nSentiment:", sentimentAnalysis.sentiment)

            # Key Phrases
            phrases = ai_client.extract_key_phrases(documents=[text])[0].key_phrases
            if phrases:
                print("\nKey Phrases:")
                for phrase in phrases:
                    print("\t", phrase)

            # Entities
            entities = ai_client.recognize_entities(documents=[text])[0].entities
            if entities:
                print("\nEntities:")
                for entity in entities:
                    print(f"\t{entity.text} ({entity.category})")

            # Linked Entities
            linked_entities = ai_client.recognize_linked_entities(documents=[text])[0].entities
            if linked_entities:
                print("\nLinks:")
                for item in linked_entities:
                    print(f"\t{item.name} ({item.url})")

            # Summarization
            summarize_text(ai_client, text)

            # PII Detection
            detect_pii(ai_client, text)

    except Exception as ex:
        print("\nERROR:", ex)


if __name__ == "__main__":
    main()
