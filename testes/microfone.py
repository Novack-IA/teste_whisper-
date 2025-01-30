# -*- coding: utf-8 -*-
import os
import sounddevice as sd
import numpy as np
import whisper
import wave

DURATION = 5 
SAMPLERATE = 44100  
model = whisper.load_model("small")

def gravar_audio(filename="meu_audio.wav"):
    # Create 'audios' directory if it doesn't exist
    if not os.path.exists('audios'):
        os.makedirs('audios')
    
    filepath = os.path.join('audios', filename)
    
    print("🎙 Gravando... Fale agora!")
    audio = sd.rec(int(DURATION * SAMPLERATE), samplerate=SAMPLERATE, channels=1, dtype=np.int16)
    sd.wait()  
    print("✅ Gravação concluída!")

    with wave.open(filepath, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2) 
        wf.setframerate(SAMPLERATE)
        wf.writeframes(audio.tobytes())

def transcrever_audio(filename="meu_audio.wav"):
    filepath = os.path.join('audios', filename)
    result = model.transcribe(filepath, language="pt")
    print("📝 Transcrição:\n", result["text"])

gravar_audio()
transcrever_audio()