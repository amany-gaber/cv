from os import listdir, path
import scipy, cv2, os, sys, argparse, audio
import numpy as np
import json, subprocess, random, string
from tqdm import tqdm
from glob import glob
import torch, face_detection
from models import Wav2Lip
import platform






fastapi==0.115.0
uvicorn==0.32.0
gunicorn==23.0.0
pydantic==2.9.2
librosa==0.10.2
numpy==1.26.4
opencv-python==4.10.0.84
opencv-contrib-python==4.10.0.84
torch==2.4.1
torchvision==0.19.1
python-multipart==0.0.12
#numpy==1.17.1

scipy
sys
random
string

















# Use NVIDIA base image for GPU support with CUDA 11.6.2 (since 11.8.0 not found)
FROM nvidia/cuda:11.6.2-cudnn8-runtime-ubuntu20.04

# Install dependencies for adding a new PPA
RUN apt-get update && apt-get install -y \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Add deadsnakes PPA for Python 3.10
RUN add-apt-repository ppa:deadsnakes/ppa -y

# Install Python 3.10 and dependencies
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3.10-venv \
    python3.10-distutils \
    python3-pip \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Set Python 3.10 as default
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.10 1

# Install pip for Python 3.10
RUN python3.10 -m ensurepip --upgrade
RUN python3.10 -m pip install --upgrade pip

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a non-root user 'docker'
RUN useradd -m -s /bin/bash docker

# Set working directory
WORKDIR /home/docker

# Create directories
RUN mkdir -p /home/docker/Wav2Lip /home/docker/source /home/docker/videos /home/docker/weights

# Copy project files
COPY API.py inference.py lipsync.py lipsync_test.py Wav2Lip_inference_patched.py requirements.txt /home/docker/
COPY Wav2Lip/ /home/docker/Wav2Lip/
COPY source/ /home/docker/source/
COPY weights/ /home/docker/weights/

# Change ownership to docker user
RUN chown -R docker:docker /home/docker

# Switch to docker user
USER docker

# Create virtual environment
RUN python3 -m venv /home/docker/venv

# Upgrade pip and install dependencies
RUN /home/docker/venv/bin/pip install --no-cache-dir --upgrade pip
RUN /home/docker/venv/bin/pip install --no-cache-dir -r requirements.txt

# Install numpy explicitly to ensure it's installed
RUN /home/docker/venv/bin/pip install --no-cache-dir numpy==1.26.4

# Install gunicorn explicitly
RUN /home/docker/venv/bin/pip install --no-cache-dir gunicorn

# Switch to root to set permissions
USER root
RUN chown -R docker:docker /home/docker /home/docker/venv
RUN chmod -R u+rwX /home/docker /home/docker/venv

# Switch back to docker user
USER docker

# Expose port
EXPOSE 8000

