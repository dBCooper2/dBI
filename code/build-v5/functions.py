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
# CSVs CANNOT HAVE SHEETS, ONLY ONE TABLE PER FILE
def to_csv(data: pd.DataFrame):
    data.to_csv()

def portfolio_to_csv(p: Portfolio, output_folder: str):
    # Output multiple CSV Files
    # 1 for the Positions/Instruments Combined DF
    # 1 for each Price History Object in the list
    os.makedirs(output_folder, exist_ok=True)

    p.get_positions_df().to_csv(os.path.join(output_folder, 'Positions.csv'))
    p.get_instruments_df().to_csv(os.path.join(output_folder, 'Instruments.csv'))
    
    for key in p.get_all_price_history():
        p.get_one_price_history(key).to_csv(os.path.join(output_folder, f'{key}.csv'), index=False)
    pass

def portfolio_to_excel(p: Portfolio, output_folder):
    # This assumes the Position and Instruments are Merged
    # Add Price Histories as separate sheets
    os.makedirs(output_folder, exist_ok=True)

    excel_filename = 'portfolio'
    fn = get_unique_filename(excel_filename)

    excel_path = os.path.join(output_folder, fn)

    with pd.ExcelWriter(excel_path, engine='xlsxwriter') as writer:

        # Write the main DataFrame to the first worksheet
        p.get_positions_df().to_excel(writer, sheet_name='Positions', index=False)
        p.get_instruments_df().to_excel(writer, sheet_name='Instruments', index=False)

        # Write each DataFrame in the list to a separate worksheet
        for key in p.get_all_price_history().keys():
            p.get_one_price_history(key).to_excel(writer, sheet_name=f'Sheet{key}', index=False)
    pass

def get_unique_filename(base_filename: str):
    count = 1
    while True:
        new_filename = f"{base_filename}-{count}.xlsx"
        if not os.path.exists(new_filename):
            return new_filename
        count += 1
