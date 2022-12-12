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

    # print(response)

    return response['key']

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

def clean(df):
    
    # make sure we don't fuck up anything
    profile = df.copy()
    
    try:
    
        # add spaces after the comma; only necessary for user profiles
        extra_whitespace = ['Core Values', 'Industry Interest', 'Technical Skills', 'Social Skills', 'Desired Skills']
        profile[extra_whitespace] = profile[extra_whitespace].str.replace(',', ', ')

    except:
        
        pass
    
    # remove English stopwords and lowercase all tokens
    english_stopwords = stopwords.words('english')
    cleaned = [str(word).lower() for word in profile if word not in english_stopwords]
    
    # transform into string 
    output = " ".join(token for token in cleaned)
    
    # remove punctuation, unnecesarry whitespaces and new lines
    output = output.translate(str.maketrans('', '', string.punctuation)).replace('\n', ' ').replace('  ', ' ')
    
    return output

def match(user, job):
    
    bow_model = TfidfVectorizer()
    tf_idf = bow_model.fit_transform([clean(user), clean(job)])
    
    return (user.name, job.name, cosine_similarity(tf_idf)[0][1].round(2))

if __name__ == '__main__':
    pass