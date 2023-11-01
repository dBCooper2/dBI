# Author: Trevor Rowland
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Imports:
import json
from tda import auth as a
from tda.client import Client
import os
from classes import Stock, Position

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Accessing Key Data to Connect to the API:

# Access API Key Data from files
def get_keys(path):
    with open(path) as f: # f = file
        return json.load(f) # return file contents as a json

# Access API Data(redirect uri, token path, td account number, etc)
def get_headers(path):
    with open(path) as f:
        return json.load(f)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Accessing the API and GET functions
def connect_to_api(api_key, redirect_uri, token_path):
    try:
        c = a.client_from_token_file(token_path, api_key)
    except FileNotFoundError:
        from selenium import webdriver
        with webdriver.Chrome() as driver:
            c = a.client_from_login_flow(driver, api_key, redirect_uri, token_path)
    return c

def get_portfolio(client, acct_num): # Returns positions and balances for a given account
    r = client.get_account(acct_num, fields=client.Account.Fields.POSITIONS)
    # helper functions to sort through and filter the data
    positions = filter_positions(r)
    balances = __get_balances(r)
    return [positions, balances]

def get_stock_hist_data(c: Client, symbol, periods): # returns historical data for a stock given a timeframe and # of periods(how many rows in the table)
    # possible params are every 1m, 5m, 10m, 15m, 30m, 1d, 1w
    if periods == '1m':
        data = c.get_price_history_every_minute(symbol)
    elif periods == '5m':
        data = c.get_price_history_every_five_minutes(symbol)
    elif periods == '10m':
        data = c.get_price_history_every_ten_minutes(symbol)
    elif periods == '15m':
        data = c.get_price_history_every_fifteen_minutes(symbol)
    elif periods == '30m':
        data = c.get_price_history_every_thirty_minutes(symbol)
    elif periods == '1d':
        data = c.get_price_history_every_day(symbol)
    elif periods == '1w':
        data = c.get_price_history_every_week(symbol)
    else:
         print("wrong period format!")
         return None
    return 

# Accesses API using a client, a symbol and a Projection Object(param that finds info on a stock or instrument data)
def get_instrument(c: Client, symbol, projection):
    if projection == 'symbol-search':
        proj = c.Instrument.Projection(projection)
        data = c.search_instruments(symbol, proj).json()
    elif projection == 'fundamental':
        proj = c.Instrument.Projection(projection)
        data = c.search_instruments(symbol, proj).json()
    else:
        data = None
        print("These endpoints have not been constructed yet!")
    return data

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Data Conversion: Converting JSONs into Analyzeable Formats

def convert_to_df(): # Convert Json to Dataframe
    pass

def convert_to_excel():
    pass

def convert_to_csv():
    pass


#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Helper Functions for API Calls

def filter_positions(data): # kept public
    return data['securitiesAccount']['positions']

def __get_balances(data): # returns all available cash for trading and balance data, privated to not show cash in CLI
    return data['securitiesAccount']['currentBalances']

def convert_positions_to_class(positions): #converts json data into a list of all position objects
	positions_to_sort = []
	
	for i in positions:
		if i['instrument']['symbol'] == 'MMDA1':
			continue
		else:
			# access values from dict, assign to vars
            # create stock obj
            # 
			temp_obj = Position(None, None, None, None, None, None, None)
			positions_to_sort.append(temp_obj)
			positions_to_return = sorted(positions_to_sort, key = lambda d: d.get_symbol())
	
	return positions_to_return

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Helper Functions for Data Analysis

# Find the % makeup of each stock in the portfolio
def calculate_percent_makeup_in_portfolio():
     pass



