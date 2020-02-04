"""Main initialization module of the Flask application."""

from importlib import import_module

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

import settings


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
csrf = CSRFProtect()


def create_app(env):
    """Factory function responsible for lazy app creation.

    Args:
        environment (str): configuration environment to be used by the app
    
    """
    app = Flask(__name__)
    app.config.from_object(settings.environments[env])
    settings.environments[env].init_app(app)

    # Configuration of extensions
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    csrf.init_app(app)

    # Register app blueprints
    for blueprint in settings.INSTALLED_BLUEPRINTS:
        module = import_module(blueprint["module"])
        app.register_blueprint(
            getattr(module, blueprint["name"]), url_prefix=blueprint["prefix"]
        )

    return app
