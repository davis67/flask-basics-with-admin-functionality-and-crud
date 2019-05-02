#third party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

#local imports
from config import app_config

#db variable initialisation
db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this Page"
    login_manager.login_view = "auth.login"
    migrate = Migrate(app, db)
    Bootstrap(app)
    from app import models
    #admin
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint,url_prefix='/admin')

    #auth
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    #home
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app