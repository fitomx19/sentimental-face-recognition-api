from flask import jsonify
from app.detectar_emociones.deteccion import clasificar_estres_version_2, clasificar_estres_version_3


def obtener_mensaje():
    return "¡Hola, mundo!"

def cargar_imagenes_datos(imagen): 
    nivel_estres,promedio_coeficientes,emocion_predominante,emociones,total_emociones = clasificar_estres_version_2(imagen)
    return jsonify({"nivel_estres": nivel_estres, "promedio_coeficientes": promedio_coeficientes, "emocion_predominante": emocion_predominante , "emociones": emociones , "total_emociones": total_emociones})

def cargar_imagenes_datos_deepface(imagen):
    emociones_ordenadas,coeficientes,emocion_predominante = clasificar_estres_version_3(imagen)
    return jsonify({"emociones_ordenadas": emociones_ordenadas, "coeficientes": coeficientes, "emocion_predominante": emocion_predominante })
