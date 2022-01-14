from flask import Flask, render_template

import requests

app = Flask(__name__)


@app.route("/")
def home():
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
        "dashboard/home.html",
        left_medicine=left_medicine,
        right_medicine=right_medicine,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
