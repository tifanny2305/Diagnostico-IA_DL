FROM python:3.12-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsndfile1 \
    git \
    && rm -rf /var/lib/apt/lists/*

# Crear carpeta de trabajo
WORKDIR /app

# Copiar todo el proyecto
COPY . /app

# Instalar dependencias Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Establecer comando por defecto
CMD ["python", "main.py", "audio.wav"]
