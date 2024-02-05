from flask import jsonify
from app.routes import routes  # Importa el Blueprint

@routes.route('/')
def index():
    return jsonify({"message": "¡Hola, mundo!"})
