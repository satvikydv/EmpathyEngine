from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
import sys
import os

# Add parent dir to sys.path for package resolution
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)

from empathy_engine.core.emotion_analyzer import EmotionAnalyzer
from empathy_engine.core.tts_engine import TTSEngine
import os

app = FastAPI(title="The Empathy Engine")

# Initialize Core Modules
emotion_analyzer = EmotionAnalyzer()
tts_engine = TTSEngine(output_dir="static/audio")

# Serve static files (API, HTML, CSS, JS, Audio)
app.mount("/static", StaticFiles(directory="static"), name="static")

class TextPayload(BaseModel):
    text: str

@app.get("/")
async def read_root():
    return FileResponse("static/index.html")

@app.post("/api/analyze")
async def analyze_sentiment(payload: TextPayload):
    """
    Analyzes the sentiment of the input text.
    """
    emotion = emotion_analyzer.analyze(payload.text)
    details = emotion_analyzer.get_details(payload.text)
    return {"emotion": emotion, "details": details}

@app.post("/api/speak")
async def generate_speech(payload: TextPayload):
    """
    Analyzes sentiment and generates audio with modulated voice parameters.
    """
    try:
        emotion = emotion_analyzer.analyze(payload.text)
        audio_path = tts_engine.generate_audio(payload.text, emotion)
        
        relative_path = audio_path.replace("\\", "/") 
        
        return {
            "emotion": emotion,
            "audio_url": f"/{relative_path}",
            "message": "Audio generated successfully"
        }
    except Exception as e:
        print(f"TTS Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
