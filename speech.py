import azure.cognitiveservices.speech as speechsdk

speech_config = speechsdk.SpeechConfig(subscription="a307da45112a4384a70b8e0f68b47da5", region="eastus")
# Note: if only language is set, the default voice of that language is chosen.
speech_config.speech_synthesis_language = "en-US" # For example, "de-DE"
# The voice setting will overwrite the language setting.
# The voice setting will not overwrite the voice element in input SSML.
speech_config.speech_synthesis_voice_name ="en-US-AriaNeural"
text=input("Input a text to make audio:\n")
audio_config = speechsdk.audio.AudioOutputConfig(filename="a.wav")
synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
synthesizer.speak_text_async(text)
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)
result = synthesizer.speak_text_async("Getting the response as an in-memory stream.").get()