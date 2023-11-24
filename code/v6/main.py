# Gets API data and performs analysis on them

# Imports
from tda.client import Client
import pandas as pd
import datetime as d

import functions as f
import analysis as a
from classes.portfolio import Portfolio

# Configs
tda_api_configs = f.get_account_data('/Users/trowland/.secret/tda-api-v6.json') # Add /Users/username/.secret/path/to/api_key/file
output_path = 'output/CSVs' # Add /Users/username/Documents/output/repo

api_key = tda_api_configs['api_key']
account_number = tda_api_configs['account_number']
redirect_uri = tda_api_configs['redirect_uri']
token_path = tda_api_configs['token_path']

end_dt = d.datetime.now() # Use as End in Portfolio params
start_dt = end_dt - d.timedelta(days = 12) # Use as start in Portfolio params

example_acct_dict = {
    'securitiesAccount':{
        'positions':[
            { 'instrument':{'symbol':'TM','assetType':'EQUITY'},
              'averagePrice':117.94,
              'quantity':5.0},
            { 'instrument':{'symbol':'UPS','assetType':'EQUITY'},
              'averagePrice': 101.49,
              'quantity': 5.0},
            { 'instrument':{'symbol':'FDX','assetType':'EQUITY'},
              'averagePrice':188.77,
              'quantity':5.0},
        ]
    }
}

# Checkpoint 2: Connect to API
print('Checkpoint 1: Connect to the API and Create Client\n')
client = f.connect_to_api(api_key, redirect_uri, token_path)
print('Checkpoint 1 Passed.\n')

# Checkpoint 3: Create Portfolio Object

print('Checkpoint 2: Create the Portfolio...\n')
p1 = Portfolio(client, account_number, '1d', start_dt, end_dt, output_path)
print('Checkpoint 2 Passed.\n')

# Risk-Free Rate: BIV - Tracks Intermediate-Term Bonds(5-10Yrs), I can't access bonds rn so this will have to do
# Market Rate: SPY - Tracks S&P 500 Index
print('Checkpoint 3: Attempting to Pull CAPM Data and Process it...\n')
p1.capm('BIV', 'SPY', 'close') # USE YAHOO FOR BONDS LATER, CHECK TDA-API DISCORD FOR MORE INFO
print('Checkpoint 3 Passed.\n')


#p1.all_to_csv()
#p1.all_to_pickle()

# Checkpoint 4: CAPM Test
print()



