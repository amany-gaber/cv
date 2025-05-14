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
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose up -d --build --remove-orphans
WARN[0000] /home/yaz/tak/GP/AVATAR/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
Compose can now delegate builds to bake for better performance.
 To do so, set COMPOSE_BAKE=true.
[+] Building 1167.7s (17/19)                                                                                                                                  docker:default
 => [avatar-app internal] load build definition from dockerfile                                                                                                         0.0s
 => => transferring dockerfile: 1.51kB                                                                                                                                  0.0s
 => [avatar-app internal] load metadata for docker.io/library/python:3.10-slim                                                                                          0.5s
 => [avatar-app internal] load .dockerignore                                                                                                                            0.0s
 => => transferring context: 2B                                                                                                                                         0.0s
 => [avatar-app  1/15] FROM docker.io/library/python:3.10-slim@sha256:e1013c40c02a7875ae30c78c69b68ea7bee31713e8ac1c0f5469c1206258d6d7                                  9.1s
 => => resolve docker.io/library/python:3.10-slim@sha256:e1013c40c02a7875ae30c78c69b68ea7bee31713e8ac1c0f5469c1206258d6d7                                               0.0s
 => => sha256:5d66a27e733ac4f56a6f6669d01e6aed278e72919f683a73238cdf2ef90dbd31 249B / 249B                                                                              0.5s
 => => sha256:e1013c40c02a7875ae30c78c69b68ea7bee31713e8ac1c0f5469c1206258d6d7 9.13kB / 9.13kB                                                                          0.0s
 => => sha256:4fc77722db8bd186386ebfe056989b2ba1c8a602ef1c46ec461fa49a9bb4c667 1.75kB / 1.75kB                                                                          0.0s
 => => sha256:abe836e1b93b4b373cd684fa406a4dea9920e7420349e7747b869e3522f06f1c 5.37kB / 5.37kB                                                                          0.0s
 => => sha256:5e3380732964a9fa4272d7d4ab36e5b9f132b331f3bdbb80c3b6e55fb8cc6be2 3.51MB / 3.51MB                                                                          2.9s
 => => sha256:5cc9686f2aa90263bd53a0ee75237af8b54c307b443c5185997aaab2bfa07f73 15.65MB / 15.65MB                                                                        8.3s
 => => extracting sha256:5e3380732964a9fa4272d7d4ab36e5b9f132b331f3bdbb80c3b6e55fb8cc6be2                                                                               0.2s
 => => extracting sha256:5cc9686f2aa90263bd53a0ee75237af8b54c307b443c5185997aaab2bfa07f73                                                                               0.7s
 => => extracting sha256:5d66a27e733ac4f56a6f6669d01e6aed278e72919f683a73238cdf2ef90dbd31                                                                               0.0s
 => [avatar-app internal] load build context                                                                                                                            2.8s
 => => transferring context: 440.95MB                                                                                                                                   2.8s
 => [avatar-app  2/15] RUN useradd -m -s /bin/bash docker                                                                                                               0.9s
 => [avatar-app  3/15] WORKDIR /home/docker                                                                                                                             0.0s
 => [avatar-app  4/15] RUN mkdir -p /home/docker/Wav2Lip /home/docker/source /home/docker/videos /home/docker/weights                                                   0.2s
 => [avatar-app  5/15] COPY API.py inference.py lipsync.py lipsync_test.py Wav2Lip_inference_patched.py requirements.txt /home/docker/                                  0.1s
 => [avatar-app  6/15] COPY Wav2Lip/ /home/docker/Wav2Lip/                                                                                                              0.0s
 => [avatar-app  7/15] COPY source/ /home/docker/source/                                                                                                                0.0s
 => [avatar-app  8/15] COPY weights/ /home/docker/weights/                                                                                                              1.0s
 => [avatar-app  9/15] RUN chown -R docker:docker /home/docker                                                                                                          1.3s
 => [avatar-app 10/15] RUN python -m venv /home/docker/venv                                                                                                             5.0s
 => [avatar-app 11/15] RUN /home/docker/venv/bin/pip install --no-cache-dir --upgrade pip                                                                               4.5s
 => [avatar-app 12/15] RUN /home/docker/venv/bin/pip install --no-cache-dir -r requirements.txt                                                                      1136.8s
 => ERROR [avatar-app 13/15] RUN /home/docker/venv/bin/pip install --no-cache-dir -r Wav2Lip/requirements.txt                                                           8.2s
------
 > [avatar-app 13/15] RUN /home/docker/venv/bin/pip install --no-cache-dir -r Wav2Lip/requirements.txt:
1.352 Collecting librosa==0.7.0 (from -r Wav2Lip/requirements.txt (line 1))
1.566   Downloading librosa-0.7.0.tar.gz (1.6 MB)
2.228      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 2.6 MB/s eta 0:00:00
2.276   Preparing metadata (setup.py): started
2.926   Preparing metadata (setup.py): finished with status 'done'
3.357 Collecting numpy==1.17.1 (from -r Wav2Lip/requirements.txt (line 2))
3.403   Downloading numpy-1.17.1.zip (6.5 MB)
5.942      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.5/6.5 MB 2.6 MB/s eta 0:00:00
6.290   Preparing metadata (setup.py): started
6.970   Preparing metadata (setup.py): finished with status 'done'
7.139 Collecting opencv-contrib-python>=4.2.0.34 (from -r Wav2Lip/requirements.txt (line 3))
7.186   Downloading opencv_contrib_python-4.11.0.86-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (20 kB)
7.403 ERROR: Ignored the following yanked versions: 3.4.11.39, 3.4.17.61, 4.4.0.42, 4.4.0.44, 4.5.4.58, 4.5.5.62, 4.7.0.68
7.403 ERROR: Could not find a version that satisfies the requirement opencv-python==4.1.0.25 (from versions: 3.4.0.14, 3.4.10.37, 3.4.11.41, 3.4.11.43, 3.4.11.45, 3.4.13.47, 3.4.15.55, 3.4.16.57, 3.4.16.59, 3.4.17.63, 3.4.18.65, 4.3.0.38, 4.4.0.40, 4.4.0.46, 4.5.1.48, 4.5.3.56, 4.5.4.60, 4.5.5.64, 4.6.0.66, 4.7.0.72, 4.8.0.74, 4.8.0.76, 4.8.1.78, 4.9.0.80, 4.10.0.82, 4.10.0.84, 4.11.0.86)
7.690 ERROR: No matching distribution found for opencv-python==4.1.0.25
------
failed to solve: process "/bin/sh -c /home/docker/venv/bin/pip install --no-cache-dir -r Wav2Lip/requirements.txt" did not complete successfully: exit code: 1
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ 
