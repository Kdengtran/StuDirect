import os
import requests as rq

import flask
import json

base_url = 'https://rijstkoker.pythonanywhere.com'

def run_something(data_from_glide):

    # the variables used for the recommender system
    payload = {'input': data_from_glide}

    response = rq.get(base_url, params=payload).json()

    return response['input']

