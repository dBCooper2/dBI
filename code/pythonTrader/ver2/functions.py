# Contains functions that the main program will call

import json
from tda import auth as a
from tda.client import Client
import os
from classes import Stock, Position

# Access API Key Data
def get_keys(path):
    with open(path) as f: # f = file
        return json.load(f) # return file contents as a json

# Access API Data(redirect uri, token path, td account number, etc)
def get_headers(path):
    with open(path) as f:
        return json.load(f)
    
#TODO: Establish connection with the Client
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

def get_stock_hist_data(c: Client, symbol, start_datetime,end_datetime, need_extended_hours_data, periods): # returns historical data for a stock given a timeframe and # of periods(how many rows in the table)
    # possible params are every 1m, 5m, 10m, 15m, 30m, 1d, 1w
    if periods.equals('1m'):
        data = c.get_price_history_every_minute(symbol, start_datetime, end_datetime, need_extended_hours_data)
    elif periods.equals('5m'):
        data = c.get_price_history_every_five_minutes(symbol, start_datetime, end_datetime, need_extended_hours_data)
    elif periods.equals('10m'):
        data = c.get_price_history_every_ten_minutes(symbol, start_datetime, end_datetime, need_extended_hours_data)
    elif periods.equals('15m'):
        data = c.get_price_history_every_fifteen_minutes(symbol, start_datetime, end_datetime, need_extended_hours_data)
    elif periods.equals('30m'):
        data = c.get_price_history_every_thirty_minutes(symbol, start_datetime, end_datetime, need_extended_hours_data)
    elif periods.equals('1d'):
        data = c.get_price_history_every_day(symbol, start_datetime, end_datetime, need_extended_hours_data)
    elif periods.equals('1w'):
        data = c.get_price_history_every_week(symbol, start_datetime, end_datetime, need_extended_hours_data)
    else:
         print("wrong period format!")
         return None
    return data

def get_sector_hist_data(sector, timeframe, periods): # access the top X companies in a sector over a given timeframe and # of periods
    pass

def convert_to_df(): # Convert Json to Dataframe
    pass

def convert_to_excel():
    pass

def convert_to_csv():
    pass

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



