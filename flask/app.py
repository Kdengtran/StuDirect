import os
import requests as rq

import flask
import json

def run_something(data_from_glide):

    base_url = 'https://rijstkoker.pythonanywhere.com'

    # the variables used for the recommender system
    payload = {'input': data_from_glide}

    response = rq.get(base_url, params=payload).json()

    print(rq.get(base_url, params=payload).url)

    return print(response['input'])

if __name__ == '__main__':
    run_something('De server zou dit moeten returnen!')