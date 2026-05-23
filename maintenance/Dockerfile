FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    rsync \
    openssh-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

HEALTHCHECK --interval=30s --timeout=30s  --retries=3 \
    CMD rsync --version && ssh -V || exit 1

COPY backup.py .

CMD ["python", "backup.py"]
