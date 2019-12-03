import os
import re
import random
import string

import click
from flask_migrate import Migrate

from {{ cookiecutter.project_app_package }} import create_app, db
from config import BASE_DIR


app = create_app(os.getenv("FLASK_ENV") or "default")
migrate = Migrate(app, db)


BLUEPRINT_INIT_TEMPLATE = """
from flask import Blueprint

{name} = Blueprint("{name}", __name__)

from . import views, errors
"""

BLUEPRINT_VIEWS_TEMPLATE = """
from flask import render_template

from . import {name}


# @{name}.route("/", methods=["GET"])
# def index():
#    return render_template("{name}/index.html")
"""


@app.cli.command("start-blueprint")
@click.argument("name")
def start_blueprint(name):
    """Creates a new blueprint."""
    name = re.sub(r"-+|\s+|/+|\.+", "_", name.strip().lower())
    new_blueprint = BASE_DIR / "app" / name
    new_blueprint.mkdir()
    new_init = new_blueprint / "__init__.py"
    with new_init.open(mode="w") as f:
        f.write(BLUEPRINT_INIT_TEMPLATE.format(name=name))
    new_views = new_blueprint / "views.py"
    with new_views.open(mode="w") as f:
        f.write(BLUEPRINT_VIEWS_TEMPLATE.format(name=name))


@app.cli.command("gen-secret-key")
def gen_secret_key():
    """Generates a secret key."""
    secret = "".join(
        random.choices([*string.digits, *string.ascii_letters], k=64)
    )
    print(secret)

