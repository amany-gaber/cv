from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import shutil
import os
import sys
import time
import subprocess
from lipsync import LipSync
import contextlib
import uuid

os.environ['FFMPEG_LOGLEVEL'] = os.getenv('FFMPEG_LOGLEVEL', 'quiet')

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR = os.getenv("CACHE_DIR", os.path.join(BASE_DIR, "cache"))
STATIC_VIDEO = os.getenv("STATIC_VIDEO", os.path.join(BASE_DIR, "source", "final.mp4"))
OUTPUT_VIDEO = os.getenv("OUTPUT_VIDEO", os.path.join(BASE_DIR, "result.mp4"))
UPLOAD_AUDIO_DIR = os.getenv("UPLOAD_AUDIO_DIR", os.path.join(BASE_DIR, "source"))
UPLOAD_AUDIO_PATH = os.path.join(UPLOAD_AUDIO_DIR, "input_audio.wav")
VIDEOS_DIR = os.getenv("VIDEOS_DIR", os.path.join(BASE_DIR, "videos"))

os.makedirs(UPLOAD_AUDIO_DIR, exist_ok=True)
os.makedirs(CACHE_DIR, exist_ok=True)
os.makedirs(VIDEOS_DIR, exist_ok=True)

app.mount("/videos", StaticFiles(directory=VIDEOS_DIR), name="videos")

lip = LipSync(
    model='wav2lip',
    checkpoint_path=os.getenv("CHECKPOINT_PATH", os.path.join(BASE_DIR, "weights", "wav2lip.pth")),
    nosmooth=True,
    device='cuda',
    cache_dir=CACHE_DIR,
    img_size=96,
    save_cache=True,
    ffmpeg_loglevel=os.getenv('FFMPEG_LOGLEVEL', 'quiet'),
    fps=25,
)

@app.post("/sync")
async def sync_audio(request: Request, audio: UploadFile = File(...)):
    try:
        with open(UPLOAD_AUDIO_PATH, "wb") as buffer:
            shutil.copyfileobj(audio.file, buffer)
        
        with open(os.devnull, 'w') as devnull:
            old_stdout = sys.stdout
            old_stderr = sys.stderr
            sys.stdout = devnull
            sys.stderr = devnull
            
            with contextlib.redirect_stdout(devnull), contextlib.redirect_stderr(devnull):
                start_time = time.time()
                
                unique_id = str(uuid.uuid4())
                output_filename = f"{unique_id}.mp4"
                output_path = os.path.join(VIDEOS_DIR, output_filename)
                
                lip.sync(STATIC_VIDEO, UPLOAD_AUDIO_PATH, output_path)
                
                end_time = time.time()
            
            sys.stdout = old_stdout
            sys.stderr = old_stderr
        
        print(f"Execution time: {end_time - start_time:.2f} seconds")
        
        base_url = str(request.base_url).rstrip("/")
        video_url = f"{base_url}/videos/{output_filename}"
        return {"video_url": video_url}
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
