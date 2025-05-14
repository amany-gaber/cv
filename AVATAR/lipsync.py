import os
import subprocess

class LipSync:
    def __init__(
        self,
        model="wav2lip",
        checkpoint_path="",
        nosmooth=True,
        device="cuda",
        cache_dir="",
        img_size=96,
        save_cache=True,
        ffmpeg_loglevel="quiet",
        fps=25,
    ):
        self.model = model
        self.checkpoint_path = checkpoint_path
        self.nosmooth = nosmooth
        self.device = device
        self.cache_dir = cache_dir
        self.img_size = img_size
        self.save_cache = save_cache
        self.ffmpeg_loglevel = ffmpeg_loglevel
        self.fps = fps
        os.environ['FFMPEG_LOGLEVEL'] = ffmpeg_loglevel

    def sync(self, video_path, audio_path, output_path):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        inference_path = os.path.join(base_dir, "Wav2Lip", "inference.py")
        if not os.path.exists(inference_path):
            inference_path = "/app/Wav2Lip/inference.py"

        cmd = [
            "python", inference_path,
            "--checkpoint_path", self.checkpoint_path,
            "--face", video_path,
            "--audio", audio_path,
            "--outfile", output_path,
            "--fps", str(self.fps),
        ]
        if self.nosmooth:
            cmd.append("--nosmooth")
        
        try:
            subprocess.run(cmd, check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            raise Exception(f"Wav2Lip failed: {e.stderr}")