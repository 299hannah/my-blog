from flask import Flask
from config import config_options


def create_app(config_name):
    app = Flask(__name__)

    #creating configurations
    app.config.from_object(config_options[config_name])
    app.config["SECRET_KEY"] = "s3cr3t3k3y"

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .requests import configure_request
    configure_request(app)

    return app
