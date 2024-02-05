from flask import Flask
from .routes import routes  # Importa el módulo de rutas
app = Flask(__name__)

# Registra las rutas en la aplicación
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug=True)
