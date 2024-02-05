from flask import Blueprint

# Crea el objeto Blueprint
routes = Blueprint('routes', __name__)

# Importa las rutas del archivo routes.py
from .routes import *
