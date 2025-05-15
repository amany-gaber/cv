yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose down
[+] Running 2/2
 ✔ Container avatar-avatar-app-1  Removed                                                                                                                               0.0s 
 ✔ Network avatar_default         Removed                                                                                                                               0.3s 
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose up -d --build --remove-orphans
Compose can now delegate builds to bake for better performance.
 To do so, set COMPOSE_BAKE=true.
[+] Building 1.0s (2/2) FINISHED                                                                                                                              docker:default
 => [avatar-app internal] load build definition from dockerfile                                                                                                         0.0s
 => => transferring dockerfile: 2.22kB                                                                                                                                  0.0s
 => ERROR [avatar-app internal] load metadata for docker.io/nvidia/cuda:12.2.0-cudnn8-runtime-Ubuntu20.04                                                               0.9s
------
 > [avatar-app internal] load metadata for docker.io/nvidia/cuda:12.2.0-cudnn8-runtime-Ubuntu20.04:
------
failed to solve: nvidia/cuda:12.2.0-cudnn8-runtime-Ubuntu20.04: failed to resolve source metadata for docker.io/nvidia/cuda:12.2.0-cudnn8-runtime-Ubuntu20.04: docker.io/nvidia/cuda:12.2.0-cudnn8-runtime-Ubuntu20.04: not found
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose up -d --build --remove-orphans
Compose can now delegate builds to bake for better performance.
 To do so, set COMPOSE_BAKE=true.
[+] Building 0.2s (2/2) FINISHED                                                                                                                              docker:default
 => [avatar-app internal] load build definition from dockerfile                                                                                                         0.0s
 => => transferring dockerfile: 2.22kB                                                                                                                                  0.0s
 => ERROR [avatar-app internal] load metadata for docker.io/nvidia/cuda:12.2.0-cudnn8-runtime-ubuntu20.04                                                               0.1s
------
 > [avatar-app internal] load metadata for docker.io/nvidia/cuda:12.2.0-cudnn8-runtime-ubuntu20.04:
------
failed to solve: nvidia/cuda:12.2.0-cudnn8-runtime-ubuntu20.04: failed to resolve source metadata for docker.io/nvidia/cuda:12.2.0-cudnn8-runtime-ubuntu20.04: docker.io/nvidia/cuda:12.2.0-cudnn8-runtime-ubuntu20.04: not found
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose up -d --build --remove-orphans
Compose can now delegate builds to bake for better performance.
 To do so, set COMPOSE_BAKE=true.
[+] Building 2505.6s (28/28) FINISHED                                                                                                                         docker:default
 => [avatar-app internal] load build definition from dockerfile                                                                                                         0.0s
 => => transferring dockerfile: 2.22kB                                                                                                                                  0.0s
 => [avatar-app internal] load metadata for docker.io/nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04                                                                     0.2s
 => [avatar-app internal] load .dockerignore                                                                                                                            0.0s
 => => transferring context: 2B                                                                                                                                         0.0s
 => [avatar-app  1/22] FROM docker.io/nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04@sha256:c2336dadc71ae5b5ce490a55cc0100d876287d28f429a5d2840c8a3a8e86fef0             0.0s
 => [avatar-app internal] load build context                                                                                                                            0.0s
 => => transferring context: 10.02kB                                                                                                                                    0.0s
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
 => [avatar-app 13/22] COPY Wav2Lip/ /home/docker/Wav2Lip/                                                                                                              0.1s
 => [avatar-app 14/22] COPY source/ /home/docker/source/                                                                                                                0.0s
 => [avatar-app 15/22] COPY weights/ /home/docker/weights/                                                                                                              1.5s
 => [avatar-app 16/22] RUN chown -R docker:docker /home/docker                                                                                                          1.3s
 => [avatar-app 17/22] RUN python3 -m venv /home/docker/venv                                                                                                            4.1s
 => [avatar-app 18/22] RUN /home/docker/venv/bin/pip install --no-cache-dir --upgrade pip                                                                               4.0s
 => [avatar-app 19/22] RUN /home/docker/venv/bin/pip install --no-cache-dir -r requirements.txt                                                                      2389.2s
 => [avatar-app 20/22] RUN /home/docker/venv/bin/pip install --no-cache-dir gunicorn                                                                                    1.2s
 => [avatar-app 21/22] RUN chown -R docker:docker /home/docker /home/docker/venv                                                                                       35.5s
 => [avatar-app 22/22] RUN chmod -R u+rwX /home/docker /home/docker/venv                                                                                               35.9s
 => [avatar-app] exporting to image                                                                                                                                    32.5s
 => => exporting layers                                                                                                                                                32.4s
 => => writing image sha256:4367066aecad29032e18ad7a9b10a22ab154765bea35d79e5316d45c118f3472                                                                            0.0s
 => => naming to docker.io/library/avatar-app                                                                                                                           0.0s
 => [avatar-app] resolving provenance for metadata file                                                                                                                 0.0s
