from flask import Flask
from med_track import blueprints  # project package
from authlib.integrations.flask_client import OAuth # OAuth
from datetime import timedelta
import os

oauth = OAuth()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)  # use instance folder
    # for developing
    app.config.from_mapping(SECRET_KEY="dev")

    if test_config is None:
        # update on production
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    app.secret_key = 'randomsecretidkite'
    app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)  
    oauth.init_app(app)
    oauth.register(
        name='google',
        client_id='122229999743-tcsb5q1ipt557mo60s1jdq0k081ho8rl.apps.googleusercontent.com',
        client_secret='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',
        access_token_url='https://accounts.google.com/o/oauth2/token',
        access_token_params=None,
        authorize_url='https://accounts.google.com/o/oauth2/auth',
        authorize_params=None,
        api_base_url='https://www.googleapis.com/oauth2/v1/',
        userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',  # This is only needed if using openId to fetch user info
        client_kwargs={'scope': 'openid email profile'},
    )


    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Blueprints
    blueprints.register_blueprints(app)

    return app
