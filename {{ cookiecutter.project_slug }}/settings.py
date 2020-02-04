import os
import pathlib


BASE_DIR = pathlib.Path(__file__).resolve().parent


INSTALLED_BLUEPRINTS = [
    {
        "module": "{{ cookiecutter.project_app_package }}.main.main",
        "prefix": "",
    }
]


class Environment:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentEnvironment(Environment):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        os.getenv("DEV_DATABASE_URL") or f"sqlite:///{BASE_DIR / 'dev.db'}"
    )


class TestingEnvironment(Environment):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL") or "sqlite://"


class ProductionEnvironment(Environment):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


config = {
    "development": DevelopmentEnvironment,
    "testing": TestingEnvironment,
    "production": ProductionEnvironment,
    "default": DevelopmentEnvironment,
}

