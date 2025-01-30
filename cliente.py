import sounddevice as sd
import numpy as np
import wave
import requests

# Configurações
DURATION = 10  # Segundos de gravação
SAMPLERATE = 44100
FILENAME = "meu_audio.wav"
SERVER_URL = "http://localhost:8000/transcribe/"

def gravar_audio(filename):
    """Grava áudio do microfone e salva em um arquivo"""
    print("🎙 Gravando... Fale agora!")
    audio = sd.rec(int(DURATION * SAMPLERATE), samplerate=SAMPLERATE, channels=1, dtype=np.int16)
    sd.wait()
    print("✅ Gravação concluída!")

    # Salvar como WAV
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLERATE)
        wf.writeframes(audio.tobytes())

def enviar_audio(filename):
    """Envia o arquivo de áudio para o servidor FastAPI"""
    with open(filename, "rb") as f:
        files = {"file": (filename, f, "audio/wav")}
        response = requests.post(SERVER_URL, files=files)
    
    if response.status_code == 200:
        print("📝 Transcrição:\n", response.json()["transcription"])
    else:
        print("❌ Erro ao transcrever áudio")

# Gravar e enviar áudio
gravar_audio(FILENAME)
enviar_audio(FILENAME)
