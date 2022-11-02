# standard libraries
import os
import sys

import numpy as np 
import pandas as pd 

from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

# import all the functions from helper.py
from helper import *

app = FastAPI()

# @app.post("/")


# user_input = input('Please enter your date of birth: ')

# if __name__ == '__main__':
#     # prompt user input
#     print(age(user_input))