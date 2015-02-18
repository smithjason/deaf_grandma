from flask import Blueprint, request, render_template
from . import blueprint
from errors import bad_request

@blueprint.route("/", methods=["GET"])
def index():
  grandma = request.args.get('grandma')
  return render_template("grandma/index.tmpl", grandma=grandma)
