from flask import Blueprint

blueprint = Blueprint('grandma', __name__)

from . import views, errors

