# Python 3.11 slim - base for the app (Phase 5: portability)
FROM python:3.11-slim

# Avoid .pyc and enable unbuffered logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install deps first for layer cache (only re-installs when requirements.txt changes)
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy app code (respects .dockerignore: excludes .git, __pycache__, .venv, docs, etc.)
COPY Principal.py .

# Run as non-root is ideal; kept simple for Phase 5 (hardened in Phase 10/12 with USER)
CMD ["python", "Principal.py"]
