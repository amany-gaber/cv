/opt/nvidia/nvidia_entrypoint.sh: line 67: exec: gunicorn: not found
yaz@gpu:~/tak/GP/AVATAR$ ls
API.py  docker-compose.yml  inference.py  lipsync_test.py  requirements.txt  videos   Wav2Lip_inference_patched.py
cache   dockerfile          lipsync.py    __pycache__      source            Wav2Lip  weights
yaz@gpu:~/tak/GP/AVATAR$ 






.env
CACHE_DIR=/app/cache
STATIC_VIDEO=/app/source/final.mp4
OUTPUT_VIDEO=/app/result.mp4
UPLOAD_AUDIO_DIR=/app/source
VIDEOS_DIR=/app/videos
CHECKPOINT_PATH=/app/weights/wav2lip.pth
FFMPEG_LOGLEVEL=quiet
API_PORT=4097
EXPOSE_PORT=1236
