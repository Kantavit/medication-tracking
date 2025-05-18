from flask import Blueprint

bp = Blueprint("account", __name__, url_prefix="/", template_folder="templates")

from . import views
