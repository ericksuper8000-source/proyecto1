# 1. Imagen base
FROM python:3.10-slim

# 2. Entorno (opcional pero recomendado)
ENV PYTHONUNBUFFERED=1

# 3. Directorio de trabajo
WORKDIR /app

# 4. Instalación de dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar el código
COPY . .

# 6. Comando de ejecución
CMD ["python", "Principal.py"]