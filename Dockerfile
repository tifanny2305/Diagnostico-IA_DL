FROM python:3.12-slim

# Instalar dependencias del sistema necesarias para audio y git
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsndfile1 \
    git \
    && rm -rf /var/lib/apt/lists/*

# Crear carpeta de trabajo
WORKDIR /app

# Copiar el proyecto al contenedor
COPY . /app

# Instalar dependencias de Python
RUN pip install --upgrade pip

# Instalar dependencias del proyecto + GraphQL (Strawberry)
RUN pip install -r requirements.txt
RUN pip install strawberry-graphql[fastapi] uvicorn

# Exponer puerto (opcional pero recomendado)
EXPOSE 8000

# Comando por defecto: iniciar el servidor GraphQL
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
