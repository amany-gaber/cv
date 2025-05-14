yaz@gpu:~/tak/GP/AVATAR$ docker compose up -d --build --remove-orphans
WARN[0000] The "GID" variable is not set. Defaulting to a blank string. 
Compose can now delegate builds to bake for better performance.
 To do so, set COMPOSE_BAKE=true.
[+] Building 0.7s (9/16)                                                                                                                                      docker:default
 => [avatar-app internal] load build definition from dockerfile                                                                                                         0.0s
 => => transferring dockerfile: 1.43kB                                                                                                                                  0.0s
 => [avatar-app internal] load metadata for docker.io/library/python:3.10-slim                                                                                          0.5s
 => [avatar-app internal] load .dockerignore                                                                                                                            0.0s
 => => transferring context: 2B                                                                                                                                         0.0s
 => CANCELED [avatar-app  1/12] FROM docker.io/library/python:3.10-slim@sha256:e1013c40c02a7875ae30c78c69b68ea7bee31713e8ac1c0f5469c1206258d6d7                         0.0s
 => => resolve docker.io/library/python:3.10-slim@sha256:e1013c40c02a7875ae30c78c69b68ea7bee31713e8ac1c0f5469c1206258d6d7                                               0.0s
 => => sha256:e1013c40c02a7875ae30c78c69b68ea7bee31713e8ac1c0f5469c1206258d6d7 9.13kB / 9.13kB                                                                          0.0s
 => => sha256:4fc77722db8bd186386ebfe056989b2ba1c8a602ef1c46ec461fa49a9bb4c667 1.75kB / 1.75kB                                                                          0.0s
 => => sha256:abe836e1b93b4b373cd684fa406a4dea9920e7420349e7747b869e3522f06f1c 5.37kB / 5.37kB                                                                          0.0s
 => [avatar-app internal] load build context                                                                                                                            0.0s
 => => transferring context: 38B                                                                                                                                        0.0s
 => CACHED [avatar-app  2/12] RUN useradd -m -s /bin/bash docker                                                                                                        0.0s
 => CACHED [avatar-app  3/12] WORKDIR /home/docker                                                                                                                      0.0s
 => CACHED [avatar-app  4/12] RUN mkdir -p /home/docker/app                                                                                                             0.0s
 => ERROR [avatar-app  5/12] COPY ./app /home/docker/app                                                                                                                0.0s
------
 > [avatar-app  5/12] COPY ./app /home/docker/app:
------
failed to solve: failed to compute cache key: failed to calculate checksum of ref d2d47a88-b07d-466b-8ece-43836925ba61::y8owu6p643if5lxt3z24h8o1u: "/app": not found
yaz@gpu:~/tak/GP/AVATAR$ ls
API.py  docker-compose.yml  inference.py  lipsync_test.py  requirements.txt  videos   Wav2Lip_inference_patched.py
cache   dockerfile          lipsync.py    __pycache__      source            Wav2Lip  weights
yaz@gpu:~/tak/GP/AVATAR$ cd videos
yaz@gpu:~/tak/GP/AVATAR/videos$ ls
yaz@gpu:~/tak/GP/AVATAR/videos$ cd ..
yaz@gpu:~/tak/GP/AVATAR$ cd source
yaz@gpu:~/tak/GP/AVATAR/source$ ls
audio.wav  final.mp4
yaz@gpu:~/tak/GP/AVATAR/source$ cd ..
yaz@gpu:~/tak/GP/AVATAR$ cd Wav2Lip
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip$ ls
audio.py     color_syncnet_train.py  face_detection  hparams.py           inference.py       models         __pycache__  requirements.txt  temp
checkpoints  evaluation              filelists       hq_wav2lip_train.py  inference.py.save  preprocess.py  README.md    results           wav2lip_train.py
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip$ cd ..
yaz@gpu:~/tak/GP/AVATAR$ cd Wav2Lip
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip$ ls
audio.py     color_syncnet_train.py  face_detection  hparams.py           inference.py       models         __pycache__  requirements.txt  temp
checkpoints  evaluation              filelists       hq_wav2lip_train.py  inference.py.save  preprocess.py  README.md    results           wav2lip_train.py
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip$ cd face_detection
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/face_detection$ ls
api.py  detection  __init__.py  models.py  __pycache__  README.md  utils.py
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/face_detection$ cd ..
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip$ cd models
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ ls
conv.py  __init__.py  __pycache__  syncnet.py  wav2lip.py
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ 
