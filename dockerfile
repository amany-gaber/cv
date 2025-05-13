# Use the official Python 3.11 slim image as the base
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory
COPY . .

# Expose the port FastAPI will run on
EXPOSE 7410

# Command to run the FastAPI application
CMD ["uvicorn", "API:app", "--host", "0.0.0.0", "--port", "7410"]