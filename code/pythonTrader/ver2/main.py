# The main program
import functions as f

key = f.get_keys('/Users/trowland/.secret/tda-api.json') # key value pair is 'api_key':'KEY'
headers = f.get_headers('/Users/trowland/.secret/tda-api_data.json') # key value pairs

chrome_path = '/Applications'
chromedriver_path = '/opt/homebrew/bin/chromedriver'


c = f.connect_to_api(key['api_key'], headers['redirect_uri'], headers['token_path'])

portfolio = f.get_portfolio(c, headers['td_acct_num'])
