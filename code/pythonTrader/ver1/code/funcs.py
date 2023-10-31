# This contains the Main Functions for the Program to keep the Build.py file clean
import config as cf
import stock as s
from tda import auth, client
import json

# Function to Login through Firefox with the TDAmeritrade API and generate an OAuth Token
def ff_login():
	try:
		c = auth.client_from_token_file(cf.token_path, cf.api_key)
	except FileNotFoundError:
		from selenium import webdriver
		with webdriver.Firefox(executable_path = r'/opt/homebrew/bin/geckodriver') as driver:
			c = auth.client_from_login_flow(driver, cf.api_key, cf.redirect_uri, cf.token_path)
			
	return c

# Function to call the tda_api's get_account() function
#	Figure out an elegant way to pass the files into the stock.py file!!!
def get_account_positions(c):
	r = c.get_account(cf.td_acct_num, fields=c.Account.Fields.POSITIONS)
	data = r.json() # This is the raw json, the whole shebang
	
	positions = filter_positions(data)
	stock_list = convert_positions_to_class(positions)
	for i in stock_list:
		print(i.to_string())
	
	# Add another method to get just the dict of the current balances
	balances = filter_balances(data)
	balance_str = ''
	balance_str += '\x1b[3;37m\nTotal Market Value:\t' + str(balances['longMarketValue'])
	balance_str += '\nAvailable Cash:\t\t' + str(balances['cashAvailableForTrading'])
	balance_str += '\x1b[0;37m'
	print(balance_str)
	
	return
	
	
# Helper Method to take the big raw json and spit out just the positions
def filter_positions(data):
	# Access the data['securities'] layer
		# Access the data['positions'] layer and spit it out
	return data['securitiesAccount']['positions'] # Does this work?

# Helper Method to take the big raw json and spit out just the current balances
def filter_balances(data):
	return data['securitiesAccount']['currentBalances']

# Helper Method to Pass in Position jsons to the __init__() function of stock.py
def convert_positions_to_class(positions):
	positions_to_sort = []
	
	for i in positions:
		if i['instrument']['symbol'] == 'MMDA1':
			continue
		else:
			symbol = i['instrument']['symbol']
			ns = i['longQuantity']
			tv = i['marketValue']
			pp = i['averagePrice']
			pla = i['currentDayProfitLoss']
			plp = i['currentDayProfitLossPercentage']
			pps = str(float(tv)/float(ns))
		
			temp_obj = s.Stock(symbol, pps, ns, tv, pp, pla, plp)
			positions_to_sort.append(temp_obj)
			positions_to_return = sorted(positions_to_sort, key = lambda d: d.get_symbol())
	
	return positions_to_return
