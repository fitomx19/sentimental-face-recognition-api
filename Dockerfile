FROM --platform=linux/amd64 python:3.9-slim as build

# Instala las bibliotecas necesarias del sistema
RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# Copiar el archivo al destino deseado
COPY facial_expression_model_weights.h5 /root/.deepface/weights/facial_expression_model_weights.h5

CMD gunicorn --bind 0.0.0.0:5000 wsgi:app

