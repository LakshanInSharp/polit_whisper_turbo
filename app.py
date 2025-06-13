from fastapi import FastAPI, File, UploadFile
import whisper
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
   CORSMiddleware,
   allow_origins=["*"],  # :white_check_mark: Allow React frontend
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
 )


# Loading Whisper model once when the server starts
model = whisper.load_model("turbo")

@app.post("/transcribe")
async def transcribe_audio(audio: UploadFile = File(...)):
    """API endpoint to transcribe a .wav file to text."""
    if audio.content_type not in ["audio/wav"]:
        return {"error": "Invalid file format. Please upload a .wav file."}

    # Save uploaded file temporarily
    with open("temp.wav", "wb") as f:
        f.write(await audio.read())    

    # Transcribe
    result = model.transcribe("temp.wav")
    return {"transcription": result["text"]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
