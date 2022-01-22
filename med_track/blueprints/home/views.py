import imp
from flask import render_template
from . import bp

import requests


@bp.route("/")
def index():
    req = requests.get(
        "https://api.netpie.io/v2/device/shadow/data",
        auth=(
            "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm",
        ),
    )
    req = req.json()
    left_medicine = req["data"]["left"]
    right_medicine = req["data"]["right"]
    return render_template(
        "home/index.html",
        left_medicine=left_medicine,
        right_medicine=right_medicine,
    )
