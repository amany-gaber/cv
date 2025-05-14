yaz@gpu:~/tak/GP/AVATAR$ docker compose up -d --build
WARN[0000] The "GID" variable is not set. Defaulting to a blank string. 
Compose can now delegate builds to bake for better performance.
 To do so, set COMPOSE_BAKE=true.
[+] Building 1973.6s (19/19) FINISHED                                                                                                                         docker:default
 => [avatar-app internal] load build definition from dockerfile                                                                                                         0.0s
 => => transferring dockerfile: 1.86kB                                                                                                                                  0.0s
 => [avatar-app internal] load metadata for docker.io/library/ubuntu:24.04                                                                                              1.0s
 => [avatar-app internal] load .dockerignore                                                                                                                            0.0s
 => => transferring context: 2B                                                                                                                                         0.0s
 => [avatar-app internal] load build context                                                                                                                            0.1s
 => => transferring context: 209B                                                                                                                                       0.1s
 => [avatar-app builder-image 1/6] FROM docker.io/library/ubuntu:24.04@sha256:6015f66923d7afbc53558d7ccffd325d43b4e249f41a6e93eef074c9505d2233                         25.0s
 => => resolve docker.io/library/ubuntu:24.04@sha256:6015f66923d7afbc53558d7ccffd325d43b4e249f41a6e93eef074c9505d2233                                                   0.0s
 => => sha256:dc17125eaac86538c57da886e494a34489122fb6a3ebb6411153d742594c2ddc 424B / 424B                                                                              0.0s
 => => sha256:a0e45e2ce6e6e22e73185397d162a64fcf2f80a41c597015cab05d9a7b5913ce 2.30kB / 2.30kB                                                                          0.0s
 => => sha256:0622fac788edde5d30e7bbd2688893e5452a19ff237a2e4615e2d8181321cb4e 29.72MB / 29.72MB                                                                       23.9s
 => => sha256:6015f66923d7afbc53558d7ccffd325d43b4e249f41a6e93eef074c9505d2233 6.69kB / 6.69kB                                                                          0.0s
 => => extracting sha256:0622fac788edde5d30e7bbd2688893e5452a19ff237a2e4615e2d8181321cb4e                                                                               1.0s
 => [avatar-app builder-image 2/6] RUN apt-get update && apt-get install -y --no-install-recommends     python3.12     python3.12-dev     python3.12-venv     python  353.3s
 => [avatar-app runner-image 2/8] RUN apt-get update && apt-get install -y --no-install-recommends     python3.12     python3.12-venv     ffmpeg     && apt-get -y a  215.8s
 => [avatar-app runner-image 3/8] RUN useradd --create-home docker                                                                                                      0.2s
 => [avatar-app builder-image 3/6] RUN python3.12 -m venv /home/docker/venv                                                                                             4.0s 
 => [avatar-app builder-image 4/6] RUN python3.12 -m pip install --upgrade pip                                                                                          4.4s
 => [avatar-app builder-image 5/6] COPY requirements.txt ./requirements.txt                                                                                             0.1s
 => [avatar-app builder-image 6/6] RUN pip install --no-cache-dir -r requirements.txt                                                                                1517.4s
 => [avatar-app runner-image 4/8] COPY --from=builder-image /home/docker/venv /home/docker/venv                                                                        16.5s
 => [avatar-app runner-image 5/8] RUN mkdir /home/docker/app                                                                                                            0.2s
 => [avatar-app runner-image 6/8] WORKDIR /home/docker/app                                                                                                              0.0s
 => [avatar-app runner-image 7/8] COPY --chown=docker:docker ./*.py .                                                                                                   0.0s
 => [avatar-app runner-image 8/8] RUN chmod -R u+rwX /home/docker/app                                                                                                   0.2s
 => [avatar-app] exporting to image                                                                                                                                    30.2s
 => => exporting layers                                                                                                                                                30.2s
 => => writing image sha256:cee48f1894a0dd450c3b868c495ec83b6645780e306f51c20f733cd698ea2e8d                                                                            0.0s
 => => naming to docker.io/library/avatar-avatar-app                                                                                                                    0.0s
 => [avatar-app] resolving provenance for metadata file                                                                                                                 0.0s
WARN[1973] Found orphan containers ([avatar-avatar-api-1]) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up. 
[+] Running 2/2
 ✔ avatar-app                     Built                                                                                                                                 0.0s 
 ✔ Container avatar-avatar-app-1  Started                                                                                                                               0.6s 
yaz@gpu:~/tak/GP/AVATAR$ docker logs avatar-avatar-app-1
/home/docker/venv/bin/python3.12: can't open file '/home/docker/venv/bin/uvicorn': [Errno 13] Permission denied
/home/docker/venv/bin/python3.12: can't open file '/home/docker/venv/bin/uvicorn': [Errno 13] Permission denied
/home/docker/venv/bin/python3.12: can't open file '/home/docker/venv/bin/uvicorn': [Errno 13] Permission denied
/home/docker/venv/bin/python3.12: can't open file '/home/docker/venv/bin/uvicorn': [Errno 13] Permission denied
/home/docker/venv/bin/python3.12: can't open file '/home/docker/venv/bin/uvicorn': [Errno 13] Permission denied
/home/docker/venv/bin/python3.12: can't open file '/home/docker/venv/bin/uvicorn': [Errno 13] Permission denied
/home/docker/venv/bin/python3.12: can't open file '/home/docker/venv/bin/uvicorn': [Errno 13] Permission denied
/home/docker/venv/bin/python3.12: can't open file '/home/docker/venv/bin/uvicorn': [Errno 13] Permission denied
/home/docker/venv/bin/python3.12: can't open file '/home/docker/venv/bin/uvicorn': [Errno 13] Permission denied
/home/docker/venv/bin/python3.12: can't open file '/home/docker/venv/bin/uvicorn': [Errno 13] Permission denied
/home/docker/venv/bin/python3.12: can't open file '/home/docker/venv/bin/uvicorn': [Errno 13] Permission denied
/home/docker/venv/bin/python3.12: can't open file '/home/docker/venv/bin/uvicorn': [Errno 13] Permission denied
/home/docker/venv/bin/python3.12: can't open file '/home/docker/venv/bin/uvicorn': [Errno 13] Permission denied
/home/docker/venv/bin/python3.12: can't open file '/home/docker/venv/bin/uvicorn': [Errno 13] Permission denied
/home/docker/venv/bin/python3.12: can't open file '/home/docker/venv/bin/uvicorn': [Errno 13] Permission denied
/home/docker/venv/bin/python3.12: can't open file '/home/docker/venv/bin/uvicorn': [Errno 13] Permission denied
yaz@gpu:~/tak/GP/AVATAR$ docker compose up -d
WARN[0000] The "GID" variable is not set. Defaulting to a blank string. 
WARN[0000] Found orphan containers ([avatar-avatar-api-1]) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up. 
[+] Running 1/1
 ✔ Container avatar-avatar-app-1  Started                                                                                                                               0.0s 
yaz@gpu:~/tak/GP/AVATAR$ docker rm -f avatar-avatar-api-1
avatar-avatar-api-1
yaz@gpu:~/tak/GP/AVATAR$ docker compose up -d --build --remove-orphans
WARN[0000] The "GID" variable is not set. Defaulting to a blank string. 
Compose can now delegate builds to bake for better performance.
 To do so, set COMPOSE_BAKE=true.
[+] Building 59.6s (7/19)                                                                                                                                     docker:default
 => [avatar-app internal] load build definition from dockerfile                                                                                                         0.0s
 => => transferring dockerfile: 1.98kB                                                                                                                                  0.0s
 => [avatar-app internal] load metadata for docker.io/nvidia/cuda:12.2.0-runtime-ubuntu22.04                                                                            0.4s
 => [avatar-app internal] load metadata for docker.io/nvidia/cuda:12.2.0-devel-ubuntu22.04                                                                              0.4s
 => [avatar-app internal] load .dockerignore                                                                                                                            0.0s
 => => transferring context: 2B                                                                                                                                         0.0s
 => CANCELED [avatar-app builder-image 1/6] FROM docker.io/nvidia/cuda:12.2.0-devel-ubuntu22.04@sha256:c4e81887e4aa9f13b1119337323cba89601319ecb282383b879c4ba50510fd  59.1s
 => => resolve docker.io/nvidia/cuda:12.2.0-devel-ubuntu22.04@sha256:c4e81887e4aa9f13b1119337323cba89601319ecb282383b879c4ba50510fd17                                   0.0s
 => => sha256:ec5d41e67e1e8e8a82451aa5d08bf3db04a2859e9a9266569406537ee2d7a9f8 2.63kB / 2.63kB                                                                          0.0s
 => => sha256:aece8493d3972efa43bfd4ee3cdba659c0f787f8f59c82fb3e48c87cbb22a12e 29.54MB / 29.54MB                                                                       34.2s
 => => sha256:c4e81887e4aa9f13b1119337323cba89601319ecb282383b879c4ba50510fd17 743B / 743B                                                                              0.0s
 => => sha256:5307765dadf8460b069757105b659484d7551f149397fb56c4817f383dd5b028 15.62kB / 15.62kB                                                                        0.0s
 => => sha256:9fe5ccccae45d6811769206667e494085cb511666be47b8e659087c249083c3f 4.62MB / 4.62MB                                                                          5.2s
 => => sha256:8054e9d6e8d6718cc3461aa4172ad048564cdf9f552c8f9820bd127859aa007c 49.28MB / 56.08MB                                                                       59.1s
 => => sha256:bdddd5cb92f6b4613055bcbcd3226df9821c7facd5af9a998ba12dae080ef134 185B / 185B                                                                              5.4s
 => => sha256:5324914b447286e0e6512290373af079a25f94499a379e642774245376e60885 6.89kB / 6.89kB                                                                          5.7s
 => => sha256:9a9dd462fc4c5ca1dd29994385be60a5bb359843fc93447331b8c97dfec99bf9 40.89MB / 1.10GB                                                                        59.1s
 => => sha256:95eef45e00fabd2bce97586bfe26be456b0e4b3ef3d88d07a8b334ee05cc603c 63.35kB / 63.35kB                                                                       35.4s
 => => extracting sha256:aece8493d3972efa43bfd4ee3cdba659c0f787f8f59c82fb3e48c87cbb22a12e                                                                               1.3s
 => => sha256:e2554c2d377e1176c0b8687b17aa7cbe2c48746857acc11686281a4adee35a0a 1.69kB / 1.69kB                                                                         35.6s
 => => extracting sha256:9fe5ccccae45d6811769206667e494085cb511666be47b8e659087c249083c3f                                                                              23.4s
 => => sha256:4640d022dbb8eb47da53ccc2de59f8f5e780ea046289ba3cffdf0a5bd8d19810 1.52kB / 1.52kB                                                                         35.8s
 => => sha256:aa750c79a4cc745750c40a37cad738f9bcea14abb96b0c5a811a9b53f185b9c9 13.63MB / 2.34GB                                                                        59.1s
 => [avatar-app internal] load build context                                                                                                                            3.3s
 => => transferring context: 498.93MB                                                                                                                                   3.3s
 => CANCELED [avatar-app runner-image 1/8] FROM docker.io/nvidia/cuda:12.2.0-runtime-ubuntu22.04@sha256:739e0bde7bafdb2ed9057865f53085539f51cbf8bd6bf719f2e114bab321e  59.1s
 => => resolve docker.io/nvidia/cuda:12.2.0-runtime-ubuntu22.04@sha256:739e0bde7bafdb2ed9057865f53085539f51cbf8bd6bf719f2e114bab321e70e                                 0.0s
 => => sha256:739e0bde7bafdb2ed9057865f53085539f51cbf8bd6bf719f2e114bab321e70e 743B / 743B                                                                              0.0s
 => => sha256:370f16e473527763fc5f78bb8bb06c76c13b692c7255405e8497df022527281d 2.21kB / 2.21kB                                                                          0.0s
 => => sha256:5f87b1ee9f9af968f84779dd3166023fb545818e0e8d572f5ca7dbc2499377d2 12.17kB / 12.17kB                                                                        0.0s
 => => sha256:8054e9d6e8d6718cc3461aa4172ad048564cdf9f552c8f9820bd127859aa007c 49.28MB / 56.08MB                                                                       59.1s
 => => sha256:aece8493d3972efa43bfd4ee3cdba659c0f787f8f59c82fb3e48c87cbb22a12e 29.54MB / 29.54MB                                                                       34.2s
 => => sha256:9fe5ccccae45d6811769206667e494085cb511666be47b8e659087c249083c3f 4.62MB / 4.62MB                                                                          5.2s
 => => sha256:bdddd5cb92f6b4613055bcbcd3226df9821c7facd5af9a998ba12dae080ef134 185B / 185B                                                                              5.4s
 => => sha256:5324914b447286e0e6512290373af079a25f94499a379e642774245376e60885 6.89kB / 6.89kB                                                                          5.7s
 => => sha256:9a9dd462fc4c5ca1dd29994385be60a5bb359843fc93447331b8c97dfec99bf9 40.89MB / 1.10GB                                                                        59.1s
 => => sha256:95eef45e00fabd2bce97586bfe26be456b0e4b3ef3d88d07a8b334ee05cc603c 63.35kB / 63.35kB                                                                       35.4s
 => => extracting sha256:aece8493d3972efa43bfd4ee3cdba659c0f787f8f59c82fb3e48c87cbb22a12e                                                                              24.9s
 => => sha256:e2554c2d377e1176c0b8687b17aa7cbe2c48746857acc11686281a4adee35a0a 1.69kB / 1.69kB                                                                         35.6s
 => => extracting sha256:9fe5ccccae45d6811769206667e494085cb511666be47b8e659087c249083c3f                                                                               0.2s
 => => sha256:4640d022dbb8eb47da53ccc2de59f8f5e780ea046289ba3cffdf0a5bd8d19810 1.52kB / 1.52kB                                                                         35.8s

yaz@gpu:~/tak/GP/AVATAR$ docker compose up -d --build --remove-orphans
WARN[0000] The "GID" variable is not set. Defaulting to a blank string. 
Compose can now delegate builds to bake for better performance.
 To do so, set COMPOSE_BAKE=true.
[+] Building 2591.6s (21/21) FINISHED                                                                                                                         docker:default
 => [avatar-app internal] load build definition from dockerfile                                                                                                         0.0s
 => => transferring dockerfile: 1.98kB                                                                                                                                  0.0s
 => [avatar-app internal] load metadata for docker.io/nvidia/cuda:12.2.0-devel-ubuntu22.04                                                                              1.1s
 => [avatar-app internal] load metadata for docker.io/nvidia/cuda:12.2.0-runtime-ubuntu22.04                                                                            1.0s
 => [avatar-app internal] load .dockerignore                                                                                                                            0.0s
 => => transferring context: 2B                                                                                                                                         0.0s
 => [avatar-app internal] load build context                                                                                                                            0.0s
 => => transferring context: 7.80kB                                                                                                                                     0.0s
 => [avatar-app builder-image 1/6] FROM docker.io/nvidia/cuda:12.2.0-devel-ubuntu22.04@sha256:c4e81887e4aa9f13b1119337323cba89601319ecb282383b879c4ba50510fd17       1096.7s
 => => resolve docker.io/nvidia/cuda:12.2.0-devel-ubuntu22.04@sha256:c4e81887e4aa9f13b1119337323cba89601319ecb282383b879c4ba50510fd17                                   0.0s
 => => sha256:ec5d41e67e1e8e8a82451aa5d08bf3db04a2859e9a9266569406537ee2d7a9f8 2.63kB / 2.63kB                                                                          0.0s
 => => sha256:aece8493d3972efa43bfd4ee3cdba659c0f787f8f59c82fb3e48c87cbb22a12e 29.54MB / 29.54MB                                                                       12.6s
 => => sha256:9fe5ccccae45d6811769206667e494085cb511666be47b8e659087c249083c3f 4.62MB / 4.62MB                                                                          7.0s
 => => sha256:c4e81887e4aa9f13b1119337323cba89601319ecb282383b879c4ba50510fd17 743B / 743B                                                                              0.0s
 => => sha256:8054e9d6e8d6718cc3461aa4172ad048564cdf9f552c8f9820bd127859aa007c 56.08MB / 56.08MB                                                                       49.3s
 => => sha256:5307765dadf8460b069757105b659484d7551f149397fb56c4817f383dd5b028 15.62kB / 15.62kB                                                                        0.0s
 => => sha256:bdddd5cb92f6b4613055bcbcd3226df9821c7facd5af9a998ba12dae080ef134 185B / 185B                                                                              7.2s
 => => sha256:5324914b447286e0e6512290373af079a25f94499a379e642774245376e60885 6.89kB / 6.89kB                                                                          7.4s
 => => sha256:9a9dd462fc4c5ca1dd29994385be60a5bb359843fc93447331b8c97dfec99bf9 1.10GB / 1.10GB                                                                        523.3s
 => => sha256:95eef45e00fabd2bce97586bfe26be456b0e4b3ef3d88d07a8b334ee05cc603c 63.35kB / 63.35kB                                                                       13.0s
 => => extracting sha256:aece8493d3972efa43bfd4ee3cdba659c0f787f8f59c82fb3e48c87cbb22a12e                                                                               1.1s
 => => sha256:e2554c2d377e1176c0b8687b17aa7cbe2c48746857acc11686281a4adee35a0a 1.69kB / 1.69kB                                                                         13.3s
 => => sha256:4640d022dbb8eb47da53ccc2de59f8f5e780ea046289ba3cffdf0a5bd8d19810 1.52kB / 1.52kB                                                                         13.7s
 => => sha256:aa750c79a4cc745750c40a37cad738f9bcea14abb96b0c5a811a9b53f185b9c9 2.34GB / 2.34GB                                                                       1066.9s
 => => extracting sha256:9fe5ccccae45d6811769206667e494085cb511666be47b8e659087c249083c3f                                                                               0.2s
 => => extracting sha256:8054e9d6e8d6718cc3461aa4172ad048564cdf9f552c8f9820bd127859aa007c                                                                            2541.2s
 => => sha256:9e2de25be969afa4e73937f8283a1100f4d964fc0876c2f2184fda25ad23eeda 88.05kB / 88.05kB                                                                       50.1s
 => => extracting sha256:bdddd5cb92f6b4613055bcbcd3226df9821c7facd5af9a998ba12dae080ef134                                                                               0.0s
 => => extracting sha256:5324914b447286e0e6512290373af079a25f94499a379e642774245376e60885                                                                               0.0s
 => => extracting sha256:9a9dd462fc4c5ca1dd29994385be60a5bb359843fc93447331b8c97dfec99bf9                                                                              11.6s
 => => extracting sha256:95eef45e00fabd2bce97586bfe26be456b0e4b3ef3d88d07a8b334ee05cc603c                                                                            2055.5s
 => => extracting sha256:e2554c2d377e1176c0b8687b17aa7cbe2c48746857acc11686281a4adee35a0a                                                                            2055.5s
 => => extracting sha256:4640d022dbb8eb47da53ccc2de59f8f5e780ea046289ba3cffdf0a5bd8d19810                                                                               0.0s
 => => extracting sha256:aa750c79a4cc745750c40a37cad738f9bcea14abb96b0c5a811a9b53f185b9c9                                                                              29.6s
 => => extracting sha256:9e2de25be969afa4e73937f8283a1100f4d964fc0876c2f2184fda25ad23eeda                                                                               0.0s
 => [avatar-app runner-image 1/8] FROM docker.io/nvidia/cuda:12.2.0-runtime-ubuntu22.04@sha256:739e0bde7bafdb2ed9057865f53085539f51cbf8bd6bf719f2e114bab321e70e       535.1s
 => => resolve docker.io/nvidia/cuda:12.2.0-runtime-ubuntu22.04@sha256:739e0bde7bafdb2ed9057865f53085539f51cbf8bd6bf719f2e114bab321e70e                                 0.0s
 => => sha256:9fe5ccccae45d6811769206667e494085cb511666be47b8e659087c249083c3f 4.62MB / 4.62MB                                                                          7.0s
 => => sha256:739e0bde7bafdb2ed9057865f53085539f51cbf8bd6bf719f2e114bab321e70e 743B / 743B                                                                              0.0s
 => => sha256:370f16e473527763fc5f78bb8bb06c76c13b692c7255405e8497df022527281d 2.21kB / 2.21kB                                                                          0.0s
 => => sha256:5f87b1ee9f9af968f84779dd3166023fb545818e0e8d572f5ca7dbc2499377d2 12.17kB / 12.17kB                                                                        0.0s
 => => sha256:aece8493d3972efa43bfd4ee3cdba659c0f787f8f59c82fb3e48c87cbb22a12e 29.54MB / 29.54MB                                                                       12.6s
 => => sha256:8054e9d6e8d6718cc3461aa4172ad048564cdf9f552c8f9820bd127859aa007c 56.08MB / 56.08MB                                                                       49.3s
 => => sha256:bdddd5cb92f6b4613055bcbcd3226df9821c7facd5af9a998ba12dae080ef134 185B / 185B                                                                              7.2s
 => => sha256:5324914b447286e0e6512290373af079a25f94499a379e642774245376e60885 6.89kB / 6.89kB                                                                          7.4s
 => => sha256:9a9dd462fc4c5ca1dd29994385be60a5bb359843fc93447331b8c97dfec99bf9 1.10GB / 1.10GB                                                                        523.3s
 => => sha256:95eef45e00fabd2bce97586bfe26be456b0e4b3ef3d88d07a8b334ee05cc603c 63.35kB / 63.35kB                                                                       13.0s
 => => extracting sha256:aece8493d3972efa43bfd4ee3cdba659c0f787f8f59c82fb3e48c87cbb22a12e                                                                            2577.8s
 => => sha256:e2554c2d377e1176c0b8687b17aa7cbe2c48746857acc11686281a4adee35a0a 1.69kB / 1.69kB                                                                         13.3s
 => => sha256:4640d022dbb8eb47da53ccc2de59f8f5e780ea046289ba3cffdf0a5bd8d19810 1.52kB / 1.52kB                                                                         13.7s
 => => extracting sha256:8054e9d6e8d6718cc3461aa4172ad048564cdf9f552c8f9820bd127859aa007c                                                                               0.9s
 => => extracting sha256:bdddd5cb92f6b4613055bcbcd3226df9821c7facd5af9a998ba12dae080ef134                                                                            2540.2s
 => => extracting sha256:5324914b447286e0e6512290373af079a25f94499a379e642774245376e60885                                                                            2540.2s
 => => extracting sha256:9a9dd462fc4c5ca1dd29994385be60a5bb359843fc93447331b8c97dfec99bf9                                                                            2067.2s
 => => extracting sha256:95eef45e00fabd2bce97586bfe26be456b0e4b3ef3d88d07a8b334ee05cc603c                                                                               0.0s
 => => extracting sha256:e2554c2d377e1176c0b8687b17aa7cbe2c48746857acc11686281a4adee35a0a                                                                               0.0s
 => => extracting sha256:4640d022dbb8eb47da53ccc2de59f8f5e780ea046289ba3cffdf0a5bd8d19810                                                                            2055.5s
 => [avatar-app runner-image 2/8] RUN apt-get update && apt-get install -y --no-install-recommends     python3.10     python3.10-venv     ffmpeg     && apt-get -y a  142.3s
 => [avatar-app runner-image 3/8] RUN useradd --create-home docker                                                                                                      0.3s
 => [avatar-app builder-image 2/6] RUN apt-get update && apt-get install -y --no-install-recommends     python3.10     python3.10-dev     python3.10-venv     python3  42.9s
 => [avatar-app builder-image 3/6] RUN python3.10 -m venv /home/docker/venv                                                                                             3.9s
 => [avatar-app builder-image 4/6] RUN python3.10 -m pip install --upgrade pip                                                                                          4.1s
 => [avatar-app builder-image 5/6] COPY requirements.txt ./requirements.txt                                                                                             0.0s
 => [avatar-app builder-image 6/6] RUN pip install -r requirements.txt  # Changed: Removed --no-cache-dir to enable caching                                          1364.1s
 => [avatar-app runner-image 4/8] COPY --from=builder-image /home/docker/venv /home/docker/venv                                                                        16.6s
 => [avatar-app runner-image 5/8] RUN mkdir /home/docker/app                                                                                                            0.2s
 => [avatar-app runner-image 6/8] WORKDIR /home/docker/app                                                                                                              0.0s
 => [avatar-app runner-image 7/8] COPY --chown=docker:docker . .                                                                                                        1.8s
 => [avatar-app runner-image 8/8] RUN chmod -R u+rwX /home/docker/app                                                                                                   1.3s
 => [avatar-app] exporting to image                                                                                                                                    35.0s
 => => exporting layers                                                                                                                                                35.0s
 => => writing image sha256:4529d65222864d0bf15a23f3406045aaec85eb9ee4fe66d3931f55ad097db984                                                                            0.0s
 => => naming to docker.io/library/avatar-avatar-app                                                                                                                    0.0s
 => [avatar-app] resolving provenance for metadata file                                                                                                                 0.0s
[+] Running 3/3
 ✔ avatar-app                     Built                                                                                                                                 0.0s 
 ✔ Volume "avatar_pip-cache"      Created                                                                                                                               0.0s 
 ✔ Container avatar-avatar-app-1  Started                                                                                                                               0.5s 
yaz@gpu:~/tak/GP/AVATAR$    
