from PIL import Image
import numpy as np
from flask import Flask, jsonify, request

from app.routes import routes  # Importa el Blueprint
from app.controllers.controller import cargar_imagenes  # Importa el controlador


@routes.route('/')
async def index():
    return jsonify({"message": "¡Hola, mundo!"})

@routes.route('/cargar_imagenes', methods=['POST'])
async def cargar_imagenes_asincrono():
    # Asegúrate de manejar adecuadamente la imagen que recibes del cliente
    imagen = request.files['imagen']
    imagen_np = cargar_imagen_desde_archivo(imagen)
    respuesta = cargar_imagenes(imagen_np)
    return respuesta

def cargar_imagen_desde_archivo(archivo):
    # Abre la imagen utilizando PIL y conviértela en una matriz numpy
    imagen = Image.open(archivo)
    imagen_np = np.array(imagen)
    return imagen_np
