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
yaz@gpu:~/tak/GP/AVATAR$ 