[+] Running 3/3
 ✔ avatar-app                     Built                                                                                                                                 0.0s 
 ✔ Network avatar_default         Created                                                                                                                               0.1s 
 ✔ Container avatar-avatar-app-1  Started                                                                                                                               0.7s 
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
avatar-app-1  | Form data requires "python-multipart" to be installed. 
avatar-app-1  | You can install "python-multipart" with: 
avatar-app-1  | 
avatar-app-1  | pip install python-multipart
avatar-app-1  | 
avatar-app-1  | Traceback (most recent call last):
avatar-app-1  |   File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main
avatar-app-1  |     return _run_code(code, main_globals, None,
avatar-app-1  |   File "/usr/lib/python3.10/runpy.py", line 86, in _run_code
avatar-app-1  |     exec(code, run_globals)
avatar-app-1  |   File "/home/docker/API.py", line 44, in <module>
avatar-app-1  |     async def sync_audio(request: Request, audio: UploadFile = File(...)):
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 992, in decorator
avatar-app-1  |     self.add_api_route(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 931, in add_api_route
avatar-app-1  |     route = route_class(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 552, in __init__
avatar-app-1  |     self.dependant = get_dependant(path=self.path_format, call=self.endpoint)
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 277, in get_dependant
avatar-app-1  |     param_details = analyze_param(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 472, in analyze_param
avatar-app-1  |     ensure_multipart_is_installed()
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 107, in ensure_multipart_is_installed
avatar-app-1  |     raise RuntimeError(multipart_not_installed_error) from None
avatar-app-1  | RuntimeError: Form data requires "python-multipart" to be installed. 
avatar-app-1  | You can install "python-multipart" with: 
avatar-app-1  | 
avatar-app-1  | pip install python-multipart
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
avatar-app-1  | Form data requires "python-multipart" to be installed. 
avatar-app-1  | You can install "python-multipart" with: 
avatar-app-1  | 
avatar-app-1  | pip install python-multipart
avatar-app-1  | 
avatar-app-1  | Traceback (most recent call last):
avatar-app-1  |   File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main
avatar-app-1  |     return _run_code(code, main_globals, None,
avatar-app-1  |   File "/usr/lib/python3.10/runpy.py", line 86, in _run_code
avatar-app-1  |     exec(code, run_globals)
avatar-app-1  |   File "/home/docker/API.py", line 44, in <module>
avatar-app-1  |     async def sync_audio(request: Request, audio: UploadFile = File(...)):
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 992, in decorator
avatar-app-1  |     self.add_api_route(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 931, in add_api_route
avatar-app-1  |     route = route_class(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 552, in __init__
avatar-app-1  |     self.dependant = get_dependant(path=self.path_format, call=self.endpoint)
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 277, in get_dependant
avatar-app-1  |     param_details = analyze_param(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 472, in analyze_param
avatar-app-1  |     ensure_multipart_is_installed()
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 107, in ensure_multipart_is_installed
avatar-app-1  |     raise RuntimeError(multipart_not_installed_error) from None
avatar-app-1  | RuntimeError: Form data requires "python-multipart" to be installed. 
avatar-app-1  | You can install "python-multipart" with: 
avatar-app-1  | 
avatar-app-1  | pip install python-multipart
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
avatar-app-1  | Form data requires "python-multipart" to be installed. 
avatar-app-1  | You can install "python-multipart" with: 
avatar-app-1  | 
avatar-app-1  | pip install python-multipart
avatar-app-1  | 
avatar-app-1  | Traceback (most recent call last):
avatar-app-1  |   File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main
avatar-app-1  |     return _run_code(code, main_globals, None,
avatar-app-1  |   File "/usr/lib/python3.10/runpy.py", line 86, in _run_code
avatar-app-1  |     exec(code, run_globals)
avatar-app-1  |   File "/home/docker/API.py", line 44, in <module>
avatar-app-1  |     async def sync_audio(request: Request, audio: UploadFile = File(...)):
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 992, in decorator
avatar-app-1  |     self.add_api_route(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 931, in add_api_route
avatar-app-1  |     route = route_class(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 552, in __init__
avatar-app-1  |     self.dependant = get_dependant(path=self.path_format, call=self.endpoint)
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 277, in get_dependant
avatar-app-1  |     param_details = analyze_param(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 472, in analyze_param
avatar-app-1  |     ensure_multipart_is_installed()
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 107, in ensure_multipart_is_installed
avatar-app-1  |     raise RuntimeError(multipart_not_installed_error) from None
avatar-app-1  | RuntimeError: Form data requires "python-multipart" to be installed. 
avatar-app-1  | You can install "python-multipart" with: 
avatar-app-1  | 
avatar-app-1  | pip install python-multipart
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
avatar-app-1  | Form data requires "python-multipart" to be installed. 
avatar-app-1  | You can install "python-multipart" with: 
avatar-app-1  | 
avatar-app-1  | pip install python-multipart
avatar-app-1  | 
avatar-app-1  | Traceback (most recent call last):
avatar-app-1  |   File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main
avatar-app-1  |     return _run_code(code, main_globals, None,
avatar-app-1  |   File "/usr/lib/python3.10/runpy.py", line 86, in _run_code
avatar-app-1  |     exec(code, run_globals)
avatar-app-1  |   File "/home/docker/API.py", line 44, in <module>
avatar-app-1  |     async def sync_audio(request: Request, audio: UploadFile = File(...)):
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 992, in decorator
avatar-app-1  |     self.add_api_route(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 931, in add_api_route
avatar-app-1  |     route = route_class(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 552, in __init__
avatar-app-1  |     self.dependant = get_dependant(path=self.path_format, call=self.endpoint)
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 277, in get_dependant
avatar-app-1  |     param_details = analyze_param(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 472, in analyze_param
avatar-app-1  |     ensure_multipart_is_installed()
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 107, in ensure_multipart_is_installed
avatar-app-1  |     raise RuntimeError(multipart_not_installed_error) from None
avatar-app-1  | RuntimeError: Form data requires "python-multipart" to be installed. 
avatar-app-1  | You can install "python-multipart" with: 
avatar-app-1  | 
avatar-app-1  | pip install python-multipart
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
avatar-app-1  | Form data requires "python-multipart" to be installed. 
avatar-app-1  | You can install "python-multipart" with: 
avatar-app-1  | 
avatar-app-1  | pip install python-multipart
avatar-app-1  | 
avatar-app-1  | Traceback (most recent call last):
avatar-app-1  |   File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main
avatar-app-1  |     return _run_code(code, main_globals, None,
avatar-app-1  |   File "/usr/lib/python3.10/runpy.py", line 86, in _run_code
avatar-app-1  |     exec(code, run_globals)
avatar-app-1  |   File "/home/docker/API.py", line 44, in <module>
avatar-app-1  |     async def sync_audio(request: Request, audio: UploadFile = File(...)):
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 992, in decorator
avatar-app-1  |     self.add_api_route(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 931, in add_api_route
avatar-app-1  |     route = route_class(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 552, in __init__
avatar-app-1  |     self.dependant = get_dependant(path=self.path_format, call=self.endpoint)
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 277, in get_dependant
avatar-app-1  |     param_details = analyze_param(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 472, in analyze_param
avatar-app-1  |     ensure_multipart_is_installed()
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 107, in ensure_multipart_is_installed
avatar-app-1  |     raise RuntimeError(multipart_not_installed_error) from None
avatar-app-1  | RuntimeError: Form data requires "python-multipart" to be installed. 
avatar-app-1  | You can install "python-multipart" with: 
avatar-app-1  | 
avatar-app-1  | pip install python-multipart
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
avatar-app-1  | Form data requires "python-multipart" to be installed. 
avatar-app-1  | You can install "python-multipart" with: 
avatar-app-1  | 
avatar-app-1  | pip install python-multipart
avatar-app-1  | 
avatar-app-1  | Traceback (most recent call last):
avatar-app-1  |   File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main
avatar-app-1  |     return _run_code(code, main_globals, None,
avatar-app-1  |   File "/usr/lib/python3.10/runpy.py", line 86, in _run_code
avatar-app-1  |     exec(code, run_globals)
avatar-app-1  |   File "/home/docker/API.py", line 44, in <module>
avatar-app-1  |     async def sync_audio(request: Request, audio: UploadFile = File(...)):
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 992, in decorator
avatar-app-1  |     self.add_api_route(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 931, in add_api_route
avatar-app-1  |     route = route_class(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 552, in __init__
avatar-app-1  |     self.dependant = get_dependant(path=self.path_format, call=self.endpoint)
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 277, in get_dependant
avatar-app-1  |     param_details = analyze_param(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 472, in analyze_param
avatar-app-1  |     ensure_multipart_is_installed()
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 107, in ensure_multipart_is_installed
avatar-app-1  |     raise RuntimeError(multipart_not_installed_error) from None
avatar-app-1  | RuntimeError: Form data requires "python-multipart" to be installed. 
avatar-app-1  | You can install "python-multipart" with: 
avatar-app-1  | 
avatar-app-1  | pip install python-multipart
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
avatar-app-1  | Form data requires "python-multipart" to be installed. 
avatar-app-1  | You can install "python-multipart" with: 
avatar-app-1  | 
avatar-app-1  | pip install python-multipart
avatar-app-1  | 
avatar-app-1  | Traceback (most recent call last):
avatar-app-1  |   File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main
avatar-app-1  |     return _run_code(code, main_globals, None,
avatar-app-1  |   File "/usr/lib/python3.10/runpy.py", line 86, in _run_code
avatar-app-1  |     exec(code, run_globals)
avatar-app-1  |   File "/home/docker/API.py", line 44, in <module>
avatar-app-1  |     async def sync_audio(request: Request, audio: UploadFile = File(...)):
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 992, in decorator
avatar-app-1  |     self.add_api_route(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 931, in add_api_route
avatar-app-1  |     route = route_class(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 552, in __init__
avatar-app-1  |     self.dependant = get_dependant(path=self.path_format, call=self.endpoint)
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 277, in get_dependant
avatar-app-1  |     param_details = analyze_param(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 472, in analyze_param
avatar-app-1  |     ensure_multipart_is_installed()
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 107, in ensure_multipart_is_installed
avatar-app-1  |     raise RuntimeError(multipart_not_installed_error) from None
avatar-app-1  | RuntimeError: Form data requires "python-multipart" to be installed. 
avatar-app-1  | You can install "python-multipart" with: 
avatar-app-1  | 
avatar-app-1  | pip install python-multipart
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
avatar-app-1  | Form data requires "python-multipart" to be installed. 
avatar-app-1  | You can install "python-multipart" with: 
avatar-app-1  | 
avatar-app-1  | pip install python-multipart
avatar-app-1  | 
avatar-app-1  | Traceback (most recent call last):
avatar-app-1  |   File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main
avatar-app-1  |     return _run_code(code, main_globals, None,
avatar-app-1  |   File "/usr/lib/python3.10/runpy.py", line 86, in _run_code
avatar-app-1  |     exec(code, run_globals)
avatar-app-1  |   File "/home/docker/API.py", line 44, in <module>
avatar-app-1  |     async def sync_audio(request: Request, audio: UploadFile = File(...)):
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 992, in decorator
avatar-app-1  |     self.add_api_route(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 931, in add_api_route
avatar-app-1  |     route = route_class(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 552, in __init__
avatar-app-1  |     self.dependant = get_dependant(path=self.path_format, call=self.endpoint)
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 277, in get_dependant
avatar-app-1  |     param_details = analyze_param(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 472, in analyze_param
avatar-app-1  |     ensure_multipart_is_installed()
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 107, in ensure_multipart_is_installed
avatar-app-1  |     raise RuntimeError(multipart_not_installed_error) from None
avatar-app-1  | RuntimeError: Form data requires "python-multipart" to be installed. 
avatar-app-1  | You can install "python-multipart" with: 
avatar-app-1  | 
avatar-app-1  | pip install python-multipart
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
avatar-app-1  | Form data requires "python-multipart" to be installed. 
avatar-app-1  | You can install "python-multipart" with: 
avatar-app-1  | 
avatar-app-1  | pip install python-multipart
avatar-app-1  | 
avatar-app-1  | Traceback (most recent call last):
avatar-app-1  |   File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main
avatar-app-1  |     return _run_code(code, main_globals, None,
avatar-app-1  |   File "/usr/lib/python3.10/runpy.py", line 86, in _run_code
avatar-app-1  |     exec(code, run_globals)
avatar-app-1  |   File "/home/docker/API.py", line 44, in <module>
avatar-app-1  |     async def sync_audio(request: Request, audio: UploadFile = File(...)):
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 992, in decorator
avatar-app-1  |     self.add_api_route(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 931, in add_api_route
avatar-app-1  |     route = route_class(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 552, in __init__
avatar-app-1  |     self.dependant = get_dependant(path=self.path_format, call=self.endpoint)
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 277, in get_dependant
avatar-app-1  |     param_details = analyze_param(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 472, in analyze_param
avatar-app-1  |     ensure_multipart_is_installed()
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 107, in ensure_multipart_is_installed
avatar-app-1  |     raise RuntimeError(multipart_not_installed_error) from None
avatar-app-1  | RuntimeError: Form data requires "python-multipart" to be installed. 
avatar-app-1  | You can install "python-multipart" with: 
avatar-app-1  | 
avatar-app-1  | pip install python-multipart
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
avatar-app-1  | Form data requires "python-multipart" to be installed. 
avatar-app-1  | You can install "python-multipart" with: 
avatar-app-1  | 
avatar-app-1  | pip install python-multipart
avatar-app-1  | 
avatar-app-1  | Traceback (most recent call last):
avatar-app-1  |   File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main
avatar-app-1  |     return _run_code(code, main_globals, None,
avatar-app-1  |   File "/usr/lib/python3.10/runpy.py", line 86, in _run_code
avatar-app-1  |     exec(code, run_globals)
avatar-app-1  |   File "/home/docker/API.py", line 44, in <module>
avatar-app-1  |     async def sync_audio(request: Request, audio: UploadFile = File(...)):
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 992, in decorator
avatar-app-1  |     self.add_api_route(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 931, in add_api_route
avatar-app-1  |     route = route_class(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 552, in __init__
avatar-app-1  |     self.dependant = get_dependant(path=self.path_format, call=self.endpoint)
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 277, in get_dependant
avatar-app-1  |     param_details = analyze_param(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 472, in analyze_param
avatar-app-1  |     ensure_multipart_is_installed()
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 107, in ensure_multipart_is_installed
avatar-app-1  |     raise RuntimeError(multipart_not_installed_error) from None
avatar-app-1  | RuntimeError: Form data requires "python-multipart" to be installed. 
avatar-app-1  | You can install "python-multipart" with: 
avatar-app-1  | 
avatar-app-1  | pip install python-multipart
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
avatar-app-1  | Form data requires "python-multipart" to be installed. 
avatar-app-1  | You can install "python-multipart" with: 
avatar-app-1  | 
avatar-app-1  | pip install python-multipart
avatar-app-1  | 
avatar-app-1  | Traceback (most recent call last):
avatar-app-1  |   File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main
avatar-app-1  |     return _run_code(code, main_globals, None,
avatar-app-1  |   File "/usr/lib/python3.10/runpy.py", line 86, in _run_code
avatar-app-1  |     exec(code, run_globals)
avatar-app-1  |   File "/home/docker/API.py", line 44, in <module>
avatar-app-1  |     async def sync_audio(request: Request, audio: UploadFile = File(...)):
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 992, in decorator
avatar-app-1  |     self.add_api_route(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 931, in add_api_route
avatar-app-1  |     route = route_class(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 552, in __init__
avatar-app-1  |     self.dependant = get_dependant(path=self.path_format, call=self.endpoint)
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 277, in get_dependant
avatar-app-1  |     param_details = analyze_param(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 472, in analyze_param
avatar-app-1  |     ensure_multipart_is_installed()
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 107, in ensure_multipart_is_installed
avatar-app-1  |     raise RuntimeError(multipart_not_installed_error) from None
avatar-app-1  | RuntimeError: Form data requires "python-multipart" to be installed. 
avatar-app-1  | You can install "python-multipart" with: 
avatar-app-1  | 
avatar-app-1  | pip install python-multipart
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
avatar-app-1  | Form data requires "python-multipart" to be installed. 
avatar-app-1  | You can install "python-multipart" with: 
avatar-app-1  | 
avatar-app-1  | pip install python-multipart
avatar-app-1  | 
avatar-app-1  | Traceback (most recent call last):
avatar-app-1  |   File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main
avatar-app-1  |     return _run_code(code, main_globals, None,
avatar-app-1  |   File "/usr/lib/python3.10/runpy.py", line 86, in _run_code
avatar-app-1  |     exec(code, run_globals)
avatar-app-1  |   File "/home/docker/API.py", line 44, in <module>
avatar-app-1  |     async def sync_audio(request: Request, audio: UploadFile = File(...)):
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 992, in decorator
avatar-app-1  |     self.add_api_route(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 931, in add_api_route
avatar-app-1  |     route = route_class(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/routing.py", line 552, in __init__
avatar-app-1  |     self.dependant = get_dependant(path=self.path_format, call=self.endpoint)
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 277, in get_dependant
avatar-app-1  |     param_details = analyze_param(
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 472, in analyze_param
avatar-app-1  |     ensure_multipart_is_installed()
avatar-app-1  |   File "/home/docker/venv/lib/python3.10/site-packages/fastapi/dependencies/utils.py", line 107, in ensure_multipart_is_installed
avatar-app-1  |     raise RuntimeError(multipart_not_installed_error) from None
avatar-app-1  | RuntimeError: Form data requires "python-multipart" to be installed. 
avatar-app-1  | You can install "python-multipart" with: 
avatar-app-1  | 
avatar-app-1  | pip install python-multipart
avatar-app-1  | 
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose up -d 
[+] Running 1/1
 ✔ Container avatar-avatar-app-1  Started                                                                                                                               0.0s 
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ 
