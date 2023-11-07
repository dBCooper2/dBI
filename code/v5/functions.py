# Imports:
import json
from tda import auth as a
from tda.client import Client
import os

# Accessing Key Data to Connect to the API:

# Access API Key Data from files
def get_keys(path):
    with open(path) as f: # f = file
        return json.load(f) # return file contents as a json

# Access API Data(redirect uri, token path, td account number, etc)
def get_headers(path):
    with open(path) as f:
        return json.load(f)
    
# Accessing the API
def connect_to_api(api_key, redirect_uri, token_path):
    try:
        c = a.client_from_token_file(token_path, api_key)
    except FileNotFoundError:
        from selenium import webdriver
        with webdriver.Chrome() as driver:
            c = a.client_from_login_flow(driver, api_key, redirect_uri, token_path)
    return c

# Access Account JSON: KEEP RAW!!!
def get_acct(c: Client, acct_num, is_balances: bool): # Returns positions and balances for a given account
    return c.get_account(acct_num, fields=c.Account.Fields.POSITIONS).json()