# Command to run the FastAPI application with gunicorn and uvicorn workers with debug logging
CMD ["/home/docker/venv/bin/gunicorn", "--log-level", "debug", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000", "API:app"]



















yaz@gpu:~/tak/GP/AVATAR$ docker compose up -d
[+] Running 1/1
 ✔ Container avatar-avatar-app-1  Started                                                                                                                               0.4s 
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
avatar-app-1  | [2025-05-16 19:28:49 +0000] [1] [DEBUG] Current configuration:
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
avatar-app-1  |   on_starting: <function OnStarting.on_starting at 0x76e17150e440>
avatar-app-1  |   on_reload: <function OnReload.on_reload at 0x76e17150e560>
avatar-app-1  |   when_ready: <function WhenReady.when_ready at 0x76e17150e680>
avatar-app-1  |   pre_fork: <function Prefork.pre_fork at 0x76e17150e7a0>
avatar-app-1  |   post_fork: <function Postfork.post_fork at 0x76e17150e8c0>
avatar-app-1  |   post_worker_init: <function PostWorkerInit.post_worker_init at 0x76e17150e9e0>
avatar-app-1  |   worker_int: <function WorkerInt.worker_int at 0x76e17150eb00>
avatar-app-1  |   worker_abort: <function WorkerAbort.worker_abort at 0x76e17150ec20>
avatar-app-1  |   pre_exec: <function PreExec.pre_exec at 0x76e17150ed40>
avatar-app-1  |   pre_request: <function PreRequest.pre_request at 0x76e17150ee60>
avatar-app-1  |   post_request: <function PostRequest.post_request at 0x76e17150eef0>
avatar-app-1  |   child_exit: <function ChildExit.child_exit at 0x76e17150f010>
avatar-app-1  |   worker_exit: <function WorkerExit.worker_exit at 0x76e17150f130>
avatar-app-1  |   nworkers_changed: <function NumWorkersChanged.nworkers_changed at 0x76e17150f250>
avatar-app-1  |   on_exit: <function OnExit.on_exit at 0x76e17150f370>
avatar-app-1  |   ssl_context: <function NewSSLContext.ssl_context at 0x76e17150f490>
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
avatar-app-1  | [2025-05-16 19:28:49 +0000] [1] [INFO] Starting gunicorn 23.0.0
avatar-app-1  | [2025-05-16 19:28:49 +0000] [1] [DEBUG] Arbiter booted
avatar-app-1  | [2025-05-16 19:28:49 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)
avatar-app-1  | [2025-05-16 19:28:49 +0000] [1] [INFO] Using worker: uvicorn.workers.UvicornWorker
avatar-app-1  | [2025-05-16 19:28:49 +0000] [27] [INFO] Booting worker with pid: 27
avatar-app-1  | [2025-05-16 19:28:49 +0000] [28] [INFO] Booting worker with pid: 28
avatar-app-1  | [2025-05-16 19:28:49 +0000] [29] [INFO] Booting worker with pid: 29
avatar-app-1  | [2025-05-16 19:28:49 +0000] [30] [INFO] Booting worker with pid: 30
avatar-app-1  | [2025-05-16 19:28:49 +0000] [1] [DEBUG] 4 workers
avatar-app-1  | [2025-05-16 19:28:49 +0000] [27] [INFO] Started server process [27]
avatar-app-1  | [2025-05-16 19:28:49 +0000] [27] [INFO] Waiting for application startup.
avatar-app-1  | [2025-05-16 19:28:49 +0000] [27] [INFO] Application startup complete.
avatar-app-1  | [2025-05-16 19:28:50 +0000] [28] [INFO] Started server process [28]
avatar-app-1  | [2025-05-16 19:28:50 +0000] [28] [INFO] Waiting for application startup.
avatar-app-1  | [2025-05-16 19:28:50 +0000] [28] [INFO] Application startup complete.
avatar-app-1  | [2025-05-16 19:28:50 +0000] [30] [INFO] Started server process [30]
avatar-app-1  | [2025-05-16 19:28:50 +0000] [30] [INFO] Waiting for application startup.
avatar-app-1  | [2025-05-16 19:28:50 +0000] [30] [INFO] Application startup complete.
avatar-app-1  | [2025-05-16 19:28:50 +0000] [29] [INFO] Started server process [29]
avatar-app-1  | [2025-05-16 19:28:50 +0000] [29] [INFO] Waiting for application startup.
avatar-app-1  | [2025-05-16 19:28:50 +0000] [29] [INFO] Application startup complete.
avatar-app-1  | [2025-05-16 19:29:54 +0000] [1] [INFO] Handling signal: term
avatar-app-1  | [2025-05-16 19:29:54 +0000] [27] [INFO] Shutting down
avatar-app-1  | [2025-05-16 19:29:54 +0000] [29] [INFO] Shutting down
avatar-app-1  | [2025-05-16 19:29:54 +0000] [30] [INFO] Shutting down
avatar-app-1  | [2025-05-16 19:29:54 +0000] [28] [INFO] Shutting down
avatar-app-1  | [2025-05-16 19:29:54 +0000] [27] [INFO] Waiting for application shutdown.
avatar-app-1  | [2025-05-16 19:29:54 +0000] [27] [INFO] Application shutdown complete.
avatar-app-1  | [2025-05-16 19:29:54 +0000] [27] [INFO] Finished server process [27]
avatar-app-1  | [2025-05-16 19:29:54 +0000] [1] [ERROR] Worker (pid:27) was sent SIGTERM!
avatar-app-1  | [2025-05-16 19:29:54 +0000] [29] [INFO] Waiting for application shutdown.
avatar-app-1  | [2025-05-16 19:29:54 +0000] [29] [INFO] Application shutdown complete.
avatar-app-1  | [2025-05-16 19:29:54 +0000] [29] [INFO] Finished server process [29]
avatar-app-1  | [2025-05-16 19:29:54 +0000] [30] [INFO] Waiting for application shutdown.
avatar-app-1  | [2025-05-16 19:29:54 +0000] [30] [INFO] Application shutdown complete.
avatar-app-1  | [2025-05-16 19:29:54 +0000] [30] [INFO] Finished server process [30]
avatar-app-1  | [2025-05-16 19:29:54 +0000] [1] [ERROR] Worker (pid:29) was sent SIGTERM!
avatar-app-1  | [2025-05-16 19:29:54 +0000] [1] [ERROR] Worker (pid:30) was sent SIGTERM!
avatar-app-1  | [2025-05-16 19:29:54 +0000] [28] [INFO] Waiting for application shutdown.
avatar-app-1  | [2025-05-16 19:29:54 +0000] [28] [INFO] Application shutdown complete.
avatar-app-1  | [2025-05-16 19:29:54 +0000] [28] [INFO] Finished server process [28]
avatar-app-1  | [2025-05-16 19:29:54 +0000] [1] [ERROR] Worker (pid:28) was sent SIGTERM!
avatar-app-1  | [2025-05-16 19:29:54 +0000] [1] [INFO] Shutting down: Master
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
avatar-app-1  | [2025-05-16 19:30:12 +0000] [1] [DEBUG] Current configuration:
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
avatar-app-1  |   on_starting: <function OnStarting.on_starting at 0x717c05132440>
avatar-app-1  |   on_reload: <function OnReload.on_reload at 0x717c05132560>
avatar-app-1  |   when_ready: <function WhenReady.when_ready at 0x717c05132680>
avatar-app-1  |   pre_fork: <function Prefork.pre_fork at 0x717c051327a0>
avatar-app-1  |   post_fork: <function Postfork.post_fork at 0x717c051328c0>
avatar-app-1  |   post_worker_init: <function PostWorkerInit.post_worker_init at 0x717c051329e0>
avatar-app-1  |   worker_int: <function WorkerInt.worker_int at 0x717c05132b00>
avatar-app-1  |   worker_abort: <function WorkerAbort.worker_abort at 0x717c05132c20>
avatar-app-1  |   pre_exec: <function PreExec.pre_exec at 0x717c05132d40>
avatar-app-1  |   pre_request: <function PreRequest.pre_request at 0x717c05132e60>
avatar-app-1  |   post_request: <function PostRequest.post_request at 0x717c05132ef0>
avatar-app-1  |   child_exit: <function ChildExit.child_exit at 0x717c05133010>
avatar-app-1  |   worker_exit: <function WorkerExit.worker_exit at 0x717c05133130>
avatar-app-1  |   nworkers_changed: <function NumWorkersChanged.nworkers_changed at 0x717c05133250>
avatar-app-1  |   on_exit: <function OnExit.on_exit at 0x717c05133370>
avatar-app-1  |   ssl_context: <function NewSSLContext.ssl_context at 0x717c05133490>
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
avatar-app-1  | [2025-05-16 19:30:12 +0000] [1] [INFO] Starting gunicorn 23.0.0
avatar-app-1  | [2025-05-16 19:30:12 +0000] [1] [DEBUG] Arbiter booted
avatar-app-1  | [2025-05-16 19:30:12 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)
avatar-app-1  | [2025-05-16 19:30:12 +0000] [1] [INFO] Using worker: uvicorn.workers.UvicornWorker
avatar-app-1  | [2025-05-16 19:30:12 +0000] [27] [INFO] Booting worker with pid: 27
avatar-app-1  | [2025-05-16 19:30:12 +0000] [28] [INFO] Booting worker with pid: 28
avatar-app-1  | [2025-05-16 19:30:12 +0000] [29] [INFO] Booting worker with pid: 29
avatar-app-1  | [2025-05-16 19:30:12 +0000] [30] [INFO] Booting worker with pid: 30
avatar-app-1  | [2025-05-16 19:30:12 +0000] [1] [DEBUG] 4 workers
avatar-app-1  | [2025-05-16 19:30:12 +0000] [27] [INFO] Started server process [27]
avatar-app-1  | [2025-05-16 19:30:12 +0000] [27] [INFO] Waiting for application startup.
avatar-app-1  | [2025-05-16 19:30:12 +0000] [27] [INFO] Application startup complete.
avatar-app-1  | [2025-05-16 19:30:12 +0000] [28] [INFO] Started server process [28]
avatar-app-1  | [2025-05-16 19:30:12 +0000] [28] [INFO] Waiting for application startup.
avatar-app-1  | [2025-05-16 19:30:12 +0000] [28] [INFO] Application startup complete.
avatar-app-1  | [2025-05-16 19:30:12 +0000] [29] [INFO] Started server process [29]
avatar-app-1  | [2025-05-16 19:30:12 +0000] [29] [INFO] Waiting for application startup.
avatar-app-1  | [2025-05-16 19:30:12 +0000] [29] [INFO] Application startup complete.
avatar-app-1  | [2025-05-16 19:30:12 +0000] [30] [INFO] Started server process [30]
avatar-app-1  | [2025-05-16 19:30:12 +0000] [30] [INFO] Waiting for application startup.
avatar-app-1  | [2025-05-16 19:30:12 +0000] [30] [INFO] Application startup complete.
yaz@gpu:~/tak/GP/AVATAR$ ls
API.py  docker-compose.yml  inference.py  lipsync_test.py  requirements.txt  videos   Wav2Lip_inference_patched.py
cache   dockerfile          lipsync.py    __pycache__      source            Wav2Lip  weights
yaz@gpu:~/tak/GP/AVATAR$ cd videos
yaz@gpu:~/tak/GP/AVATAR/videos$ ls
yaz@gpu:~/tak/GP/AVATAR/videos$ cd ..
yaz@gpu:~/tak/GP/AVATAR$ cd cache
yaz@gpu:~/tak/GP/AVATAR/cache$ ls
final.mp4.pk
yaz@gpu:~/tak/GP/AVATAR/cache$ cd ..
yaz@gpu:~/tak/GP/AVATAR$ cd source
yaz@gpu:~/tak/GP/AVATAR/source$ ls
audio.wav  final.mp4
yaz@gpu:~/tak/GP/AVATAR/source$ cd ..
yaz@gpu:~/tak/GP/AVATAR$ cd Wav2Lip
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip$ ls
audio.py     color_syncnet_train.py  face_detection  hparams.py           inference.py       models         __pycache__  requirements.txt  temp
checkpoints  evaluation              filelists       hq_wav2lip_train.py  inference.py.save  preprocess.py  README.md    results           wav2lip_train.py
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip$ cd face_detection
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/face_detection$ ls
api.py  detection  __init__.py  models.py  __pycache__  README.md  utils.py
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/face_detection$ cd detection
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/face_detection/detection$ ls
core.py  __init__.py  __pycache__  sfd
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/face_detection/detection$ cd sfd
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/face_detection/detection/sfd$ ls
bbox.py  detect.py  __init__.py  net_s3fd.py  __pycache__  sfd_detector.py
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/face_detection/detection/sfd$ cd ..
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/face_detection/detection$ 
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/face_detection/detection$ cd ..
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/face_detection$ cd ..
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip$ ls
audio.py     color_syncnet_train.py  face_detection  hparams.py           inference.py       models         __pycache__  requirements.txt  temp
checkpoints  evaluation              filelists       hq_wav2lip_train.py  inference.py.save  preprocess.py  README.md    results           wav2lip_train.py
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip$ cd models
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ ls
conv.py  __init__.py  __pycache__  syncnet.py  wav2lip.py
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ cd ..
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip$ cd temp
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/temp$ ls
README.md
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/temp$ cd ..
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip$ cd evaluation
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/evaluation$ ls
gen_videos_from_filelist.py  README.md  real_videos_inference.py  scores_LSE  test_filelists
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/evaluation$ cd source_LSE
bash: cd: source_LSE: No such file or directory
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/evaluation$ cd scores_LSE
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/evaluation/scores_LSE$ LS
LS: command not found
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/evaluation/scores_LSE$ ls
calculate_scores_LRS.py  calculate_scores_real_videos.py  calculate_scores_real_videos.sh  SyncNetInstance_calc_scores.py
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/evaluation/scores_LSE$ cd ..
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/evaluation$ cd ..
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip$ ls
audio.py     color_syncnet_train.py  face_detection  hparams.py           inference.py       models         __pycache__  requirements.txt  temp
checkpoints  evaluation              filelists       hq_wav2lip_train.py  inference.py.save  preprocess.py  README.md    results           wav2lip_train.py
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip$ cd results
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/results$ ls
README.md
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/results$ cd ..
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip$ cd ..
yaz@gpu:~/tak/GP/AVATAR$ ls
API.py  docker-compose.yml  inference.py  lipsync_test.py  requirements.txt  videos   Wav2Lip_inference_patched.py
cache   dockerfile          lipsync.py    __pycache__      source            Wav2Lip  weights
yaz@gpu:~/tak/GP/AVATAR$ cd weights
yaz@gpu:~/tak/GP/AVATAR/weights$ ls
wav2lip.pth
yaz@gpu:~/tak/GP/AVATAR/weights$ cd ..
yaz@gpu:~/tak/GP/AVATAR$ 


----------------------------------------------------------------
when I test on swagger with wav sound or opus 
                                                               the result is Error: Internal Server Error
Response body

{
  "error": "Wav2Lip failed: Traceback (most recent call last):\n  File \"/home/docker/Wav2Lip/inference.py\", line 2, in <module>\n    import numpy as np\nModuleNotFoundError: No module named 'numpy'\n"
}






tell me t=what do you want to solve this problem 
                                                               ask if you want on anything like any file content that will help to solve the problem 
but note that this docker file build the api corret so try to keep it works also okay ?






