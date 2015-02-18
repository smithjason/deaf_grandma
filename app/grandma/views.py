from flask import Blueprint, request, render_template, url_for, redirect
from flask.ext.bootstrap import Bootstrap

from . import blueprint
from .forms import GrandmaForm

from errors import bad_request

@blueprint.route("/", methods=["GET", "POST"])
def index():
    form = GrandmaForm()
    if form.validate_on_submit():
        user_input = request.args.get('user_input')
        if user_input == user_input.upper():
            response = "YOLO BRO!"
        else:
            response = "Speak up, kiddo!"
    else:
        response = request.args.get('grandma')
    return render_template("grandma/index.tmpl", grandma=response, form=form)

@blueprint.route("/grandma", methods=["POST"])
def grandma():

    if form.validate_on_submit():
        user_input = request.args.get('user_input')
        if user_input == user_input.upper():
            response = "YOLO BRO!"
        else:
            response = "Speak up, kiddo!"
    return redirect(url_for("grandma.index", grandma=response))
