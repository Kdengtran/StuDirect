import requests as rq
import pandas as pd 

# test if the API works
def api_call(data_from_glide):

    base_url = 'http://127.0.0.1:5000'

    # the variables used for the recommender system
    payload = {'input': data_from_glide}

    # JSON response. For the url, change .json() to .url
    response = rq.get(base_url, params=payload).json()

    print(response)

    return print(response['value'])

def recommendation(words):
    
    df = pd.DataFrame([words.split(';')], columns=['input1', 'input2', 'input3', 'input4'])
    
    return print(df)

if __name__ == '__main__':
    recommendation('kaas; pizza; ham, kaas; tonijn')