from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem

endpoint=""
key=""
region = "eastus"

credential = TranslatorCredential(key, region)
client = TextTranslationClient(endpoint=endpoint, credential=credential)

# -----------------------------------------
# Input Text is Italian
# -----------------------------------------
input_text = "Il futuro appartiene a chi è disposto a imparare, adattarsi e innovare."
# input_text = "This damn system is really stupid sometimes."
documents = [InputTextItem(text=input_text)]

# -----------------------------------------
# 1️⃣ Detection
# -----------------------------------------
detect_response = client.translate(
    content=documents,
    to=["en"]  # required even for detection
)

detected_language = detect_response[0].detected_language.language
print("Detected Language:", detected_language)

# -----------------------------------------
# 2️⃣ One-to-Many Translation
# -----------------------------------------
translate_response = client.translate(
    content=documents,
    to=["en", "fr", "de"],
    include_alignment=True,
    include_sentence_length=True,
    profanity_action="Marked"  # Options: NoAction, Marked, Deleted
)

print("\nTranslations:")
for translation in translate_response[0].translations:
    print(f"\nLanguage: {translation.to}")
    print("Text:", translation.text)

    # Word alignment
    print("Alignment:", translation.alignment.proj if translation.alignment else "N/A")

    # Sentence length
    print("Sentence Length:", translation.sent_len if hasattr(translation, "sent_len") else "N/A")

# -----------------------------------------
# 3️⃣ Transliteration
# -----------------------------------------
translit_text = "नमस्ते दुनिया"
translit_documents = [InputTextItem(text=translit_text)]

translit_response = client.transliterate(
    content=translit_documents,
    language="hi",
    from_script="Deva",
    to_script="Latn"
)

print("\nTransliteration:")
print(translit_response[0].text)