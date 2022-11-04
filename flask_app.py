# import libraries
from flask import Flask, request, jsonify

# import functions from helper.py
from helper import *

# initialise flask app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle_request():

    # API endpoint /?input=
    text = str(request.args.get('input'))

    # perform method
    text_upper = upper(text)

    # make sure the output is JSON and cross-origin is enabled; necessary for Glide fetch column function
    response = jsonify(key=text, value=text_upper)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

# check whether the API returns a string
if __name__ == '__main__':
    api_call('pizza')