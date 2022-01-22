from flask import Flask

from med_track import blueprints  # project package

import os


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)  # use instance folder
    # for developing
    app.config.from_mapping(SECRET_KEY="dev")

    if test_config is None:
        # update on production
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Blueprints
    blueprints.register_blueprints(app)

    return app
