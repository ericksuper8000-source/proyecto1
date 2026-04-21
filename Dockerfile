# Usamos una imagen ligera de Python
FROM python:3.10-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos de requerimientos primero (para aprovechar la caché de Docker)
COPY requirements.txt .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código (Principal.py y test_Principal.py)
COPY . .

# Comando por defecto al iniciar el contenedor (ejecutar las pruebas)
CMD ["python", "test_Principal.py"]
