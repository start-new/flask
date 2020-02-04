import os
import pathlib


BASE_DIR = pathlib.Path(__file__).resolve().parent


INSTALLED_BLUEPRINTS = [
    {
        "module": "{{ cookiecutter.project_app_package }}.main",
        "name": "main",
        "prefix": "",
    }
]


class Environment:
    SECRET_KEY = os.environ.get("SECRET_KEY", "very secret and unguessable value") 
    {%- if cookiecutter.use_flask_sqlalchemy == 'y' %}
    SQLALCHEMY_TRACK_MODIFICATIONS = False{% endif %}

    @staticmethod
    def init_app(app):
        pass


class DevelopmentEnvironment(Environment):
    DEBUG = True
    {%- if cookiecutter.use_flask_sqlalchemy == 'y' %}
    SQLALCHEMY_DATABASE_URI = (
        os.getenv("DEV_DATABASE_URL") or f"sqlite:///{BASE_DIR / 'dev.db'}"
    ){% endif %}


class TestingEnvironment(Environment):
    TESTING = True
    {%- if cookiecutter.use_flask_sqlalchemy == 'y' %}
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL") or "sqlite://"{% endif %}


class ProductionEnvironment(Environment):
    {%- if cookiecutter.use_flask_sqlalchemy == 'y' %}
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL"){% endif %}


environments = {
    "development": DevelopmentEnvironment,
    "testing": TestingEnvironment,
    "production": ProductionEnvironment,
    "default": DevelopmentEnvironment,
}

