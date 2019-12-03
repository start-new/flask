import os
import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent

INSTALLED_BLUEPRINTS = [
    {
        "module": "{{ cookiecutter.project_app_package }}.main.main",
        "prefix": "",
    }
]


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        os.getenv("DEV_DATABASE_URL") or f"sqlite:///{BASE_DIR / 'dev.db'}"
    )


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL") or "sqlite://"


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}

