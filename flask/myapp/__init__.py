from flask import Flask
from myapp.config import Config
from myapp.main.routes import main


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(main)

    return app
