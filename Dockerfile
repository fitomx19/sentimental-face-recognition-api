FROM python:3.9-slim

WORKDIR /app

COPY . .

# Asegúrate de configurar la carpeta de archivos en tu aplicación Flask
# Esto podría depender de cómo está configurada tu aplicación, pero aquí hay un ejemplo:
ENV ARCHIVOS_FOLDER=/app/archivos
RUN mkdir -p $ARCHIVOS_FOLDER

RUN pip install -r requirements.txt

# Configura otros aspectos del contenedor...

# CMD original
CMD gunicorn --bind 0.0.0.0:5000 wsgi:app