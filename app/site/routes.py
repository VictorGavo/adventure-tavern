import os
import pathlib
import sys
from logging import FileHandler, WARNING
import json
import requests
from flask import Blueprint, render_template, session, abort, redirect, request
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests

from app.encounters import encounter
from app.dalle import image_url


site = Blueprint('site', __name__, template_folder='site_templates')
site.secret_key = os.environ.get('client_secret')

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

print(os.listdir())

# f = open('./secrets.json')
# auth = json.load(f)
# print(auth)
# f.close()
GOOGLE_CLIENT_ID = os.environ.get("client_id")
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://localhost:5000/callback"
)

def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401) #Authorization required
        else:
            return function()
    return wrapper

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/login')
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)

@site.route('/callback')
def callback():
    try:
        flow.fetch_token(authorization_response=request.url)

        if session.get("state")!= request.args.get("state"):
            raise Exception("State mismatch")
            
    # if not session["state"] == request.args["state"]:
    #     abort(500) # State does not match!

        credentials = flow.credentials
        request_session = requests.session()
        cached_session = cachecontrol.CacheControl(request_session)
        token_request = google.auth.transport.requests.Request(session=cached_session)

        id_info = id_token.verify_oauth2_token(
            id_token=credentials.id_token,
            request=token_request,
            audience=GOOGLE_CLIENT_ID
        )

        session["google_id"] = id_info.get("sub")
        session["name"] = id_info.get("name")
    except Exception as e:
        return f"Error: {e}", 500
    
    return redirect("/tavern")
    
@site.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@site.route('/tavern')
@login_is_required
def tavern():
    return render_template('tavern.html')

@site.route('/adventure')
def adventure():
    return render_template('adventure.html', image_url=image_url, encounter=encounter)

@site.route('/contact')
def contact():
    return render_template('contact.html')

@site.route('/about')
def about():
    return render_template('about.html')

