yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose down
[+] Running 2/2
 ✔ Container avatar-avatar-app-1  Removed                                                                                                                               0.0s 
 ✔ Network avatar_default         Removed                                                                                                                               0.2s 
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose up --build
Compose can now delegate builds to bake for better performance.
 To do so, set COMPOSE_BAKE=true.
[+] Building 0.6s (28/28) FINISHED                                                                                                                            docker:default
 => [avatar-app internal] load build definition from dockerfile                                                                                                         0.0s
 => => transferring dockerfile: 2.31kB                                                                                                                                  0.0s
 => [avatar-app internal] load metadata for docker.io/nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04                                                                     0.5s
 => [avatar-app internal] load .dockerignore                                                                                                                            0.0s
 => => transferring context: 2B                                                                                                                                         0.0s
 => [avatar-app  1/22] FROM docker.io/nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04@sha256:c2336dadc71ae5b5ce490a55cc0100d876287d28f429a5d2840c8a3a8e86fef0             0.0s
 => [avatar-app internal] load build context                                                                                                                            0.0s
 => => transferring context: 7.33kB                                                                                                                                     0.0s
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
 => => writing image sha256:632cf6c03fce37938bc6f53d193e175b76e81bc47e53e7d7941c7f833fa77642                                                                            0.0s
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
avatar-app-1  | [2025-05-15 12:29:11 +0000] [1] [DEBUG] Current configuration:
avatar-app-1  |   config: ./gunicorn.conf.py
avatar-app-1  |   wsgi_app: None
avatar-app-1  |   bind: ['0.0.0.0:4036']
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
avatar-app-1  |   on_starting: <function OnStarting.on_starting at 0x72819ba4e440>
avatar-app-1  |   on_reload: <function OnReload.on_reload at 0x72819ba4e560>
avatar-app-1  |   when_ready: <function WhenReady.when_ready at 0x72819ba4e680>
avatar-app-1  |   pre_fork: <function Prefork.pre_fork at 0x72819ba4e7a0>
avatar-app-1  |   post_fork: <function Postfork.post_fork at 0x72819ba4e8c0>
avatar-app-1  |   post_worker_init: <function PostWorkerInit.post_worker_init at 0x72819ba4e9e0>
avatar-app-1  |   worker_int: <function WorkerInt.worker_int at 0x72819ba4eb00>
avatar-app-1  |   worker_abort: <function WorkerAbort.worker_abort at 0x72819ba4ec20>
avatar-app-1  |   pre_exec: <function PreExec.pre_exec at 0x72819ba4ed40>
avatar-app-1  |   pre_request: <function PreRequest.pre_request at 0x72819ba4ee60>
avatar-app-1  |   post_request: <function PostRequest.post_request at 0x72819ba4eef0>
avatar-app-1  |   child_exit: <function ChildExit.child_exit at 0x72819ba4f010>
avatar-app-1  |   worker_exit: <function WorkerExit.worker_exit at 0x72819ba4f130>
avatar-app-1  |   nworkers_changed: <function NumWorkersChanged.nworkers_changed at 0x72819ba4f250>
avatar-app-1  |   on_exit: <function OnExit.on_exit at 0x72819ba4f370>
avatar-app-1  |   ssl_context: <function NewSSLContext.ssl_context at 0x72819ba4f490>
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
avatar-app-1  | [2025-05-15 12:29:11 +0000] [1] [INFO] Starting gunicorn 23.0.0
avatar-app-1  | [2025-05-15 12:29:11 +0000] [1] [DEBUG] Arbiter booted
avatar-app-1  | [2025-05-15 12:29:11 +0000] [1] [INFO] Listening at: http://0.0.0.0:4036 (1)
avatar-app-1  | [2025-05-15 12:29:11 +0000] [1] [INFO] Using worker: uvicorn.workers.UvicornWorker
avatar-app-1  | [2025-05-15 12:29:11 +0000] [27] [INFO] Booting worker with pid: 27
avatar-app-1  | [2025-05-15 12:29:11 +0000] [28] [INFO] Booting worker with pid: 28
avatar-app-1  | [2025-05-15 12:29:11 +0000] [29] [INFO] Booting worker with pid: 29
avatar-app-1  | [2025-05-15 12:29:12 +0000] [30] [INFO] Booting worker with pid: 30
avatar-app-1  | [2025-05-15 12:29:12 +0000] [1] [DEBUG] 4 workers
avatar-app-1  | [2025-05-15 12:29:12 +0000] [27] [INFO] Started server process [27]
avatar-app-1  | [2025-05-15 12:29:12 +0000] [27] [INFO] Waiting for application startup.
avatar-app-1  | [2025-05-15 12:29:12 +0000] [27] [INFO] Application startup complete.
avatar-app-1  | [2025-05-15 12:29:12 +0000] [28] [INFO] Started server process [28]
avatar-app-1  | [2025-05-15 12:29:12 +0000] [28] [INFO] Waiting for application startup.
avatar-app-1  | [2025-05-15 12:29:12 +0000] [28] [INFO] Application startup complete.
avatar-app-1  | [2025-05-15 12:29:12 +0000] [29] [INFO] Started server process [29]
avatar-app-1  | [2025-05-15 12:29:12 +0000] [29] [INFO] Waiting for application startup.
avatar-app-1  | [2025-05-15 12:29:12 +0000] [29] [INFO] Application startup complete.
avatar-app-1  | [2025-05-15 12:29:12 +0000] [30] [INFO] Started server process [30]
avatar-app-1  | [2025-05-15 12:29:12 +0000] [30] [INFO] Waiting for application startup.
avatar-app-1  | [2025-05-15 12:29:12 +0000] [30] [INFO] Application startup complete.
Gracefully stopping... (press Ctrl+C again to force)
[+] Stopping 1/1
 ✔ Container avatar-avatar-app-1  Stopped                                                                                                                               0.4s 
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose up -d 
[+] Running 1/1
 ✔ Container avatar-avatar-app-1  Started                                                                                                                               0.4s 
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker ps -a
CONTAINER ID   IMAGE                                              COMMAND                  CREATED              STATUS                          PORTS                                                                                                                                       NAMES
d64fe8aa88d6   avatar-app                                         "/opt/nvidia/nvidia_…"   About a minute ago   Up 19 seconds                   0.0.0.0:4036->8000/tcp, [::]:4036->8000/tcp  
