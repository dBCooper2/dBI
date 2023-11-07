import json

from classes.portfolio import Portfolio
from classes.position import Position
from classes.instrument import Instrument
from classes.price_history import PriceHistory

import functions as f

key = f.get_keys('/Users/trowland/.secret/tda-api.json') # key value pair is 'api_key':'KEY'
headers = f.get_headers('/Users/trowland/.secret/tda-api_data.json') # extra details like Account Number, Redirect URI and Token Path

chrome_path = '/Applications'
chromedriver_path = '/opt/homebrew/bin/chromedriver'

c = f.connect_to_api(key['api_key'], headers['redirect_uri'], headers['token_path'])
print(vars(Portfolio(c, False, None, '5m', headers)))

with open('portfolio_dump.json', "w") as json_file:
    json.dump(vars(Portfolio(c, False, None, '5m', headers)), json_file, indent=4)

print('saved to \'portfolio_dump.json\'')