# import libraries
from flask import Flask, request, jsonify

# import functions from helper.py
from helper import *

# initialise flask app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle_request():
    """This function obtains the user profile from Glide, runs the RecSys script, and returns the top n matches. 

       If the pythonanywhere_call_api functions works properly, push this to Pythonanywhere!

    Returns:
        JSON: Returns the unique Row IDs of the job profiles
    """

    # API endpoint /?input=
    user_profile = str(request.args.get('input'))

    # TODO
    # create DataFrame from user_profile

    # TODO 
    # obtain all the job profiles using the google_api_call function

    # TODO 
    # match and rank
    output = upper(user_profile) # REPLACE THIS WITH THE MATCH AND RANK FUNCTION

    # make sure the output is JSON and cross-origin is enabled; necessary for Glide fetch column function
    response = jsonify(key=text, value=output)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == '__main__':
    ...
