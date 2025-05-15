yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose down
[+] Running 2/2
 ✔ Container avatar-avatar-app-1  Removed                                                                                                                               0.0s 
 ✔ Network avatar_default         Removed                                                                                                                               0.2s 
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose up -d --build --remove-orphans
Compose can now delegate builds to bake for better performance.
 To do so, set COMPOSE_BAKE=true.
[+] Building 2689.0s (28/28) FINISHED                                                                                                                         docker:default
 => [avatar-app internal] load build definition from dockerfile                                                                                                         0.0s
 => => transferring dockerfile: 2.22kB                                                                                                                                  0.0s
 => [avatar-app internal] load metadata for docker.io/nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04                                                                     1.2s
 => [avatar-app internal] load .dockerignore                                                                                                                            0.0s
 => => transferring context: 2B                                                                                                                                         0.0s
 => [avatar-app internal] load build context                                                                                                                            0.0s
 => => transferring context: 7.56kB                                                                                                                                     0.0s
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
 => [avatar-app 12/22] COPY API.py inference.py lipsync.py lipsync_test.py Wav2Lip_inference_patched.py requirements.txt /home/docker/                                  0.1s
 => [avatar-app 13/22] COPY Wav2Lip/ /home/docker/Wav2Lip/                                                                                                              0.0s
 => [avatar-app 14/22] COPY source/ /home/docker/source/                                                                                                                0.0s
 => [avatar-app 15/22] COPY weights/ /home/docker/weights/                                                                                                              0.9s
 => [avatar-app 16/22] RUN chown -R docker:docker /home/docker                                                                                                          1.2s
 => [avatar-app 17/22] RUN python3 -m venv /home/docker/venv                                                                                                            4.1s
 => [avatar-app 18/22] RUN /home/docker/venv/bin/pip install --no-cache-dir --upgrade pip                                                                               4.1s
 => [avatar-app 19/22] RUN /home/docker/venv/bin/pip install --no-cache-dir -r requirements.txt                                                                      2569.7s
 => [avatar-app 20/22] RUN /home/docker/venv/bin/pip install --no-cache-dir gunicorn                                                                                    1.2s
 => [avatar-app 21/22] RUN chown -R docker:docker /home/docker /home/docker/venv                                                                                       36.2s
 => [avatar-app 22/22] RUN chmod -R u+rwX /home/docker /home/docker/venv                                                                                               36.8s
 => [avatar-app] exporting to image                                                                                                                                    33.3s
 => => exporting layers                                                                                                                                                33.3s
 => => writing image sha256:351e3c4f65e17f0ebb253803c306b758e8afa3441488506dd0efe46856d3e48e                                                                            0.0s
 => => naming to docker.io/library/avatar-app                                                                                                                           0.0s
 => [avatar-app] resolving provenance for metadata file                                                                                                                 0.0s
[+] Running 3/3
 ✔ avatar-app                     Built                                                                                                                                 0.0s 
 ✔ Network avatar_default         Created                                                                                                                               0.0s 
 ✔ Container avatar-avatar-app-1  Started                                                                                                                               0.5s 
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose logs
avatar-app-1  | 
avatar-app-1  | ==========
avatar-app-1  | == CUDA ==
avatar-app-1  | ==========
avatar-app-1  | 
avatar-app-1  | CUDA Version 11.8.0
avatar-app-1  | 
avatar-app-1  | Container image Copyright (c) 2016-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
avatar-app-1  | 
avatar-app-1  | This container image and its contents are governed by the NVIDIA Deep Learning Container License.
avatar-app-1  | By pulling and using the container, you accept the terms and conditions of this license:
avatar-app-1  | https://developer.nvidia.com/ngc/nvidia-deep-learning-container-license
avatar-app-1  | 
avatar-app-1  | A copy of this license is made available in this container at /NGC-DL-CONTAINER-LICENSE for your convenience.
avatar-app-1  | 
avatar-app-1  | 
avatar-app-1  | ==========
avatar-app-1  | == CUDA ==
avatar-app-1  | ==========
avatar-app-1  | 
avatar-app-1  | CUDA Version 11.8.0
avatar-app-1  | 
avatar-app-1  | Container image Copyright (c) 2016-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
avatar-app-1  | 
avatar-app-1  | This container image and its contents are governed by the NVIDIA Deep Learning Container License.
avatar-app-1  | By pulling and using the container, you accept the terms and conditions of this license:
avatar-app-1  | https://developer.nvidia.com/ngc/nvidia-deep-learning-container-license
avatar-app-1  | 
avatar-app-1  | A copy of this license is made available in this container at /NGC-DL-CONTAINER-LICENSE for your convenience.
avatar-app-1  | 
avatar-app-1  | 
avatar-app-1  | ==========
avatar-app-1  | == CUDA ==
avatar-app-1  | ==========
avatar-app-1  | 
avatar-app-1  | CUDA Version 11.8.0
avatar-app-1  | 
avatar-app-1  | Container image Copyright (c) 2016-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
avatar-app-1  | 
avatar-app-1  | This container image and its contents are governed by the NVIDIA Deep Learning Container License.
avatar-app-1  | By pulling and using the container, you accept the terms and conditions of this license:
avatar-app-1  | https://developer.nvidia.com/ngc/nvidia-deep-learning-container-license
avatar-app-1  | 
avatar-app-1  | A copy of this license is made available in this container at /NGC-DL-CONTAINER-LICENSE for your convenience.
avatar-app-1  | 
avatar-app-1  | 
avatar-app-1  | ==========
avatar-app-1  | == CUDA ==
avatar-app-1  | ==========
avatar-app-1  | 
avatar-app-1  | CUDA Version 11.8.0
avatar-app-1  | 
avatar-app-1  | Container image Copyright (c) 2016-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
avatar-app-1  | 
avatar-app-1  | This container image and its contents are governed by the NVIDIA Deep Learning Container License.
avatar-app-1  | By pulling and using the container, you accept the terms and conditions of this license:
avatar-app-1  | https://developer.nvidia.com/ngc/nvidia-deep-learning-container-license
avatar-app-1  | 
avatar-app-1  | A copy of this license is made available in this container at /NGC-DL-CONTAINER-LICENSE for your convenience.
avatar-app-1  | 
avatar-app-1  | 
avatar-app-1  | ==========
avatar-app-1  | == CUDA ==
avatar-app-1  | ==========
avatar-app-1  | 
avatar-app-1  | CUDA Version 11.8.0
avatar-app-1  | 
avatar-app-1  | Container image Copyright (c) 2016-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
avatar-app-1  | 
avatar-app-1  | This container image and its contents are governed by the NVIDIA Deep Learning Container License.
avatar-app-1  | By pulling and using the container, you accept the terms and conditions of this license:
avatar-app-1  | https://developer.nvidia.com/ngc/nvidia-deep-learning-container-license
avatar-app-1  | 
avatar-app-1  | A copy of this license is made available in this container at /NGC-DL-CONTAINER-LICENSE for your convenience.
avatar-app-1  | 
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose up -d 
[+] Running 1/1
 ✔ Container avatar-avatar-app-1  Started                                                                                                                               0.0s 
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ 
