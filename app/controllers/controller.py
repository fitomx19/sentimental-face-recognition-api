from services.service import obtener_mensaje

def obtener_mensaje_controlador():
    mensaje = obtener_mensaje()
    return {"message": mensaje}
