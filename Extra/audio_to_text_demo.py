import azure.cognitiveservices.speech as speechsdk

endpoint=""
key=""

config=speechsdk.SpeechConfig(subscription=key,endpoint=endpoint)

output_file="transcribed.txt"
audio_filename="speech01.wav"
config.speech_recognition_language="en-US"

audio_input = speechsdk.AudioConfig(filename=audio_filename)
txt_generator = speechsdk.SpeechRecognizer(speech_config=config,audio_config=audio_input)

result=txt_generator.recognize_once_async().get()
if result.reason== speechsdk.ResultReason.RecognizedSpeech:
    print("Text generated successfully")
else:
    print("Generating text failed")

with open(output_file, "w", encoding="utf-8") as file:
    file.write(result.text)
