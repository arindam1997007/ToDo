from flask import Flask
from .extensions import mongo
from .main.routes import main


def create_app():
    app = Flask(__name__)

    # Initializing MONGO URI with DB url
    app.config['MONGO_URI'] = '"

    # Initializing mongo with Flask object as argument
    app.register_blueprint(main)
    mongo.init_app(app)
    return app
