

import openai

openai.api_key = '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'

audio_file = open('5872dae0-5b0b-4684-9c9e-9d619cb927fc.wav', 'rb')
transcript = openai.Audio.transcribe('whisper-1', audio_file)

print(transcript.text)