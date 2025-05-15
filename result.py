yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose up --build
Compose can now delegate builds to bake for better performance.
 To do so, set COMPOSE_BAKE=true.
[+] Building 0.5s (2/2) FINISHED                                                                                                                              docker:default
 => [avatar-app internal] load build definition from dockerfile                                                                                                         0.0s
 => => transferring dockerfile: 2.65kB                                                                                                                                  0.0s
 => ERROR [avatar-app internal] load metadata for docker.io/nvidia/cuda:11.8.0-cudnn8-runtime-Ubuntu20.04                                                               0.4s
------
 > [avatar-app internal] load metadata for docker.io/nvidia/cuda:11.8.0-cudnn8-runtime-Ubuntu20.04:
------
failed to solve: nvidia/cuda:11.8.0-cudnn8-runtime-Ubuntu20.04: failed to resolve source metadata for docker.io/nvidia/cuda:11.8.0-cudnn8-runtime-Ubuntu20.04: docker.io/nvidia/cuda:11.8.0-cudnn8-runtime-Ubuntu20.04: not found
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ 
