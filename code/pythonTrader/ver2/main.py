# The main program
import functions as f

key = f.get_keys('/Users/trowland/.secret/tda-api.json') # key value pair is 'api_key':'KEY'
headers = f.get_headers('/Users/trowland/.secret/tda-api_data.json') # key value pairs
chrome_path = '/Applications'
chromedriver_path = '/opt/homebrew/bin/chromedriver'


f.connect_to_api(chrome_path, chromedriver_path, key['api_key'], headers['redirect_uri'], headers['token_path'])

#portfolio = get_portfolio(params)

#for stock in portfolio:
#    print(expected_return(stock))

#print(expected_return(portfolio))

# add stock and portfolio data to a db