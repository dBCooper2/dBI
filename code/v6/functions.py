from tda.client import Client
from tda import auth as a
import pandas as pd
import json
import os

from classes.portfolio import Portfolio


# Accessing API:
def get_account_data(path: str)->dict: # Gets api key, account_number, redirect_uri, and token path and returns them as a dict from a specified filename and path
    with open(path) as f: # f = file
        return json.load(f) # return file contents as a json

def get_output_path(path: str)->dict: # Gets a directory path to output all data to
    return

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


# Output to Files
def to_csv(output_path: str, filename: str, df: pd.DataFrame)->int: # Outputs Data and Analysis as CSV files, return an exit code to make sure the data exported properly
    try:
        os.makedirs(output_path, exist_ok=True)
        df.to_csv(os.path.join(output_path, filename))
        return 1
    except:
        return -1

def to_pickle(output_path: str, df: pd.DataFrame)->int: #Outputs a Pickle of the data, only use within your python code!
    return -1

def output_to_excel(output_path: str, df: pd.DataFrame)->int: # Outputs Data and Analysis as an Excel Workbook, return an exit code
    return -1

def weighted_avg(rb: list, ns: list)->float: # rb = return or betas list, ns = list of number of shares per position
    if len(rb) == len(ns):
        return 1
    return -1


# CAPM-Specific Functions
def filter_positions_for_capm(p_df: pd.DataFrame)->pd.DataFrame:
    p_df = p_df[['symbol', 'cusip', 'assetType', 'longQuantity', 'marketValue', 'averagePrice', 'currentDayProfitLoss', 'currentDayProfitLossPercentage']]
    return p_df

def filter_instruments_for_capm(i_df: pd.DataFrame)->pd.DataFrame:
    i_df = i_df[['symbol', 'cusip', 'beta']] # Add to this if needed
    return i_df

def capm(c: Client, an: str)->int: # Perform capm on a Portfolio of stocks, output the results to csv/excel, return with exit code
    return -1