from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("dashboard/home.html", left_medicine=0, right_medicine=0)


if __name__ == "__main__":
    app.run(debug=True)
