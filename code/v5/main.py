from tda.client import Client
from classes.portfolio import Portfolio  
import functions as f

key_dict = f.get_keys('/Users/trowland/.secret/tda-api.json') # key value pair is 'api_key':'KEY'
headers_dict = f.get_headers('/Users/trowland/.secret/tda-api_data.json') # extra details like Account Number, Redirect URI and Token Path

chrome_path = '/Applications'
chromedriver_path = '/opt/homebrew/bin/chromedriver'

client_obj = f.connect_to_api(key_dict['api_key'], headers_dict['redirect_uri'], headers_dict['token_path'])
print('connected to api')

acct_dict = f.get_acct(client_obj, headers_dict['td_acct_num'], False)
#print(acct_dict)
print('received acct data')
if isinstance(acct_dict, dict) & isinstance(client_obj, Client):
    print('params are correct format')

p = Portfolio(client_obj, acct_dict, '')
print(p)
print()
print('Positions\n')
print(p.positions)
print()
print('Instruments\n')
print(p.instruments)