# Imports:
import json
from tda import auth as a
from tda.client import Client
import pandas as pd
import os

from classes.portfolio import Portfolio

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


# Data Processing: Outputting the Data as a CSV or Excel File
def to_csv(data: pd.DataFrame):
    data.to_csv()

def to_excel(p: Portfolio):
    # This assumes the Position and Instruments are Merged
    # Add Price Histories as separate sheets
    excel_file_path = 'output.xlsx'

    with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:

        # Write the main DataFrame to the first worksheet
        p.positions_df.to_excel(writer, sheet_name='Positions', index=False)
        p.instruments_df.to_excel(writer, sheet_name='Instruments', index=False)

        # Write each DataFrame in the list to a separate worksheet
        for key in p.get_all_price_history().keys():
            p.get_one_price_history(key).to_excel(writer, sheet_name=f'Sheet{key}', index=False)
    pass