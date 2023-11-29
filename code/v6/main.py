# Gets API data and performs analysis on them

# Imports
from tda.client import Client
import pandas as pd
import datetime as d

import functions as f
from classes.td_portfolio import TD_Portfolio
from classes.test_portfolio import TestPortfolio

from classes.visualization import PieChart
from classes.visualization import LineGraph
from classes.visualization import ScatterPlot
from classes.visualization import Histogram


# Configs
tda_api_configs = f.get_account_data('/Users/trowland/.secret/tda-api-v6.json') # Add /Users/username/.secret/path/to/api_key/file
output_path = '/Users/trowland/Documents/pythonTrader_Data/output/CSVs' # Add /Users/username/Documents/output/repo
output_path_test = '/Users/trowland/Documents/pythonTrader_Data/test_data__output/CSVs'

api_key = tda_api_configs['api_key']
account_number = tda_api_configs['account_number']
redirect_uri = tda_api_configs['redirect_uri']
token_path = tda_api_configs['token_path']

end_dt = d.datetime.now() # Use as End in Portfolio params
start_dt = end_dt - d.timedelta(days = 64) # Use as start in Portfolio params

example_acct_dict = {
    'data':
    [
        {'symbol':'TM', 'assetType':'EQUITY', 'averagePrice':117.94, 'longQuantity':5.0},
        {'symbol':'UPS', 'assetType':'EQUITY', 'averagePrice': 101.49,'longQuantity': 5.0},
        {'symbol':'FDX', 'assetType':'EQUITY', 'averagePrice':188.77, 'longQuantity':5.0},
    ]}

# Checkpoint 2: Connect to API
print('Checkpoint 1: Connect to the API and Create Client\n')
client = f.connect_to_api(api_key, redirect_uri, token_path)
print('Checkpoint 1 Passed.\n')

# Checkpoint 3: Create Portfolio Object

print('Checkpoint 2: Create the Portfolios...\n')
p1 = TD_Portfolio(client, account_number, '1d', start_dt, end_dt, output_path, 'BIV', 'SPY', 'close')
print('TD_Portfolio created...')
p2 = TestPortfolio(client, example_acct_dict, '1d', start_dt, end_dt, output_path_test, 'BIV', 'SPY', 'close')
print('Checkpoint 2 Passed.\n')

# Checkpoinrt 4: CAPM Test

# Risk-Free Rate: BIV - Tracks Intermediate-Term Bonds(5-10Yrs), I can't access bonds rn so this will have to do
# Market Rate: SPY - Tracks S&P 500 Index
print('Checkpoint 4: Attempting to Pull CAPM Data and Process it...\n')
td_capm_df = p1.capm() # USE YAHOO FOR BONDS LATER, CHECK TDA-API DISCORD FOR MORE INFO
print('TD CAPM DF Created')
print(td_capm_df)

test_capm_df = p2.capm()
print('Test CAPM DF Created')
print(test_capm_df)
print()
print('Checkpoint 4 Passed.\n')

p1.all_to_csv()
p2.all_to_csv()
#p1.all_to_pickle()
#p2.all_to_pickle()

# Checkpoint 5: Create Graphs
qty = p1._positions_df['longQuantity'].to_list()
names = p1._positions_df.index.to_list()

pc = PieChart(qty, names)
pc.output_plot()