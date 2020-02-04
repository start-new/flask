"""Main module of the application."""

import os

from . import create_app, db
from flask_migrate import Migrate

if __name__ == "__main__":
  app = create_app(os.getenv('FLASK_CONFIG') or 'default')
  migrate = Migrate(app, db)
