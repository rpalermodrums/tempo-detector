# Use an official Python runtime as the base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libsndfile1 \
    ffmpeg \
    libavcodec-extra \
    && rm -rf /var/lib/apt/lists/*

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install additional AudioRead backend
RUN pip install --no-cache-dir pydub

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run tempo_detector.py when the container launches
ENTRYPOINT ["python", "tempo_detector.py"]