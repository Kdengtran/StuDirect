# standard modules
import numpy as np 
import pandas as pd 
import sklearn

# connect
import requests as rq
import gspread

# clean 
import re
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import string

# match
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def pythonanywhere_api_call(data_from_glide):
    """This function tests whether the API on Pythonanywhere works.

       If all works well, push the flask_app.py to Pythonanywhere!

    Args:
        data_from_glide (JSON): Data seperated by ;

    Returns:
        JSON: The output after running the script on Pythonanywhere.
    """

    base_url = 'http://rijstkoker.pythonanywhere.com/' # REPLACE THIS WITH THE STUDIRECT APP

    # the variables used for the recommender system
    payload = {'input': data_from_glide}

    # JSON response. For the url, change .json() to .url
    response = rq.get(base_url, params=payload).json()

    return print(response['value'])

def google_api_call():
    """This function obtains all the Job profiles from StuDirect.

    Returns:
        DataFrame: This DataFrame will be used to match and rank. 
    """

    # connect to spreadsheets using json credentials
    gc = gspread.service_account(filename='Credentials.json') # REPLACE THIS WITH THE STUDIRECT CREDENTIALS

    # open the worksheets and select the first; we don't have other worksheets
    sh = gc.open_by_key('1ajtIu6OrbVMTL_RG5wTLvHaD6-D5c8AtykoPKDKQ_-w') # REPLACE THIS WITH THE STUDIRECT CREDENTIALS
    worksheet = sh.sheet1

    # fetch data and return a Pandas DataFrame
    results = worksheet.get_all_records()

    df = pd.DataFrame(results)

    return df

def clean(df):
    """This function cleans a row from a users/jobs dataframe.

    Returns:
        str: A cleaned string ready for matching.
    """
    
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

    # stem words of the cleaned list
    stemmer = SnowballStemmer(language='english')
    stemmed_words = [stemmer.stem(word) for word in cleaned]
    
    # transform into string 
    output = " ".join(token for token in stemmed_words)
    
    # remove punctuation, unnecesarry whitespaces and new lines
    output = output.translate(str.maketrans('', '', string.punctuation)).replace('\n', ' ').replace('  ', ' ')
    
    return output

def match_and_rank(user, jobs, top_n):
    """This functions calls the clean function and matches a user with the job profiles. Thereafter, this function ranks the top n results.

    Args:
        user (Series): The user.
        jobs (Series): The jobs.
        top_n (int): Indicate how many results you want returned.

    Returns:
        List: Tuples with the Row ID, Job Title, and Cosine Similarity Score.
    """

    # create local student variable
    student = user

    # student ID, job ID, and the cosine similarity score
    rank_list = []
    
    bow_model = TfidfVectorizer()

    # iterate over all the jobs and match with the local student variable
    for index, job in jobs.iterrows():
        tf_idf = bow_model.fit_transform([student, clean(job)])
        rank_list.append((job.name, jobs.loc[job.name]['Job Title'], cosine_similarity(tf_idf)[0][1].round(2)))

    # return the top n results --> Job title: Similarity score
    sorted_list = sorted(rank_list, key=lambda s: s[2], reverse=True)
    
    return sorted_list[:top_n]