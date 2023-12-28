from classes.api_handler import APIHandler
import pandas as pd
import datetime as dt

# Configs
tda_api_configs = '/Users/dB/.secret/tda-api-v6.json' # Add /Users/username/.secret/path/to/api_key/file
output_path = '/Users/dB/Documents/pythonTrader_Data/output/' # Add /Users/username/Documents/output/repo

end_dt = dt.datetime.now() # Use as End in Portfolio params
start_dt = end_dt - dt.timedelta(days = 28) # Use as start in Portfolio params

mpl_chart_style = 'Solarize_Light2'

ah = APIHandler(tda_api_configs, output_path)
acct_dict = ah.get_account_with_positions()
#print(acct_dict)

print()
print('positions symbols:')
print(ah.get_position_symbols(acct_dict))

print()
print('positions dataframe:')
#print(ah.get_position_df(acct_dict).head())
print(ah.get_position_df(acct_dict).columns)

print()
print('price_history_AMD')
#print(ah.get_candles('AMD', '5m', start_dt, end_dt))

print()
print('Instruments_AMD')
print(ah.get_instrument('AMD').columns)
