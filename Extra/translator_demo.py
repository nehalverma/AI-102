from azure.ai.translation.text import TextTranslationClient,TranslatorCredential
from azure.ai.translation.text.models import InputTextItem

endpoint=""
key=""
region="eastus"

credential=TranslatorCredential(key,region)
client=TextTranslationClient(endpoint=endpoint,credential=credential)

source_language="it"
target_language=["en"]

input_txt="Il futuro appartiene a chi è disposto a imparare, adattarsi e innovare."

documents=[InputTextItem(text=input_txt)]

response=client.translate(content=documents,to=target_language,from_parameter=source_language)

print(f"Translated Text : {response[0].translations}")