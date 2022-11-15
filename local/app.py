# import libraries
from flask import Flask, request, jsonify

# import functions from helper.py
# from helper import *

# initialise flask app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle_request():

    # API endpoint /?input=
    text = str(request.args.get('input'))

    # perform method imported from helper.py
    output = text.upper()

    # make sure the output is JSON and cross-origin is enabled; necessary for Glide fetch column function
    response = jsonify(key=text, value=output)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
