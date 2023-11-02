# The main program
import functions as f
from classes import Stock

key = f.get_keys('/Users/trowland/.secret/tda-api.json') # key value pair is 'api_key':'KEY'
headers = f.get_headers('/Users/trowland/.secret/tda-api_data.json') # key value pairs

chrome_path = '/Applications'
chromedriver_path = '/opt/homebrew/bin/chromedriver'


c = f.connect_to_api(key['api_key'], headers['redirect_uri'], headers['token_path'])

#portfolio = f.get_portfolio(c, headers['td_acct_num'])
"""
data = f.get_stock_hist_data(c, 'AMD', '5m')
import json
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print()
"""
#print(f.get_stock_info(c, 'AMD', 'symbol-search'))
print()
#print(f.get_stock_info(c, 'AMD', 'fundamental'))
amd_symbol = 'AMD'
amd_cusip = '007903107'
data = Stock(amd_symbol, amd_cusip, c, '1w')
print(vars(data))
print(vars(data.instruments))
print(vars(data.hist_data))


# Main Method Pseudocode
# Call get_account()
# For positions in Account:
#   Access Stock Symbol and CUSIP
#   Create Stock object for each stock in Portfolio
#   Skip Symbol 'MMDA'

