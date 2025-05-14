yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose up -d --build --remove-orphans
Compose can now delegate builds to bake for better performance.
 To do so, set COMPOSE_BAKE=true.
[+] Building 1646.3s (28/28) FINISHED                                                                                                                         docker:default
 => [avatar-app internal] load build definition from dockerfile                                                                                                         0.0s
 => => transferring dockerfile: 2.25kB                                                                                                                                  0.0s
 => [avatar-app internal] load metadata for docker.io/nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04                                                                     0.5s
 => [avatar-app internal] load .dockerignore                                                                                                                            0.0s
 => => transferring context: 2B                                                                                                                                         0.0s
 => [avatar-app internal] load build context                                                                                                                            0.0s
 => => transferring context: 7.53kB                                                                                                                                     0.0s
 => CACHED [avatar-app  1/22] FROM docker.io/nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04@sha256:c2336dadc71ae5b5ce490a55cc0100d876287d28f429a5d2840c8a3a8e86fef0      0.0s
 => [avatar-app  2/22] RUN apt-get update && apt-get install -y     software-properties-common     && rm -rf /var/lib/apt/lists/*                                      43.8s
 => [avatar-app  3/22] RUN add-apt-repository ppa:deadsnakes/ppa -y                                                                                                    22.0s 
 => [avatar-app  4/22] RUN apt-get update && apt-get install -y     python3.10     python3.10-venv     python3.10-distutils     python3-pip     && rm -rf /var/lib/ap  54.7s 
 => [avatar-app  5/22] RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1                                                                 0.2s 
 => [avatar-app  6/22] RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.10 1                                                                   0.3s 
 => [avatar-app  7/22] RUN python3.10 -m ensurepip --upgrade                                                                                                            4.2s 
 => [avatar-app  8/22] RUN python3.10 -m pip install --upgrade pip                                                                                                      4.0s 
 => [avatar-app  9/22] RUN useradd -m -s /bin/bash docker                                                                                                               0.3s 
 => [avatar-app 10/22] WORKDIR /home/docker                                                                                                                             0.0s 
 => [avatar-app 11/22] RUN mkdir -p /home/docker/Wav2Lip /home/docker/source /home/docker/videos /home/docker/weights                                                   0.2s 
 => [avatar-app 12/22] COPY API.py inference.py lipsync.py lipsync_test.py Wav2Lip_inference_patched.py requirements.txt /home/docker/                                  0.1s
 => [avatar-app 13/22] COPY Wav2Lip/ /home/docker/Wav2Lip/                                                                                                              0.0s
 => [avatar-app 14/22] COPY source/ /home/docker/source/                                                                                                                0.0s
 => [avatar-app 15/22] COPY weights/ /home/docker/weights/                                                                                                              1.1s
 => [avatar-app 16/22] RUN chown -R docker:docker /home/docker                                                                                                          1.4s
 => [avatar-app 17/22] RUN python3 -m venv /home/docker/venv                                                                                                            4.2s
 => [avatar-app 18/22] RUN /home/docker/venv/bin/pip install --no-cache-dir --upgrade pip                                                                               4.0s
 => [avatar-app 19/22] RUN /home/docker/venv/bin/pip install --no-cache-dir -r requirements.txt                                                                      1372.7s
 => [avatar-app 20/22] RUN /home/docker/venv/bin/pip install --no-cache-dir gunicorn                                                                                    1.3s
 => [avatar-app 21/22] RUN chown -R docker:docker /home/docker /home/docker/venv                                                                                       43.0s
 => [avatar-app 22/22] RUN chmod -R u+rwX /home/docker /home/docker/venv                                                                                               49.3s
 => [avatar-app] exporting to image                                                                                                                                    38.7s
 => => exporting layers                                                                                                                                                38.7s
 => => writing image sha256:df64508035f7db741b450764d251f18a675bb1502a04ffa2e1d2200adce262ba                                                                            0.0s
 => => naming to docker.io/library/avatar-app                                                                                                                           0.0s
 => [avatar-app] resolving provenance for metadata file                                                                                                                 0.0s
[+] Running 1/2
 ✔ avatar-app                     Built                                                                                                                                 0.0s 
 ⠧ Container avatar-avatar-app-1  Starting                                                                                                                              0.7s 
Error response from daemon: failed to set up container networking: driver failed programming external connectivity on endpoint avatar-avatar-app-1 (f8a30e4fb223afda6312a535cae33cf3e42d753e9a13bb9819788213028092f2): failed to bind host port for 0.0.0.0:8000:172.31.0.2:8000/tcp: address already in use
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose logs
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose up -d 
[+] Running 0/1
 ⠼ Container avatar-avatar-app-1  Starting                                                                                                                              0.5s 
Error response from daemon: failed to set up container networking: driver failed programming external connectivity on endpoint avatar-avatar-app-1 (3c65aaad1d5e3da5446875ef4e64346e185b6c2256114c91844ce81b7f26d60c): failed to bind host port for 0.0.0.0:9036:172.31.0.2:9036/tcp: address already in use
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose down
[+] Running 2/2
 ✔ Container avatar-avatar-app-1  Removed                                                                                                                               0.0s 
 ✔ Network avatar_default         Removed                                                                                                                               0.2s 
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose up -d 
[+] Running 1/2
 ✔ Network avatar_default         Created                                                                                                                               0.1s 
 ⠴ Container avatar-avatar-app-1  Starting                                                                                                                              0.5s 
Error response from daemon: failed to set up container networking: driver failed programming external connectivity on endpoint avatar-avatar-app-1 (156864fc9932806f71133ca1efaeda528a755cb60fd7c4249dc355f483b145e9): failed to bind host port for 0.0.0.0:9036:172.25.0.2:9036/tcp: address already in use
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose down
[+] Running 2/2
 ✔ Container avatar-avatar-app-1  Removed                                                                                                                               0.0s 
 ✔ Network avatar_default         Removed                                                                                                                               0.2s 
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose up -d --build --remove-orphans
Compose can now delegate builds to bake for better performance.
 To do so, set COMPOSE_BAKE=true.
[+] Building 0.6s (28/28) FINISHED                                                                                                                            docker:default
 => [avatar-app internal] load build definition from dockerfile                                                                                                         0.0s
 => => transferring dockerfile: 2.25kB                                                                                                                                  0.0s
 => [avatar-app internal] load metadata for docker.io/nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04                                                                     0.5s
 => [avatar-app internal] load .dockerignore                                                                                                                            0.0s
 => => transferring context: 2B                                                                                                                                         0.0s
 => [avatar-app internal] load build context                                                                                                                            0.0s
 => => transferring context: 7.33kB                                                                                                                                     0.0s
 => [avatar-app  1/22] FROM docker.io/nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04@sha256:c2336dadc71ae5b5ce490a55cc0100d876287d28f429a5d2840c8a3a8e86fef0             0.0s
 => CACHED [avatar-app  2/22] RUN apt-get update && apt-get install -y     software-properties-common     && rm -rf /var/lib/apt/lists/*                                0.0s
 => CACHED [avatar-app  3/22] RUN add-apt-repository ppa:deadsnakes/ppa -y                                                                                              0.0s
 => CACHED [avatar-app  4/22] RUN apt-get update && apt-get install -y     python3.10     python3.10-venv     python3.10-distutils     python3-pip     && rm -rf /var/  0.0s
 => CACHED [avatar-app  5/22] RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1                                                          0.0s
 => CACHED [avatar-app  6/22] RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.10 1                                                            0.0s
 => CACHED [avatar-app  7/22] RUN python3.10 -m ensurepip --upgrade                                                                                                     0.0s
 => CACHED [avatar-app  8/22] RUN python3.10 -m pip install --upgrade pip                                                                                               0.0s
 => CACHED [avatar-app  9/22] RUN useradd -m -s /bin/bash docker                                                                                                        0.0s
 => CACHED [avatar-app 10/22] WORKDIR /home/docker                                                                                                                      0.0s
 => CACHED [avatar-app 11/22] RUN mkdir -p /home/docker/Wav2Lip /home/docker/source /home/docker/videos /home/docker/weights                                            0.0s
 => CACHED [avatar-app 12/22] COPY API.py inference.py lipsync.py lipsync_test.py Wav2Lip_inference_patched.py requirements.txt /home/docker/                           0.0s
 => CACHED [avatar-app 13/22] COPY Wav2Lip/ /home/docker/Wav2Lip/                                                                                                       0.0s
 => CACHED [avatar-app 14/22] COPY source/ /home/docker/source/                                                                                                         0.0s
 => CACHED [avatar-app 15/22] COPY weights/ /home/docker/weights/                                                                                                       0.0s
 => CACHED [avatar-app 16/22] RUN chown -R docker:docker /home/docker                                                                                                   0.0s
 => CACHED [avatar-app 17/22] RUN python3 -m venv /home/docker/venv                                                                                                     0.0s
 => CACHED [avatar-app 18/22] RUN /home/docker/venv/bin/pip install --no-cache-dir --upgrade pip                                                                        0.0s
 => CACHED [avatar-app 19/22] RUN /home/docker/venv/bin/pip install --no-cache-dir -r requirements.txt                                                                  0.0s
 => CACHED [avatar-app 20/22] RUN /home/docker/venv/bin/pip install --no-cache-dir gunicorn                                                                             0.0s
 => CACHED [avatar-app 21/22] RUN chown -R docker:docker /home/docker /home/docker/venv                                                                                 0.0s
 => CACHED [avatar-app 22/22] RUN chmod -R u+rwX /home/docker /home/docker/venv                                                                                         0.0s
 => [avatar-app] exporting to image                                                                                                                                     0.0s
 => => exporting layers                                                                                                                                                 0.0s
 => => writing image sha256:9ec2ca2ae2e34bd5decd4c9a585b2ece82e902033412dd59e8fdd9490485e53b                                                                            0.0s
 => => naming to docker.io/library/avatar-app                                                                                                                           0.0s
 => [avatar-app] resolving provenance for metadata file                                                                                                                 0.0s
[+] Running 2/3
 ✔ avatar-app                     Built                                                                                                                                 0.0s 
 ✔ Network avatar_default         Created                                                                                                                               0.1s 
 ⠼ Container avatar-avatar-app-1  Starting                                                                                                                              0.5s 
Error response from daemon: failed to set up container networking: driver failed programming external connectivity on endpoint avatar-avatar-app-1 (85e8acc0df27d31ee74a1cd1bff43edc51cb79610abfcef26be41c7043e058bd): failed to bind host port for 0.0.0.0:9036:172.25.0.2:9036/tcp: address already in use
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose logs
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ 
