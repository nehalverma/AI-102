import azure.cognitiveservices.speech as speechsdk

endpoint=""
key=""

config=speechsdk.SpeechConfig(subscription=key,endpoint=endpoint)

output_file="speech03.wav"
audio_output = speechsdk.audio.AudioConfig(filename=output_file)
speech_generator = speechsdk.SpeechSynthesizer(speech_config=config,audio_config=audio_output)

with open("config.xml", "r", encoding="utf-8") as file:
    ssml_string = file.read()

result=speech_generator.speak_ssml_async(ssml_string).get()
if result.reason== speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Successfully generated speech")
else:
    print("Speech generation failed")
    cancellation = result.cancellation_details
    print("Reason:", cancellation.reason)
    print("Error details:", cancellation.error_details)

