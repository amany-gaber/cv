yaz@gpu:~/tak/GP/AVATAR$ docker compose down
[+] Running 2/2
 ✔ Container avatar-avatar-app-1  Removed                                                                                                                               0.0s 
 ✔ Network avatar_default         Removed                                                                                                                               0.2s 
yaz@gpu:~/tak/GP/AVATAR$ docker compose up --build
Compose can now delegate builds to bake for better performance.
 To do so, set COMPOSE_BAKE=true.
[+] Building 3809.5s (29/29) FINISHED                                                                                                                         docker:default
 => [avatar-app internal] load build definition from dockerfile                                                                                                         0.0s
 => => transferring dockerfile: 2.52kB                                                                                                                                  0.0s
 => [avatar-app internal] load metadata for docker.io/nvidia/cuda:11.6.2-cudnn8-runtime-ubuntu20.04                                                                     0.5s
 => [avatar-app internal] load .dockerignore                                                                                                                            0.0s
 => => transferring context: 2B                                                                                                                                         0.0s
 => [avatar-app  1/23] FROM docker.io/nvidia/cuda:11.6.2-cudnn8-runtime-ubuntu20.04@sha256:ea2af6ed2bc770f83ed30235f7369b8c83a49b58cdb0bfd55f1227d89edfad8f          1256.8s
 => => resolve docker.io/nvidia/cuda:11.6.2-cudnn8-runtime-ubuntu20.04@sha256:ea2af6ed2bc770f83ed30235f7369b8c83a49b58cdb0bfd55f1227d89edfad8f                          0.0s
 => => sha256:56480238c4d714e5e5d2438e34e144c114a8d1088c5f385b791bab68b7f3ccdc 2.42kB / 2.42kB                                                                          0.0s
 => => sha256:ea2af6ed2bc770f83ed30235f7369b8c83a49b58cdb0bfd55f1227d89edfad8f 743B / 743B                                                                              0.0s
 => => sha256:5971243731bceb03735002e6ee458efdf4a5bb61dc9413e66c37f9d600f0747f 12.66kB / 12.66kB                                                                        0.0s
 => => sha256:a3d20efe6db8b46becf9f41b997b53a8b8165d6bfeee0a5ff49a7be97bdf2233 7.94MB / 7.94MB                                                                         16.4s
 => => sha256:bfdf8ce43b671936d3ff95ddbbf98c7e5a6fcf9c30b391ff68a1f5bd8f2542f0 23.61MB / 23.61MB                                                                       37.7s
 => => sha256:ad14f66bfcf925d4d3845f273afe5a865b9d9e9facf722b88416b30ac62071a0 184B / 184B                                                                              0.9s
 => => sha256:1056ff735c5934cffc31a621d8f362eb3ecaee0667227fe735dfaaa1165286f3 6.88kB / 6.88kB                                                                          4.4s
 => => sha256:a08e157987cd9fc3e8d38ceeaf215714d570bd31c907f95789149406cf533488 1.12GB / 1.12GB                                                                       1235.1s
 => => extracting sha256:a3d20efe6db8b46becf9f41b997b53a8b8165d6bfeee0a5ff49a7be97bdf2233                                                                               0.3s
 => => sha256:b05f735a8d36dd8deb11dd6429ceadd62dc9e4a39853b522a52ba8d81cde20ec 62.69kB / 62.69kB                                                                       17.2s
 => => sha256:2ca2acc6de6fb15b50b8fb872e242fd21a9aab9ebb28e6438f5f2d4f99f601e1 1.68kB / 1.68kB                                                                         17.7s
 => => sha256:a5f96919abbf7212577a68604528951c76e98558582f83236e7e6f0fb2a24f54 1.52kB / 1.52kB                                                                         18.0s
 => => sha256:e2656b42ba8bbb33ae9842d877d83f583017e58fc1b7ebbcdf97e42dc654a408 727.16MB / 727.16MB                                                                   1037.2s
 => => extracting sha256:bfdf8ce43b671936d3ff95ddbbf98c7e5a6fcf9c30b391ff68a1f5bd8f2542f0                                                                               0.4s
 => => extracting sha256:ad14f66bfcf925d4d3845f273afe5a865b9d9e9facf722b88416b30ac62071a0                                                                               0.0s
 => => extracting sha256:1056ff735c5934cffc31a621d8f362eb3ecaee0667227fe735dfaaa1165286f3                                                                               0.0s
 => => extracting sha256:a08e157987cd9fc3e8d38ceeaf215714d570bd31c907f95789149406cf533488                                                                              13.0s
 => => extracting sha256:b05f735a8d36dd8deb11dd6429ceadd62dc9e4a39853b522a52ba8d81cde20ec                                                                               0.0s
 => => extracting sha256:2ca2acc6de6fb15b50b8fb872e242fd21a9aab9ebb28e6438f5f2d4f99f601e1                                                                               0.0s
 => => extracting sha256:a5f96919abbf7212577a68604528951c76e98558582f83236e7e6f0fb2a24f54                                                                               0.0s
 => => extracting sha256:e2656b42ba8bbb33ae9842d877d83f583017e58fc1b7ebbcdf97e42dc654a408                                                                               8.4s
 => [avatar-app internal] load build context                                                                                                                            0.0s
 => => transferring context: 7.33kB                                                                                                                                     0.0s
 => [avatar-app  2/23] RUN apt-get update && apt-get install -y     software-properties-common     && rm -rf /var/lib/apt/lists/*                                      63.6s
 => [avatar-app  3/23] RUN add-apt-repository ppa:deadsnakes/ppa -y                                                                                                    33.7s
 => [avatar-app  4/23] RUN apt-get update && apt-get install -y     python3.10     python3.10-venv     python3.10-distutils     python3-pip     ffmpeg     && rm -rf  156.1s
 => [avatar-app  5/23] RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1                                                                 0.2s
 => [avatar-app  6/23] RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.10 1                                                                   0.3s
 => [avatar-app  7/23] RUN python3.10 -m ensurepip --upgrade                                                                                                            4.3s
 => [avatar-app  8/23] RUN python3.10 -m pip install --upgrade pip                                                                                                      4.1s
 => [avatar-app  9/23] RUN useradd -m -s /bin/bash docker                                                                                                               0.3s
 => [avatar-app 10/23] WORKDIR /home/docker                                                                                                                             0.0s
 => [avatar-app 11/23] RUN mkdir -p /home/docker/Wav2Lip /home/docker/source /home/docker/videos /home/docker/weights                                                   0.2s
 => [avatar-app 12/23] COPY API.py inference.py lipsync.py lipsync_test.py Wav2Lip_inference_patched.py requirements.txt /home/docker/                                  0.1s
 => [avatar-app 13/23] COPY Wav2Lip/ /home/docker/Wav2Lip/                                                                                                              0.0s
 => [avatar-app 14/23] COPY source/ /home/docker/source/                                                                                                                0.0s
 => [avatar-app 15/23] COPY weights/ /home/docker/weights/                                                                                                              1.1s
 => [avatar-app 16/23] RUN chown -R docker:docker /home/docker                                                                                                          1.3s
 => [avatar-app 17/23] RUN python3 -m venv /home/docker/venv                                                                                                            4.2s
 => [avatar-app 18/23] RUN /home/docker/venv/bin/pip install --no-cache-dir --upgrade pip                                                                               3.9s
 => [avatar-app 19/23] RUN /home/docker/venv/bin/pip install --no-cache-dir -r requirements.txt                                                                      2165.4s
 => [avatar-app 20/23] RUN /home/docker/venv/bin/pip install --no-cache-dir numpy==1.26.4                                                                               1.3s
 => [avatar-app 21/23] RUN /home/docker/venv/bin/pip install --no-cache-dir gunicorn                                                                                    1.2s
 => [avatar-app 22/23] RUN chown -R docker:docker /home/docker /home/docker/venv                                                                                       36.7s
 => [avatar-app 23/23] RUN chmod -R u+rwX /home/docker /home/docker/venv                                                                                               37.0s
 => [avatar-app] exporting to image                                                                                                                                    36.8s
 => => exporting layers                                                                                                                                                36.7s
 => => writing image sha256:f0d7f58c23882f1b2ab3da079e568ca35015d19389264a19df9a569bae1f997d                                                                            0.0s
 => => naming to docker.io/library/avatar-app                                                                                                                           0.0s
 => [avatar-app] resolving provenance for metadata file                                                                                                                 0.0s
[+] Running 3/3
 ✔ avatar-app                     Built                                                                                                                                 0.0s 
 ✔ Network avatar_default         Created                                                                                                                               0.1s 
 ✔ Container avatar-avatar-app-1  Created                                                                                                                               0.1s 
Attaching to avatar-app-1
avatar-app-1  | 
avatar-app-1  | ==========
avatar-app-1  | == CUDA ==
avatar-app-1  | ==========
avatar-app-1  | 
avatar-app-1  | CUDA Version 11.6.2
avatar-app-1  | 
avatar-app-1  | Container image Copyright (c) 2016-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
avatar-app-1  | 
avatar-app-1  | This container image and its contents are governed by the NVIDIA Deep Learning Container License.
avatar-app-1  | By pulling and using the container, you accept the terms and conditions of this license:
avatar-app-1  | https://developer.nvidia.com/ngc/nvidia-deep-learning-container-license
avatar-app-1  | 
avatar-app-1  | A copy of this license is made available in this container at /NGC-DL-CONTAINER-LICENSE for your convenience.
avatar-app-1  | 
avatar-app-1  | [2025-05-15 15:34:29 +0000] [1] [DEBUG] Current configuration:
avatar-app-1  |   config: ./gunicorn.conf.py
avatar-app-1  |   wsgi_app: None
avatar-app-1  |   bind: ['0.0.0.0:8000']
avatar-app-1  |   backlog: 2048
avatar-app-1  |   workers: 4
avatar-app-1  |   worker_class: uvicorn.workers.UvicornWorker
avatar-app-1  |   threads: 1
avatar-app-1  |   worker_connections: 1000
avatar-app-1  |   max_requests: 0
avatar-app-1  |   max_requests_jitter: 0
avatar-app-1  |   timeout: 30
avatar-app-1  |   graceful_timeout: 30
avatar-app-1  |   keepalive: 2
avatar-app-1  |   limit_request_line: 4094
avatar-app-1  |   limit_request_fields: 100
avatar-app-1  |   limit_request_field_size: 8190
avatar-app-1  |   reload: False
avatar-app-1  |   reload_engine: auto
avatar-app-1  |   reload_extra_files: []
avatar-app-1  |   spew: False
avatar-app-1  |   check_config: False
avatar-app-1  |   print_config: False
avatar-app-1  |   preload_app: False
avatar-app-1  |   sendfile: None
avatar-app-1  |   reuse_port: False
avatar-app-1  |   chdir: /home/docker
avatar-app-1  |   daemon: False
avatar-app-1  |   raw_env: []
avatar-app-1  |   pidfile: None
avatar-app-1  |   worker_tmp_dir: None
avatar-app-1  |   user: 1000
avatar-app-1  |   group: 1000
avatar-app-1  |   umask: 0
avatar-app-1  |   initgroups: False
avatar-app-1  |   tmp_upload_dir: None
avatar-app-1  |   secure_scheme_headers: {'X-FORWARDED-PROTOCOL': 'ssl', 'X-FORWARDED-PROTO': 'https', 'X-FORWARDED-SSL': 'on'}
avatar-app-1  |   forwarded_allow_ips: ['127.0.0.1', '::1']
avatar-app-1  |   accesslog: None
avatar-app-1  |   disable_redirect_access_to_syslog: False
avatar-app-1  |   access_log_format: %(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"
avatar-app-1  |   errorlog: -
avatar-app-1  |   loglevel: debug
avatar-app-1  |   capture_output: False
avatar-app-1  |   logger_class: gunicorn.glogging.Logger
avatar-app-1  |   logconfig: None
avatar-app-1  |   logconfig_dict: {}
avatar-app-1  |   logconfig_json: None
avatar-app-1  |   syslog_addr: udp://localhost:514
avatar-app-1  |   syslog: False
avatar-app-1  |   syslog_prefix: None
avatar-app-1  |   syslog_facility: user
avatar-app-1  |   enable_stdio_inheritance: False
avatar-app-1  |   statsd_host: None
avatar-app-1  |   dogstatsd_tags: 
avatar-app-1  |   statsd_prefix: 
avatar-app-1  |   proc_name: None
avatar-app-1  |   default_proc_name: API:app
avatar-app-1  |   pythonpath: None
avatar-app-1  |   paste: None
avatar-app-1  |   on_starting: <function OnStarting.on_starting at 0x74d0ccb4a440>
avatar-app-1  |   on_reload: <function OnReload.on_reload at 0x74d0ccb4a560>
avatar-app-1  |   when_ready: <function WhenReady.when_ready at 0x74d0ccb4a680>
avatar-app-1  |   pre_fork: <function Prefork.pre_fork at 0x74d0ccb4a7a0>
avatar-app-1  |   post_fork: <function Postfork.post_fork at 0x74d0ccb4a8c0>
avatar-app-1  |   post_worker_init: <function PostWorkerInit.post_worker_init at 0x74d0ccb4a9e0>
avatar-app-1  |   worker_int: <function WorkerInt.worker_int at 0x74d0ccb4ab00>
avatar-app-1  |   worker_abort: <function WorkerAbort.worker_abort at 0x74d0ccb4ac20>
avatar-app-1  |   pre_exec: <function PreExec.pre_exec at 0x74d0ccb4ad40>
avatar-app-1  |   pre_request: <function PreRequest.pre_request at 0x74d0ccb4ae60>
avatar-app-1  |   post_request: <function PostRequest.post_request at 0x74d0ccb4aef0>
avatar-app-1  |   child_exit: <function ChildExit.child_exit at 0x74d0ccb4b010>
avatar-app-1  |   worker_exit: <function WorkerExit.worker_exit at 0x74d0ccb4b130>
avatar-app-1  |   nworkers_changed: <function NumWorkersChanged.nworkers_changed at 0x74d0ccb4b250>
avatar-app-1  |   on_exit: <function OnExit.on_exit at 0x74d0ccb4b370>
avatar-app-1  |   ssl_context: <function NewSSLContext.ssl_context at 0x74d0ccb4b490>
avatar-app-1  |   proxy_protocol: False
avatar-app-1  |   proxy_allow_ips: ['127.0.0.1', '::1']
avatar-app-1  |   keyfile: None
avatar-app-1  |   certfile: None
avatar-app-1  |   ssl_version: 2
avatar-app-1  |   cert_reqs: 0
avatar-app-1  |   ca_certs: None
avatar-app-1  |   suppress_ragged_eofs: True
avatar-app-1  |   do_handshake_on_connect: False
avatar-app-1  |   ciphers: None
avatar-app-1  |   raw_paste_global_conf: []
avatar-app-1  |   permit_obsolete_folding: False
avatar-app-1  |   strip_header_spaces: False
avatar-app-1  |   permit_unconventional_http_method: False
avatar-app-1  |   permit_unconventional_http_version: False
avatar-app-1  |   casefold_http_method: False
avatar-app-1  |   forwarder_headers: ['SCRIPT_NAME', 'PATH_INFO']
avatar-app-1  |   header_map: drop
avatar-app-1  | [2025-05-15 15:34:29 +0000] [1] [INFO] Starting gunicorn 23.0.0
avatar-app-1  | [2025-05-15 15:34:29 +0000] [1] [DEBUG] Arbiter booted
avatar-app-1  | [2025-05-15 15:34:29 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)
avatar-app-1  | [2025-05-15 15:34:29 +0000] [1] [INFO] Using worker: uvicorn.workers.UvicornWorker
avatar-app-1  | [2025-05-15 15:34:29 +0000] [27] [INFO] Booting worker with pid: 27
avatar-app-1  | [2025-05-15 15:34:29 +0000] [28] [INFO] Booting worker with pid: 28
avatar-app-1  | [2025-05-15 15:34:29 +0000] [29] [INFO] Booting worker with pid: 29
avatar-app-1  | [2025-05-15 15:34:29 +0000] [30] [INFO] Booting worker with pid: 30
avatar-app-1  | [2025-05-15 15:34:29 +0000] [1] [DEBUG] 4 workers
avatar-app-1  | [2025-05-15 15:34:29 +0000] [28] [INFO] Started server process [28]
avatar-app-1  | [2025-05-15 15:34:29 +0000] [27] [INFO] Started server process [27]
avatar-app-1  | [2025-05-15 15:34:29 +0000] [28] [INFO] Waiting for application startup.
avatar-app-1  | [2025-05-15 15:34:29 +0000] [27] [INFO] Waiting for application startup.
avatar-app-1  | [2025-05-15 15:34:29 +0000] [28] [INFO] Application startup complete.
avatar-app-1  | [2025-05-15 15:34:29 +0000] [27] [INFO] Application startup complete.
avatar-app-1  | [2025-05-15 15:34:29 +0000] [29] [INFO] Started server process [29]
avatar-app-1  | [2025-05-15 15:34:29 +0000] [29] [INFO] Waiting for application startup.
avatar-app-1  | [2025-05-15 15:34:29 +0000] [29] [INFO] Application startup complete.
avatar-app-1  | [2025-05-15 15:34:29 +0000] [30] [INFO] Started server process [30]
avatar-app-1  | [2025-05-15 15:34:29 +0000] [30] [INFO] Waiting for application startup.
avatar-app-1  | [2025-05-15 15:34:29 +0000] [30] [INFO] Application startup complete.
Gracefully stopping... (press Ctrl+C again to force)
[+] Stopping 1/1
 ✔ Container avatar-avatar-app-1  Stopped                                                                                                                               0.4s 
yaz@gpu:~/tak/GP/AVATAR$ docker compose up -d
[+] Running 1/1
 ✔ Container avatar-avatar-app-1  Started                                                                                                                               0.4s 
yaz@gpu:~/tak/GP/AVATAR$ docker ps -a
CONTAINER ID   IMAGE                                              COMMAND                  CREATED         STATUS                          PORTS                                                                                                                                       NAMES
46ec38f78201   avatar-app                                         "/opt/nvidia/nvidia_…"   7 minutes ago   Up About a minute               0.0.0.0:4036->8000/tcp, [::]:4036->8000/tcp                                                                                                 avatar-avatar-app-1
073e97948ba2   docker.infogerance.d-fi.fr/camel_llm_fe:1.0.6      "/docker-entrypoint.…"   21 hours ago    Up 21 hours                     0.0.0.0:4623->80/tcp, [::]:4623->80/tcp                                                                                                     camel_llm-client-1
fcef7aa298c3   docker.infogerance.d-fi.fr/meapal-front:1.0.7      "/docker-entrypoint.…"   21 hours ago    Up 21 hours                     0.0.0.0:5144->80/tcp, [::]:5144->80/tcp                                                                                                     meapal-client-1
7d01fd2462b3   sttapi:1.0.0                                       "sh -c 'uvicorn rout…"   2 days ago      Up 2 days                       0.0.0.0:4004->4004/tcp, [::]:4004->4004/tcp                                                                                                 sttapi-api-1
053a8f5f5608   docker.infogerance.d-fi.fr/nginx-domain:2.10.0     "/docker-entrypoint.…"   2 days ago      Up 2 days                       0.0.0.0:80->80/tcp, [::]:80->80/tcp, 0.0.0.0:443->443/tcp, [::]:443->443/tcp                                                                domain-client-1
e28fae0f6b38   llm-fastapi                                        "uvicorn API:app --h…"   2 days ago      Up 2 days                       0.0.0.0:8906->7410/tcp, [::]:8906->7410/tcp                                                                                                 llm-fastapi-1
e3c3ee10c02e   specificjob-api                                    "uvicorn main:app --…"   7 days ago      Up 7 days                       0.0.0.0:6437->8080/tcp, [::]:6437->8080/tcp                                                                                                 spisficjob-api-1
ded6917ecd5c   7fc9b59b8ab5                                       "uvicorn main:app --…"   7 days ago      Up 7 days                       0.0.0.0:8080->8080/tcp, [::]:8080->8080/tcp                                                                                                 jobspecific-api-1
ab9daddbb340   confluentinc/cp-kafka:7.5.0                        "/etc/confluent/dock…"   7 days ago      Up 7 days                       0.0.0.0:4567->4567/tcp, [::]:4567->4567/tcp, 9092/tcp                                                                                       ivs5-kafka-1
1a8732f0a46d   confluentinc/cp-zookeeper:7.5.0                    "/etc/confluent/dock…"   7 days ago      Up 7 days                       2888/tcp, 3888/tcp, 0.0.0.0:3456->2181/tcp, [::]:3456->2181/tcp                                                                             ivs5-zookeeper-1
0150c0768bdf   timescale/timescaledb:latest-pg14                  "docker-entrypoint.s…"   7 days ago      Up 7 days                       0.0.0.0:5678->5432/tcp, [::]:5678->5432/tcp                                                                                                 timescaledb
9eb1faa0e9d3   postgres:14                                        "docker-entrypoint.s…"   7 days ago      Up 7 days                       0.0.0.0:6789->5432/tcp, [::]:6789->5432/tcp                                                                                                 postgres
fd0e88ed5362   cvm-api:1.0.0                                      "uvicorn main:app --…"   8 days ago      Up 7 days                       0.0.0.0:6438->8080/tcp, [::]:6438->8080/tcp                                                                                                 jobmatch_api
5d6dad1cbce7   ollama/ollama                                      "/bin/ollama serve"      10 days ago     Created                                                                                                                                                                     llm-ollama-1
5038ccc85271   nvidia/cuda:11.8.0-base-ubuntu20.04                "nvidia-smi"             11 days ago     Exited (0) 11 days ago                                                                                                                                                      eager_lovelace
92f14d4ee1cf   face-api:1.0.0                                     "sh -c 'uvicorn main…"   2 weeks ago     Up 7 days                       0.0.0.0:4400->8080/tcp, [::]:4400->8080/tcp                                                                                                 faceapp-api-1
7810e5b346b1   project_graduation_api                             "uvicorn main:app --…"   2 weeks ago     Up 7 days                       0.0.0.0:5111->8080/tcp, [::]:5111->8080/tcp                                                                                                 project_toursium
7bce721ddb6c   voice-api:1.0.0                                    "uvicorn main:app --…"   2 weeks ago     Up 7 days                       0.0.0.0:4444->8080/tcp, [::]:4444->8080/tcp                                                                                                 voice_toon_api
2c2b67879969   interview-system-fastapi                           "uvicorn app.main:ap…"   2 weeks ago     Exited (0) 7 days ago                                                                                                                                                       interview-system-fastapi-1
59e9ac4304fb   mongo-express:latest                               "/sbin/tini -- /dock…"   2 weeks ago     Exited (143) 7 days ago                                                                                                                                                     interview-system-mongo-express-1
faf5e2f59363   interview-system-celery                            "celery -A app.tasks…"   2 weeks ago     Exited (0) 7 days ago                                                                                                                                                       interview-system-celery-1
9b60d99eb568   mongo:6.0                                          "docker-entrypoint.s…"   2 weeks ago     Exited (0) 7 days ago                                                                                                                                                       interview-system-mongodb-1
381dfd86d53e   redis:7.0                                          "docker-entrypoint.s…"   2 weeks ago     Exited (0) 7 days ago                                                                                                                                                       interview-system-redis-1
9b952f4e5400   project_ficofi_db                                  "docker-entrypoint.s…"   3 weeks ago     Up 7 days                       0.0.0.0:5434->5432/tcp, [::]:5434->5432/tcp                                                                                                 ficofi_postgres
1ef8daa96af3   debezium/debezium-ui:latest                        "/deployments/run-ja…"   3 weeks ago     Up 7 days                       0.0.0.0:8568->8080/tcp, [::]:8568->8080/tcp                                                                                                 debezium-ui
5e9aa6cd4123   debezium/connect:3.0.0.Final                       "/docker-entrypoint.…"   3 weeks ago     Up 7 days (unhealthy)           8778/tcp, 9092/tcp, 0.0.0.0:8093->8083/tcp, [::]:8093->8083/tcp                                                                             debezium
fa8d230cf079   confluentinc/cp-enterprise-control-center:latest   "/etc/confluent/dock…"   3 weeks ago     Up 7 days (unhealthy)           0.0.0.0:9321->9021/tcp, [::]:9321->9021/tcp                                                                                                 control-center
194c62554175   confluentinc/cp-kafka:7.4.0                        "/etc/confluent/dock…"   3 weeks ago     Up 7 days (healthy)             0.0.0.0:9092->9092/tcp, [::]:9092->9092/tcp, 0.0.0.0:9101->9101/tcp, [::]:9101->9101/tcp, 0.0.0.0:29092->29092/tcp, [::]:29092->29092/tcp   broker
d2fe1598b7e4   bitnami/spark:latest                               "/bin/sh -c 'pip ins…"   3 weeks ago     Up 7 days                                                                                                                                                                   spark-worker
ee048f667bc8   bitnami/spark:latest                               "/bin/sh -c 'pip ins…"   3 weeks ago     Up 7 days                       0.0.0.0:7077->7077/tcp, [::]:7077->7077/tcp, 0.0.0.0:8081->8081/tcp, [::]:8081->8081/tcp                                                    spark-master
2df05a750140   confluentinc/cp-zookeeper:7.4.0                    "/etc/confluent/dock…"   3 weeks ago     Up 7 days (healthy)             2888/tcp, 0.0.0.0:2181->2181/tcp, [::]:2181->2181/tcp, 3888/tcp                                                                             zookeeper
b9d4f0acba57   dpage/pgadmin4:latest                              "/entrypoint.sh"         3 weeks ago     Up 7 days                       443/tcp, 0.0.0.0:5050->80/tcp, [::]:5050->80/tcp                                                                                            pgadmin
bafa3d4a6635   grafana/grafana:latest                             "/run.sh"                3 weeks ago     Restarting (1) 17 seconds ago                                                                                                                                               grafana
yaz@gpu:~/tak/GP/AVATAR$ docker compose logs
avatar-app-1  | 
avatar-app-1  | ==========
avatar-app-1  | == CUDA ==
avatar-app-1  | ==========
avatar-app-1  | 
avatar-app-1  | CUDA Version 11.6.2
avatar-app-1  | 
avatar-app-1  | Container image Copyright (c) 2016-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
avatar-app-1  | 
avatar-app-1  | This container image and its contents are governed by the NVIDIA Deep Learning Container License.
avatar-app-1  | By pulling and using the container, you accept the terms and conditions of this license:
avatar-app-1  | https://developer.nvidia.com/ngc/nvidia-deep-learning-container-license
avatar-app-1  | 
avatar-app-1  | A copy of this license is made available in this container at /NGC-DL-CONTAINER-LICENSE for your convenience.
avatar-app-1  | 
avatar-app-1  | [2025-05-15 15:34:29 +0000] [1] [DEBUG] Current configuration:
avatar-app-1  |   config: ./gunicorn.conf.py
avatar-app-1  |   wsgi_app: None
avatar-app-1  |   bind: ['0.0.0.0:8000']
avatar-app-1  |   backlog: 2048
avatar-app-1  |   workers: 4
avatar-app-1  |   worker_class: uvicorn.workers.UvicornWorker
avatar-app-1  |   threads: 1
avatar-app-1  |   worker_connections: 1000
avatar-app-1  |   max_requests: 0
avatar-app-1  |   max_requests_jitter: 0
avatar-app-1  |   timeout: 30
avatar-app-1  |   graceful_timeout: 30
avatar-app-1  |   keepalive: 2
avatar-app-1  |   limit_request_line: 4094
avatar-app-1  |   limit_request_fields: 100
avatar-app-1  |   limit_request_field_size: 8190
avatar-app-1  |   reload: False
avatar-app-1  |   reload_engine: auto
avatar-app-1  |   reload_extra_files: []
avatar-app-1  |   spew: False
avatar-app-1  |   check_config: False
avatar-app-1  |   print_config: False
avatar-app-1  |   preload_app: False
avatar-app-1  |   sendfile: None
avatar-app-1  |   reuse_port: False
avatar-app-1  |   chdir: /home/docker
avatar-app-1  |   daemon: False
avatar-app-1  |   raw_env: []
avatar-app-1  |   pidfile: None
avatar-app-1  |   worker_tmp_dir: None
avatar-app-1  |   user: 1000
avatar-app-1  |   group: 1000
avatar-app-1  |   umask: 0
avatar-app-1  |   initgroups: False
avatar-app-1  |   tmp_upload_dir: None
avatar-app-1  |   secure_scheme_headers: {'X-FORWARDED-PROTOCOL': 'ssl', 'X-FORWARDED-PROTO': 'https', 'X-FORWARDED-SSL': 'on'}
avatar-app-1  |   forwarded_allow_ips: ['127.0.0.1', '::1']
avatar-app-1  |   accesslog: None
avatar-app-1  |   disable_redirect_access_to_syslog: False
avatar-app-1  |   access_log_format: %(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"
avatar-app-1  |   errorlog: -
avatar-app-1  |   loglevel: debug
avatar-app-1  |   capture_output: False
avatar-app-1  |   logger_class: gunicorn.glogging.Logger
avatar-app-1  |   logconfig: None
avatar-app-1  |   logconfig_dict: {}
avatar-app-1  |   logconfig_json: None
avatar-app-1  |   syslog_addr: udp://localhost:514
avatar-app-1  |   syslog: False
avatar-app-1  |   syslog_prefix: None
avatar-app-1  |   syslog_facility: user
avatar-app-1  |   enable_stdio_inheritance: False
avatar-app-1  |   statsd_host: None
avatar-app-1  |   dogstatsd_tags: 
avatar-app-1  |   statsd_prefix: 
avatar-app-1  |   proc_name: None
avatar-app-1  |   default_proc_name: API:app
avatar-app-1  |   pythonpath: None
avatar-app-1  |   paste: None
avatar-app-1  |   on_starting: <function OnStarting.on_starting at 0x74d0ccb4a440>
avatar-app-1  |   on_reload: <function OnReload.on_reload at 0x74d0ccb4a560>
avatar-app-1  |   when_ready: <function WhenReady.when_ready at 0x74d0ccb4a680>
avatar-app-1  |   pre_fork: <function Prefork.pre_fork at 0x74d0ccb4a7a0>
avatar-app-1  |   post_fork: <function Postfork.post_fork at 0x74d0ccb4a8c0>
avatar-app-1  |   post_worker_init: <function PostWorkerInit.post_worker_init at 0x74d0ccb4a9e0>
avatar-app-1  |   worker_int: <function WorkerInt.worker_int at 0x74d0ccb4ab00>
avatar-app-1  |   worker_abort: <function WorkerAbort.worker_abort at 0x74d0ccb4ac20>
avatar-app-1  |   pre_exec: <function PreExec.pre_exec at 0x74d0ccb4ad40>
avatar-app-1  |   pre_request: <function PreRequest.pre_request at 0x74d0ccb4ae60>
avatar-app-1  |   post_request: <function PostRequest.post_request at 0x74d0ccb4aef0>
avatar-app-1  |   child_exit: <function ChildExit.child_exit at 0x74d0ccb4b010>
avatar-app-1  |   worker_exit: <function WorkerExit.worker_exit at 0x74d0ccb4b130>
avatar-app-1  |   nworkers_changed: <function NumWorkersChanged.nworkers_changed at 0x74d0ccb4b250>
avatar-app-1  |   on_exit: <function OnExit.on_exit at 0x74d0ccb4b370>
avatar-app-1  |   ssl_context: <function NewSSLContext.ssl_context at 0x74d0ccb4b490>
avatar-app-1  |   proxy_protocol: False
avatar-app-1  |   proxy_allow_ips: ['127.0.0.1', '::1']
avatar-app-1  |   keyfile: None
avatar-app-1  |   certfile: None
avatar-app-1  |   ssl_version: 2
avatar-app-1  |   cert_reqs: 0
avatar-app-1  |   ca_certs: None
avatar-app-1  |   suppress_ragged_eofs: True
avatar-app-1  |   do_handshake_on_connect: False
avatar-app-1  |   ciphers: None
avatar-app-1  |   raw_paste_global_conf: []
avatar-app-1  |   permit_obsolete_folding: False
avatar-app-1  |   strip_header_spaces: False
avatar-app-1  |   permit_unconventional_http_method: False
avatar-app-1  |   permit_unconventional_http_version: False
avatar-app-1  |   casefold_http_method: False
avatar-app-1  |   forwarder_headers: ['SCRIPT_NAME', 'PATH_INFO']
avatar-app-1  |   header_map: drop
avatar-app-1  | [2025-05-15 15:34:29 +0000] [1] [INFO] Starting gunicorn 23.0.0
avatar-app-1  | [2025-05-15 15:34:29 +0000] [1] [DEBUG] Arbiter booted
avatar-app-1  | [2025-05-15 15:34:29 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)
avatar-app-1  | [2025-05-15 15:34:29 +0000] [1] [INFO] Using worker: uvicorn.workers.UvicornWorker
avatar-app-1  | [2025-05-15 15:34:29 +0000] [27] [INFO] Booting worker with pid: 27
avatar-app-1  | [2025-05-15 15:34:29 +0000] [28] [INFO] Booting worker with pid: 28
avatar-app-1  | [2025-05-15 15:34:29 +0000] [29] [INFO] Booting worker with pid: 29
avatar-app-1  | [2025-05-15 15:34:29 +0000] [30] [INFO] Booting worker with pid: 30
avatar-app-1  | [2025-05-15 15:34:29 +0000] [1] [DEBUG] 4 workers
avatar-app-1  | [2025-05-15 15:34:29 +0000] [28] [INFO] Started server process [28]
avatar-app-1  | [2025-05-15 15:34:29 +0000] [27] [INFO] Started server process [27]
avatar-app-1  | [2025-05-15 15:34:29 +0000] [28] [INFO] Waiting for application startup.
avatar-app-1  | [2025-05-15 15:34:29 +0000] [27] [INFO] Waiting for application startup.
avatar-app-1  | [2025-05-15 15:34:29 +0000] [28] [INFO] Application startup complete.
avatar-app-1  | [2025-05-15 15:34:29 +0000] [27] [INFO] Application startup complete.
avatar-app-1  | [2025-05-15 15:34:29 +0000] [29] [INFO] Started server process [29]
avatar-app-1  | [2025-05-15 15:34:29 +0000] [29] [INFO] Waiting for application startup.
avatar-app-1  | [2025-05-15 15:34:29 +0000] [29] [INFO] Application startup complete.
avatar-app-1  | [2025-05-15 15:34:29 +0000] [30] [INFO] Started server process [30]
avatar-app-1  | [2025-05-15 15:34:29 +0000] [30] [INFO] Waiting for application startup.
avatar-app-1  | [2025-05-15 15:34:29 +0000] [30] [INFO] Application startup complete.
avatar-app-1  | [2025-05-15 15:40:42 +0000] [1] [INFO] Handling signal: term
avatar-app-1  | [2025-05-15 15:40:42 +0000] [30] [INFO] Shutting down
avatar-app-1  | [2025-05-15 15:40:42 +0000] [28] [INFO] Shutting down
avatar-app-1  | [2025-05-15 15:40:43 +0000] [29] [INFO] Shutting down
avatar-app-1  | [2025-05-15 15:40:43 +0000] [27] [INFO] Shutting down
avatar-app-1  | [2025-05-15 15:40:43 +0000] [30] [INFO] Waiting for application shutdown.
avatar-app-1  | [2025-05-15 15:40:43 +0000] [30] [INFO] Application shutdown complete.
avatar-app-1  | [2025-05-15 15:40:43 +0000] [30] [INFO] Finished server process [30]
avatar-app-1  | [2025-05-15 15:40:43 +0000] [28] [INFO] Waiting for application shutdown.
avatar-app-1  | [2025-05-15 15:40:43 +0000] [28] [INFO] Application shutdown complete.
avatar-app-1  | [2025-05-15 15:40:43 +0000] [28] [INFO] Finished server process [28]
avatar-app-1  | [2025-05-15 15:40:43 +0000] [1] [ERROR] Worker (pid:30) was sent SIGTERM!
avatar-app-1  | [2025-05-15 15:40:43 +0000] [1] [ERROR] Worker (pid:28) was sent SIGTERM!
avatar-app-1  | [2025-05-15 15:40:43 +0000] [29] [INFO] Waiting for application shutdown.
avatar-app-1  | [2025-05-15 15:40:43 +0000] [29] [INFO] Application shutdown complete.
avatar-app-1  | [2025-05-15 15:40:43 +0000] [29] [INFO] Finished server process [29]
avatar-app-1  | [2025-05-15 15:40:43 +0000] [1] [ERROR] Worker (pid:29) was sent SIGTERM!
avatar-app-1  | [2025-05-15 15:40:43 +0000] [27] [INFO] Waiting for application shutdown.
avatar-app-1  | [2025-05-15 15:40:43 +0000] [27] [INFO] Application shutdown complete.
avatar-app-1  | [2025-05-15 15:40:43 +0000] [27] [INFO] Finished server process [27]
avatar-app-1  | [2025-05-15 15:40:43 +0000] [1] [ERROR] Worker (pid:27) was sent SIGTERM!
avatar-app-1  | [2025-05-15 15:40:43 +0000] [1] [INFO] Shutting down: Master
avatar-app-1  | 
avatar-app-1  | ==========
avatar-app-1  | == CUDA ==
avatar-app-1  | ==========
avatar-app-1  | 
avatar-app-1  | CUDA Version 11.6.2
avatar-app-1  | 
avatar-app-1  | Container image Copyright (c) 2016-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
avatar-app-1  | 
avatar-app-1  | This container image and its contents are governed by the NVIDIA Deep Learning Container License.
avatar-app-1  | By pulling and using the container, you accept the terms and conditions of this license:
avatar-app-1  | https://developer.nvidia.com/ngc/nvidia-deep-learning-container-license
avatar-app-1  | 
avatar-app-1  | A copy of this license is made available in this container at /NGC-DL-CONTAINER-LICENSE for your convenience.
avatar-app-1  | 
avatar-app-1  | [2025-05-15 15:41:12 +0000] [1] [DEBUG] Current configuration:
avatar-app-1  |   config: ./gunicorn.conf.py
avatar-app-1  |   wsgi_app: None
avatar-app-1  |   bind: ['0.0.0.0:8000']
avatar-app-1  |   backlog: 2048
avatar-app-1  |   workers: 4
avatar-app-1  |   worker_class: uvicorn.workers.UvicornWorker
avatar-app-1  |   threads: 1
avatar-app-1  |   worker_connections: 1000
avatar-app-1  |   max_requests: 0
avatar-app-1  |   max_requests_jitter: 0
avatar-app-1  |   timeout: 30
avatar-app-1  |   graceful_timeout: 30
avatar-app-1  |   keepalive: 2
avatar-app-1  |   limit_request_line: 4094
avatar-app-1  |   limit_request_fields: 100
avatar-app-1  |   limit_request_field_size: 8190
avatar-app-1  |   reload: False
avatar-app-1  |   reload_engine: auto
avatar-app-1  |   reload_extra_files: []
avatar-app-1  |   spew: False
avatar-app-1  |   check_config: False
avatar-app-1  |   print_config: False
avatar-app-1  |   preload_app: False
avatar-app-1  |   sendfile: None
avatar-app-1  |   reuse_port: False
avatar-app-1  |   chdir: /home/docker
avatar-app-1  |   daemon: False
avatar-app-1  |   raw_env: []
avatar-app-1  |   pidfile: None
avatar-app-1  |   worker_tmp_dir: None
avatar-app-1  |   user: 1000
avatar-app-1  |   group: 1000
avatar-app-1  |   umask: 0
avatar-app-1  |   initgroups: False
avatar-app-1  |   tmp_upload_dir: None
avatar-app-1  |   secure_scheme_headers: {'X-FORWARDED-PROTOCOL': 'ssl', 'X-FORWARDED-PROTO': 'https', 'X-FORWARDED-SSL': 'on'}
avatar-app-1  |   forwarded_allow_ips: ['127.0.0.1', '::1']
avatar-app-1  |   accesslog: None
avatar-app-1  |   disable_redirect_access_to_syslog: False
avatar-app-1  |   access_log_format: %(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"
avatar-app-1  |   errorlog: -
avatar-app-1  |   loglevel: debug
avatar-app-1  |   capture_output: False
avatar-app-1  |   logger_class: gunicorn.glogging.Logger
avatar-app-1  |   logconfig: None
avatar-app-1  |   logconfig_dict: {}
avatar-app-1  |   logconfig_json: None
avatar-app-1  |   syslog_addr: udp://localhost:514
avatar-app-1  |   syslog: False
avatar-app-1  |   syslog_prefix: None
avatar-app-1  |   syslog_facility: user
avatar-app-1  |   enable_stdio_inheritance: False
avatar-app-1  |   statsd_host: None
avatar-app-1  |   dogstatsd_tags: 
avatar-app-1  |   statsd_prefix: 
avatar-app-1  |   proc_name: None
avatar-app-1  |   default_proc_name: API:app
avatar-app-1  |   pythonpath: None
avatar-app-1  |   paste: None
avatar-app-1  |   on_starting: <function OnStarting.on_starting at 0x739edf0ce440>
avatar-app-1  |   on_reload: <function OnReload.on_reload at 0x739edf0ce560>
avatar-app-1  |   when_ready: <function WhenReady.when_ready at 0x739edf0ce680>
avatar-app-1  |   pre_fork: <function Prefork.pre_fork at 0x739edf0ce7a0>
avatar-app-1  |   post_fork: <function Postfork.post_fork at 0x739edf0ce8c0>
avatar-app-1  |   post_worker_init: <function PostWorkerInit.post_worker_init at 0x739edf0ce9e0>
avatar-app-1  |   worker_int: <function WorkerInt.worker_int at 0x739edf0ceb00>
avatar-app-1  |   worker_abort: <function WorkerAbort.worker_abort at 0x739edf0cec20>
avatar-app-1  |   pre_exec: <function PreExec.pre_exec at 0x739edf0ced40>
avatar-app-1  |   pre_request: <function PreRequest.pre_request at 0x739edf0cee60>
avatar-app-1  |   post_request: <function PostRequest.post_request at 0x739edf0ceef0>
avatar-app-1  |   child_exit: <function ChildExit.child_exit at 0x739edf0cf010>
avatar-app-1  |   worker_exit: <function WorkerExit.worker_exit at 0x739edf0cf130>
avatar-app-1  |   nworkers_changed: <function NumWorkersChanged.nworkers_changed at 0x739edf0cf250>
avatar-app-1  |   on_exit: <function OnExit.on_exit at 0x739edf0cf370>
avatar-app-1  |   ssl_context: <function NewSSLContext.ssl_context at 0x739edf0cf490>
avatar-app-1  |   proxy_protocol: False
avatar-app-1  |   proxy_allow_ips: ['127.0.0.1', '::1']
avatar-app-1  |   keyfile: None
avatar-app-1  |   certfile: None
avatar-app-1  |   ssl_version: 2
avatar-app-1  |   cert_reqs: 0
avatar-app-1  |   ca_certs: None
avatar-app-1  |   suppress_ragged_eofs: True
avatar-app-1  |   do_handshake_on_connect: False
avatar-app-1  |   ciphers: None
avatar-app-1  |   raw_paste_global_conf: []
avatar-app-1  |   permit_obsolete_folding: False
avatar-app-1  |   strip_header_spaces: False
avatar-app-1  |   permit_unconventional_http_method: False
avatar-app-1  |   permit_unconventional_http_version: False
avatar-app-1  |   casefold_http_method: False
avatar-app-1  |   forwarder_headers: ['SCRIPT_NAME', 'PATH_INFO']
avatar-app-1  |   header_map: drop
avatar-app-1  | [2025-05-15 15:41:12 +0000] [1] [INFO] Starting gunicorn 23.0.0
avatar-app-1  | [2025-05-15 15:41:12 +0000] [1] [DEBUG] Arbiter booted
avatar-app-1  | [2025-05-15 15:41:12 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)
avatar-app-1  | [2025-05-15 15:41:12 +0000] [1] [INFO] Using worker: uvicorn.workers.UvicornWorker
avatar-app-1  | [2025-05-15 15:41:12 +0000] [27] [INFO] Booting worker with pid: 27
avatar-app-1  | [2025-05-15 15:41:12 +0000] [28] [INFO] Booting worker with pid: 28
avatar-app-1  | [2025-05-15 15:41:12 +0000] [29] [INFO] Booting worker with pid: 29
avatar-app-1  | [2025-05-15 15:41:12 +0000] [30] [INFO] Booting worker with pid: 30
avatar-app-1  | [2025-05-15 15:41:12 +0000] [1] [DEBUG] 4 workers
avatar-app-1  | [2025-05-15 15:41:12 +0000] [27] [INFO] Started server process [27]
avatar-app-1  | [2025-05-15 15:41:12 +0000] [27] [INFO] Waiting for application startup.
avatar-app-1  | [2025-05-15 15:41:12 +0000] [27] [INFO] Application startup complete.
avatar-app-1  | [2025-05-15 15:41:12 +0000] [28] [INFO] Started server process [28]
avatar-app-1  | [2025-05-15 15:41:12 +0000] [28] [INFO] Waiting for application startup.
avatar-app-1  | [2025-05-15 15:41:12 +0000] [28] [INFO] Application startup complete.
avatar-app-1  | [2025-05-15 15:41:12 +0000] [29] [INFO] Started server process [29]
avatar-app-1  | [2025-05-15 15:41:12 +0000] [29] [INFO] Waiting for application startup.
avatar-app-1  | [2025-05-15 15:41:12 +0000] [29] [INFO] Application startup complete.
avatar-app-1  | [2025-05-15 15:41:12 +0000] [30] [INFO] Started server process [30]
avatar-app-1  | [2025-05-15 15:41:12 +0000] [30] [INFO] Waiting for application startup.
avatar-app-1  | [2025-05-15 15:41:12 +0000] [30] [INFO] Application startup complete.
yaz@gpu:~/tak/GP/AVATAR$ 
