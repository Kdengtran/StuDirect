import requests as rq
import pandas as pd 
import gspread

# test if the API works locally
def pythonanywhere_api_call(data_from_glide):

    # setup local server
    base_url = 'http://127.0.0.1:5000'

    # the variables used for the recommender system
    payload = {'input': data_from_glide}

    # JSON response. For the url, change .json() to .url
    response = rq.get(base_url, params=payload).json()

    print(response)

    return print(response['value'])

def google_api_call():

    # connect to spreadsheets using json credentials
    gc = gspread.service_account(filename='google_kevin.json')

    # open the worksheets and select the first; we don't have other worksheets
    sh = gc.open_by_key('1T2If_xR-fhQw6hFejDxdPLLnz1J0lDstTKZ1FJVNwQI')
    worksheet = sh.sheet1

    # fetch data and return a Pandas DataFrame
    results = worksheet.get_all_records()

    df = pd.DataFrame(results)

    return print(df)

if __name__ == '__main__':
    recommendation()