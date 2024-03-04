from app.services.service import obtener_mensaje, cargar_imagenes_datos

def obtener_mensaje_controlador():
    mensaje = obtener_mensaje()
    return {"message": mensaje}

def cargar_imagenes(imagen):
    print("Cargando imagen...")
    # Llama a la función para cargar imágenes de forma asíncrona
    datos = cargar_imagenes_datos(imagen)
    return datos
