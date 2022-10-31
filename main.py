# standard libraries
import os
import sys

import numpy as np 
import pandas as pd 

# import all the functions from helper.py
from helper import *

user_input = input('Please enter your date of birth: ')

if __name__ == '__main__':
    # prompt user input
    print(age(user_input))
