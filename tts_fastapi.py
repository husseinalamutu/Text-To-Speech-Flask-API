from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from gtts import gTTS

app = FastAPI()

# Define request body model
class TextRequest(BaseModel):
    text: str

@app.post("/speak")
async def speak(request: TextRequest):
    tts = gTTS(text=request.text, lang='en')
    tts.save("output.mp3")
    return FileResponse("output.mp3", media_type="audio/mpeg", filename="output.mp3")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)