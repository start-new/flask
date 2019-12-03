from flask import render_template

from . import main


@main.route("/", methods=["GET"])
def index():
    return render_template(
        "main/index.html", page_title="{{ cookiecutter.project_name }}"
    )

