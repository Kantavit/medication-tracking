import profile
from flask import Flask, redirect, url_for, render_template, session
from authlib.integrations.flask_client import OAuth
from med_track import  oauth
from datetime import timedelta
from . import bp

import requests


@bp.route('/')
def home():
    if(session):
        return redirect('/home')
    return render_template("account/index.html")


@bp.route('/login/')
def login():
    # google = oauth.create_client('google')  # create the google oauth client
    redirect_uri = url_for('account.authorize', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

    
@bp.route('/authorize')
def authorize():
    token = oauth.google.authorize_access_token()
    resp = oauth.google.get('userinfo')  # userinfo contains stuff u specificed in the scrope
    user_info = resp.json()
    user = oauth.google.userinfo()  # uses openid endpoint to fetch user info
    # Here you use the profile/user data that you got and query your database find/register the user
    # and set ur own data in the session not the profile from google
    session['profile'] = user_info
    session.permanent = True  # make the session permanant so it keeps existing after broweser gets closed
    print(session, user_info, user)

    # name = dict(session)['profile']['name']
    # return redirect(url_for('home.index', email=email))
    # return render_template("home/index.html",name=name)
    return redirect('/home')


@bp.route('/logout')
def logout():
    print(session)
    for key in list(session.keys()):
        session.pop(key)
    print(session)
    return redirect('/')