import requests as rq
from datetime import date, datetime

# test if the API works
def api_call(data_from_glide):

    base_url = 'https://rijstkoker.pythonanywhere.com'

    # the variables used for the recommender system
    payload = {'input': data_from_glide}

    # JSON response. For the url, change .json() to .url
    response = rq.get(base_url, params=payload).json()

    return print(response['key'])

# geboortedatum omrekenen naar leeftijd
def age(datum):

    born = datetime.strptime(datum, "%d/%m/%Y").date()
    today = date.today()

    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    return '\nYou\'re {} years old!'.format(age)

# capitalise input
def upper(text):

    return text.upper()

