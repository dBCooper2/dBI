# Gets API data and performs analysis on them

# Imports
from tda.client import Client
import pandas as pd
import datetime as d
import matplotlib.pyplot as plt
import mplfinance as mpf

import functions as f
from classes.td_portfolio import TD_Portfolio
from classes.test_portfolio import TestPortfolio
from classes.price_history import PriceHistory

from classes.visualization import PieChart


# Configs
tda_api_configs = f.get_account_data('/Users/trowland/.secret/tda-api-v6.json') # Add /Users/username/.secret/path/to/api_key/file
output_path = '/Users/trowland/Documents/pythonTrader_Data/output/CSVs' # Add /Users/username/Documents/output/repo
output_path_test = '/Users/trowland/Documents/pythonTrader_Data/test_data__output/CSVs'

api_key = tda_api_configs['api_key']
account_number = tda_api_configs['account_number']
redirect_uri = tda_api_configs['redirect_uri']
token_path = tda_api_configs['token_path']

end_dt = d.datetime.now() # Use as End in Portfolio params
start_dt = end_dt - d.timedelta(days = 365) # Use as start in Portfolio params

example_acct_dict = {
    'data':
    [
        {'symbol':'TM', 'assetType':'EQUITY', 'averagePrice':117.94, 'longQuantity':5.0},
        {'symbol':'UPS', 'assetType':'EQUITY', 'averagePrice': 101.49,'longQuantity': 5.0},
        {'symbol':'FDX', 'assetType':'EQUITY', 'averagePrice':188.77, 'longQuantity':5.0},
        {'symbol':'AMD', 'assetType':'EQUITY', 'averagePrice':150.50, 'longQuantity':5.0},
        {'symbol':'NVDA', 'assetType':'EQUITY', 'averagePrice':400.00, 'longQuantity':5.0},
        {'symbol':'AAPL', 'assetType':'EQUITY', 'averagePrice':200.00, 'longQuantity':5.0},
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
#td_capm_df = p1.capm() # USE YAHOO FOR BONDS LATER, CHECK TDA-API DISCORD FOR MORE INFO
print('TD CAPM DF Created')
#print(td_capm_df)

#test_capm_df = p2.capm()
print('Test CAPM DF Created')
#print(test_capm_df)
print()
print('Checkpoint 4 Passed.\n')

#p1.all_to_csv()
#p2.all_to_csv()
#p1.all_to_pickle()
#p2.all_to_pickle()
#p1.all_to_excel()
#p2.all_to_excel()

# Checkpoint 5: Create Graphs
# Pie Chart:

qty = p2._positions_df['longQuantity'].to_list()
names = p2._positions_df.index.to_list()

pc = PieChart(qty, names, 'Solarize_Light2')
#pc.output_plot()

# LineGraph
#exp_ret = (test_capm_df['r_exp']*100).to_list()
#t = test_capm_df.index.to_list()
#title = 'YTD Expected Return'
#xlabel = 'DateTime'
#ylabel = 'Return Rate (%)'
#lg = LineGraph(xlabel, ylabel, title, t, exp_ret)
#lg.output_plot()

print('Checkpoint 5: Building Graphs with MPLFinance...')

ph_amd_1min = PriceHistory(client, 'AMD', '1m', start_dt, end_dt)
ph_amd_5min = PriceHistory(client, 'AMD', '5m', start_dt, end_dt)
ph_amd_10min = PriceHistory(client, 'AMD', '10m', start_dt, end_dt)
ph_amd_1d = PriceHistory(client, 'AMD', '1d', start_dt, end_dt)
ph_amd_1wk = PriceHistory(client, 'AMD', '1w', start_dt, end_dt)


#mpf.plot(ph_amd_1wk.candles, type='candle')
#mpf.plot(ph_amd_1wk.candles, type='renko')
#mpf.plot(ph_amd_1wk.candles, type='pnf')

