# import libraries
from flask import Flask, request, jsonify

import pandas as pd

from helper import google_api_call, clean, match_and_rank

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

    # create DataFrame from user_profile
    split = user_profile.split(";")
    df = pd.DataFrame(split)

    for index, row in df.iterrows():
        if index > 5:
            df.iloc[index] = df.iloc[index].str.replace(',',', ')

    student = clean(df.iloc[:,0])

    # obtain all the job profiles using the google_api_call function
    vacancies = google_api_call().set_index('🔒 Row ID')

    # match and rank
    output = ", ".join(x[0] for x in match_and_rank(student, vacancies, 5)) # REPLACE THIS WITH THE MATCH AND RANK FUNCTION
    
    # make sure the output is JSON and cross-origin is enabled; necessary for Glide fetch column function
    response = jsonify(key=user_profile, value=output)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
