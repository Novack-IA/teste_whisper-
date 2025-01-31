import whisper
import os


model = whisper.load_model("turbo")  

os.makedirs("audios", exist_ok=True)
audio_dir = "/audios"

for file in os.listdir(audio_dir):
    if file.endswith((".mp3", ".wav", ".m4a")): 
        audio_path = os.path.join(audio_dir, file)
        print(f"Transcrevendo: {audio_path}")

        result = model.transcribe(audio_path, language="pt")

        print(f"Transcrição de {file}:")
        print(result["text"])
        print("-" * 50)
