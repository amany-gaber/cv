✔ avatar-app                     Built                                                                                                                                 0.0s 
 ✔ Network avatar_default         Created                                                                                                                               0.1s 
 ⠼ Container avatar-avatar-app-1  Starting                                                                                                                              0.5s 
Error response from daemon: failed to set up container networking: driver failed programming external connectivity on endpoint avatar-avatar-app-1 (85e8acc0df27d31ee74a1cd1bff43edc51cb79610abfcef26be41c7043e058bd): failed to bind host port for 0.0.0.0:9036:172.25.0.2:9036/tcp: address already in use
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose logs
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose down
[+] Running 2/2
 ✔ Container avatar-avatar-app-1  Removed                                                                                                                               0.0s 
 ✔ Network avatar_default         Removed                                                                                                                               0.2s 
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose up -d 
[+] Running 1/2
 ✔ Network avatar_default         Created                                                                                                                               0.1s 
 ⠧ Container avatar-avatar-app-1  Starting                                                                                                                              0.7s 
Error response from daemon: failed to set up container networking: driver failed programming external connectivity on endpoint avatar-avatar-app-1 (8b6f4f72722cb85a521a4f9773d63a6a7857c5d6dac214e8369c92b1e8b98ef7): failed to bind host port for 0.0.0.0:9036:172.25.0.2:8000/tcp: address already in use
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose down
[+] Running 2/2
 ✔ Container avatar-avatar-app-1  Removed                                                                                                                               0.0s 
 ✔ Network avatar_default         Removed                                                                                                                               0.2s 
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose up -d 
[+] Running 2/2
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
avatar-app-1  | Traceback (most recent call last):
avatar-app-1  |   File "/home/docker/API.py", line 9, in <module>
avatar-app-1  |     from .lipsync import LipSync
avatar-app-1  | ImportError: attempted relative import with no known parent package
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
avatar-app-1  | Traceback (most recent call last):
avatar-app-1  |   File "/home/docker/API.py", line 9, in <module>
avatar-app-1  |     from .lipsync import LipSync
avatar-app-1  | ImportError: attempted relative import with no known parent package
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
avatar-app-1  | Traceback (most recent call last):
avatar-app-1  |   File "/home/docker/API.py", line 9, in <module>
avatar-app-1  |     from .lipsync import LipSync
avatar-app-1  | ImportError: attempted relative import with no known parent package
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
avatar-app-1  | Traceback (most recent call last):
avatar-app-1  |   File "/home/docker/API.py", line 9, in <module>
avatar-app-1  |     from .lipsync import LipSync
avatar-app-1  | ImportError: attempted relative import with no known parent package
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
avatar-app-1  | Traceback (most recent call last):
avatar-app-1  |   File "/home/docker/API.py", line 9, in <module>
avatar-app-1  |     from .lipsync import LipSync
avatar-app-1  | ImportError: attempted relative import with no known parent package
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
avatar-app-1  | Traceback (most recent call last):
avatar-app-1  |   File "/home/docker/API.py", line 9, in <module>
avatar-app-1  |     from .lipsync import LipSync
avatar-app-1  | ImportError: attempted relative import with no known parent package
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
avatar-app-1  | Traceback (most recent call last):
avatar-app-1  |   File "/home/docker/API.py", line 9, in <module>
avatar-app-1  |     from .lipsync import LipSync
avatar-app-1  | ImportError: attempted relative import with no known parent package
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
avatar-app-1  | Traceback (most recent call last):
avatar-app-1  |   File "/home/docker/API.py", line 9, in <module>
avatar-app-1  |     from .lipsync import LipSync
avatar-app-1  | ImportError: attempted relative import with no known parent package
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
avatar-app-1  | Traceback (most recent call last):
avatar-app-1  |   File "/home/docker/API.py", line 9, in <module>
avatar-app-1  |     from .lipsync import LipSync
avatar-app-1  | ImportError: attempted relative import with no known parent package
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ curl http://127.0.0.1:4036/docs
curl: (7) Failed to connect to 127.0.0.1 port 4036 after 0 ms: Could not connect to server
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ 
