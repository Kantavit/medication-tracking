from flask import Blueprint

bp = Blueprint("home", __name__, url_prefix="/", template_folder="templates")

from . import views
