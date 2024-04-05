from flask import Flask
from flask_cors import CORS
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

from src.main.routes.eventoRoutes import eventoRoute_bp
from src.main.routes.participantesRoutes import participantesRoute_bp
from src.main.routes.checkInRoutes import checkInRoutes_bp

app.register_blueprint(eventoRoute_bp)
app.register_blueprint(participantesRoute_bp)
app.register_blueprint(checkInRoutes_bp)
