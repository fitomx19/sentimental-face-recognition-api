from flask import jsonify
from app.detectar_emociones.deteccion import clasificar_estres_version_2

def obtener_mensaje():
    return "¡Hola, mundo!"

def cargar_imagenes_datos(imagen): 
    print("Cargando imagen...")
    # Aquí se cargarían las imágenes

    nivel_estres,promedio_coeficientes,emocion_predominante = clasificar_estres_version_2(imagen)

    return jsonify({"nivel_estres": nivel_estres, "promedio_coeficientes": promedio_coeficientes, "emocion_predominante": emocion_predominante})
