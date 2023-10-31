# Contains functions that the main program will call

import json
from tda.auth import easy_client, client_from_login_flow, client_from_token_file
from tda.client import Client
import os

# Access API Key Data
def get_keys(path):
    with open(path) as f: # f = file
        return json.load(f) # return file contents as a json

# Access API Data(redirect uri, token path, td account number, etc)
def get_headers(path):
    with open(path) as f:
        return json.load(f)
    
#TODO: Establish connection with the Client
def connect_to_api(chromedriver_path, chrome_path, api_key, redirect_uri, token_path):
    try:
        c = client_from_token_file(token_path, api_key)
    except FileNotFoundError:
        from selenium import webdriver
        with webdriver.Chrome() as driver:
            c = client_from_login_flow(driver, api_key, redirect_uri, token_path)
    print(c)
    pass



