# Use NVIDIA base image for GPU support with CUDA 11.8.0
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04

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

# Command to run the application as a module
# Command to run the FastAPI application with gunicorn and uvicorn workers with debug logging
CMD ["/home/docker/venv/bin/gunicorn", "--log-level", "debug", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000", "API:app"]
