import whisper
from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import Dict
import os
from uuid import uuid4
from contextlib import asynccontextmanager

# Define a context manager for lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize the Whisper model
    print("Loading Whisper model...")
    model = whisper.load_model(name="turbo", download_root="./models")
    print("Model loaded successfully.")
    
    # Make the model available in the app state
    app.state.model = model
    
    # create a temp dir if it doesn't exist
    if not os.path.exists("./temp"):
        os.makedirs("./temp")

    # Yield to start the app
    yield

    # Cleanup resources if needed
    print("Shutting down the application.")

# Create FastAPI app instance with lifespan handler
app = FastAPI(lifespan=lifespan)

@app.post("/transcribe/", response_model=Dict[str, str])
async def transcribe_audio(file: UploadFile = File(...)):
    # Verify the file type
    #if not file.content_type.startswith("audio/"):
    #    raise HTTPException(status_code=400, detail="The uploaded file is not a valid audio file.")
    
    print("Received audio file:", file.filename)
    _, file_extension = os.path.splitext(file.filename)
    print("File extension:", file_extension)

    # Generate a random file name
    temp_file_path = f"./temp/{uuid4().hex}{file_extension}"

    # Save the file temporarily
    try:
        with open(temp_file_path, "wb") as f:
            f.write(await file.read())
        
        # Access the model from the app state and transcribe the audio
        model = app.state.model
        result = model.transcribe(temp_file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during transcription: {e}")
    finally:
        # Remove the temporary file
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

    # Return the transcription result
    return {"transcription": result["text"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
