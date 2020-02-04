"""Main initialization module of the Flask application."""

from importlib import import_module

from flask import Flask
{%- if cookiecutter.use_flask_bootstrap == 'y' %}
from flask_bootstrap import Bootstrap{% endif %}
{%- if cookiecutter.use_flask_mail == 'y' %}
from flask_mail import Mail{% endif %}
{%- if cookiecutter.use_flask_moment == 'y' %}
from flask_moment import Moment{% endif %}
{%- if cookiecutter.use_flask_sqlalchemy == 'y' %}
from flask_sqlalchemy import SQLAlchemy{% endif %}
{%- if cookiecutter.use_flask_wtf == 'y' %}
from flask_wtf.csrf import CSRFProtect{% endif %}

import settings

{%- if cookiecutter.use_flask_bootstrap == 'y' %}
bootstrap = Bootstrap(){% endif %}
{%- if cookiecutter.use_flask_mail == 'y' %}
mail = Mail(){% endif %}
{%- if cookiecutter.use_flask_moment == 'y' %}
moment = Moment(){% endif %}
{%- if cookiecutter.use_flask_sqlalchemy == 'y' %}
db = SQLAlchemy(){% endif %}
{%- if cookiecutter.use_flask_wtf == 'y' %}
csrf = CSRFProtect(){% endif %}

def create_app(env):
    """Factory function responsible for lazy app creation.

    Args:
        environment (str): configuration environment to be used by the app
    
    """
    app = Flask(__name__)
    app.config.from_object(settings.environments[env])
    settings.environments[env].init_app(app)

    # Configuration of extensions
    {%- if cookiecutter.use_flask_bootstrap == 'y' %}
    bootstrap.init_app(app){% endif %}
    {%- if cookiecutter.use_flask_mail == 'y' %}
    mail.init_app(app){% endif %}
    {%- if cookiecutter.use_flask_moment == 'y' %}
    moment.init_app(app){% endif %}
    {%- if cookiecutter.use_flask_sqlalchemy == 'y' %}
    db.init_app(app){% endif %}
    {%- if cookiecutter.use_flask_wtf == 'y' %}
    csrf.init_app(app){% endif %}

    # Register app blueprints
    for blueprint in settings.INSTALLED_BLUEPRINTS:
        module = import_module(blueprint["module"])
        app.register_blueprint(
            getattr(module, blueprint["name"]), url_prefix=blueprint["prefix"]
        )

    return app
