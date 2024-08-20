FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y \
    libsndfile1 \
    ffmpeg \
    libavcodec-extra \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir pydub

EXPOSE 8000

ENTRYPOINT ["python", "tempo_detector.py"]