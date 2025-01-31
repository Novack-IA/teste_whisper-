from fastapi import FastAPI, File, UploadFile
import whisper
import uvicorn
import os

app = FastAPI()

print("🔄 Carregando modelo Whisper...")
model = whisper.load_model("turbo")
print("✅ Modelo carregado!")

@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    """Recebe um áudio, transcreve e retorna o texto"""
    
    temp_audio_path = f"temp_{file.filename}"
    
    with open(temp_audio_path, "wb") as buffer:
        buffer.write(await file.read())

    result = model.transcribe(temp_audio_path, language="pt")

    os.remove(temp_audio_path)

    return {"transcription": result["text"]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
