FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    rsync \
    openssh-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY backup.py .

CMD ["python", "backup.py"]
