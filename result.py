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
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$
