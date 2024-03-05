from flask import Flask
from app.routes import routes  # Importa el módulo de rutas
app = Flask(__name__)
from flask_cors import CORS

# Registra las rutas en la aplicación
CORS(app,resources={r"/*":{"origins":"*"}})
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug=True)
