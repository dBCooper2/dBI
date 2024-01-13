from tda.client import Client
from tda import auth as a
import pandas as pd
import json
import os


# Accessing API:
def get_account_data(path: str)->dict: # Gets api key, account_number, redirect_uri, and token path and returns them as a dict from a specified filename and path
    with open(path) as f: # f = file
        return json.load(f) # return file contents as a json

def get_output_path(path: str)->dict: # Gets a directory path to output all data to
    with open(path) as f: # f = /path/to/folder
        return json.load(f)

# Connects to api and returns the Client object for API calls
# ak: str = API Key
# ru: str = Redirect URI
# tp: str = Token Path(path/to/token.json)
def connect_to_api(ak: str, ru: str, tp: str)->Client: 
    try:
        c = a.client_from_token_file(tp, ak)
    except FileNotFoundError:
        from selenium import webdriver
        with webdriver.Chrome() as driver:
            c = a.client_from_login_flow(driver, ak, ru, tp)
    return c