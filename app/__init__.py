from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# from flask_bcrypt import Bcrypt

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'


db = SQLAlchemy()
# bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)

    #creating configurations
    app.config.from_object(config_options[config_name])
    app.config["SECRET_KEY"] = "s3cr3t3k3y"
    

   

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

     # Initializing flask extensions
    db.init_app(app)
    login_manager.init_app(app)

    from .requests import configure_request
    configure_request(app)
    

   
    return app
