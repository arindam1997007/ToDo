from flask import Flask
from .extensions import mongo
from .main.routes import main


def create_app():
    app = Flask(__name__)

    # Initializing MONGO URI with DB url
    app.config['MONGO_URI'] = 'mongodb+srv://admin:admin@cluster0.c6mva.mongodb.net/mydb?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE'

    # Initializing mongo with Flask object as argument
    app.register_blueprint(main)
    mongo.init_app(app)
    return app
