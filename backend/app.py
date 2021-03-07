import json

from flask import Flask, request, session
from flask_cors import CORS, cross_origin

from google.oauth2 import id_token
from google.auth.transport import requests

import string
import random

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# TODO: Replace secret key in an actual prod environment (See this article)
# https://blog.paradoxis.nl/defeating-flasks-session-management-65706ba9d3ce
# In a nutshell, hackers can use a rainbow table against your session to find out the secret key and parrot your app.
app.secret_key = f'INSECURE_DEV_SECRET_KEY_REPLACE_STATICALLY_IN_PROD_'.join(random.choices(string.ascii_uppercase +
                                                                                            string.digits, k=10))

# Replace with your client ID later.
CLIENT_ID = '838132247517-n9cve8sucts7h0cp93bhjifogr3i4k88.apps.googleusercontent.com'


@app.route('/authenticated_endpoint')
def authenticated_endpoint():
    if "user" in session:
        user = session['user']
        print(user)
        return user
    return "Not found!"


# Enable CORS so frontend (localhost:3000) can communicate with backend (localhost:5000)
@app.route('/api/auth/google', methods=['POST'])
@cross_origin()
def google_sign_in():
    request_data = request.get_json()
    token = request_data['token']
    print(token)
    try:
        # Specify the CLIENT_ID of the app that accesses the backend:
        id_info = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)

        # ID token is valid. Get the user's Google Account ID from the decoded token.
        userid = id_info['sub']
        print(userid)
        print(id_info['email'])

        # Create the session
        session["user"] = id_info['email']
    except ValueError:
        # Invalid token
        pass
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }

    # convert into JSON:
    y = json.dumps(x)
    return y


if __name__ == '__main__':
    app.run()
