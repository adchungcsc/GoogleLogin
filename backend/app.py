import json

from flask import Flask, request
from flask_cors import CORS, cross_origin

from google.oauth2 import id_token
from google.auth.transport import requests

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
CLIENT_ID = '838132247517-n9cve8sucts7h0cp93bhjifogr3i4k88.apps.googleusercontent.com'

@app.route('/authenticated_endpoint')
def authenticated_endpoint():
    return "Hello World!"


# Enable CORS so frontend (localhost:3000) can communicate with backend (localhost:5000)
@app.route('/api/auth/google', methods=['POST'])
@cross_origin()
def token_sign_in():
    request_data = request.get_json()
    token = request_data['token']
    print(token)
    try:
        # Specify the CLIENT_ID of the app that accesses the backend:
        id_info = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)

        # ID token is valid. Get the user's Google Account ID from the decoded token.
        userid = id_info['sub']
        print(id_info)
        print(userid)
    except ValueError:
        # Invalid token
        pass

    return 'hello world'


if __name__ == '__main__':
    app.run()
