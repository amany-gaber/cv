# Stage 1: Build dependencies
FROM ubuntu:20.04 AS builder-image

ARG DEBIAN_FRONTEND=noninteractive

# Install dependencies and clean up
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.9 \
    python3.9-dev \
    python3.9-venv \
    python3-pip \
    python3-wheel \
    build-essential \
    git \
    ffmpeg \
    && apt-get -y autoremove && apt-get clean autoclean && rm -rf /var/lib/apt/lists/*

# Set up Python virtual environment
RUN python3.9 -m venv /home/docker/venv
ENV PATH="/home/docker/venv/bin:$PATH"

# Upgrade pip and install requirements
RUN python3.9 -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final image to run the app
FROM ubuntu:20.04 AS runner-image

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.9 \
    python3-venv \
    ffmpeg \
    && apt-get -y autoremove && apt-get clean autoclean && rm -rf /var/lib/apt/lists/*

# Create a non-root user to run the application
RUN useradd --create-home docker

# Copy the virtual environment from the builder stage
COPY --from=builder-image /home/docker/venv /home/docker/venv

# Switch to the 'docker' user and set the working directory
USER docker
RUN mkdir /home/docker/app
WORKDIR /home/docker/app

# Copy the app source code and fix permissions
COPY --chown=docker:docker ./src .
RUN chmod -R u+rwX /home/docker/app

# Expose theმოდ

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/home/docker/venv
ENV PATH="/home/docker/venv/bin:$PATH"

# Command to run the application
CMD ["uvicorn", "routes.user:app", "--host", "0.0.0.0", "--port", "4004", \
     "--workers", "3", "--log-level", "debug", "--timeout-keep-alive", "1000"]