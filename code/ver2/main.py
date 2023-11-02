# Prompts User for what they want to do with the app
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Imports
import functions as f
from classes import Stock, Stock_nb, Position

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Main Method Pseudocode
"""
Prompt if the user wants to view their portfolio or perform analysis
if user wants to view portfolio...
    call get_account
    filter portfolio into positions and balances
    output poisitions in a sorted, clean list
    output balances
else if user wants to view portfolio but passes in the param --no-balances...
    call get_account
    filter portfolio into just positions
    output positions but withold all cash amount, output price of stocks and P/L %s for the day ONLY
else if user wishes to perform analysis...
    prompt if they want to analyze a single stock, a custom portfolio of stocks or your own portfolio
        if your own portfolio is chosen...
            call get_account
            filter positions and balances
            with positions...
                create position objects and append to a list(Skip Symbol 'MMDA')
                create Stock objects from that list
                output dataframes and prompt the user what format they want the output to be
                    if csv...
                        output csv to the desktop
                    else if excel...
                        output .xlsx to the desktop
                    else if tableau...
                        perform analysis
                        TBD - output as tableau dashboard
        if custom portfolio is chosen...
            prompt for stocks, user types done when they are done creating the list
            prompt for number of shares with each stock
            search for positions with get_instrument('symbol-search'), append to list of tuples(symbol, cusip) or except if the symbol is not found
                - possibly prompt at runtime to re-search the symbol if it was a typo
            iterate through list of tuples, create Stock objects
            output dataframes and prompt the user what format they want the output to be
                    if csv...
                        output csv to the desktop
                    else if excel...
                        output .xlsx to the desktop
                    else if tableau...
                        perform analysis
                        TBD - output as tableau dashboard
        if single stock is chosen...
            prompt for symbol
            search for symbol with get_instrument('symbol-search')
            create Stock Object
            output dataframes and prompt the user what format they want the output to be
                    if csv...
                        output csv to the desktop
                    else if excel...
                        output .xlsx to the desktop
                    else if tableau...
                        perform analysis
                        TBD - output as tableau dashboard
"""
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
key = f.get_keys('/Users/trowland/.secret/tda-api.json') # key value pair is 'api_key':'KEY'
headers = f.get_headers('/Users/trowland/.secret/tda-api_data.json') # extra details like Account Number, Redirect URI and Token Path

chrome_path = '/Applications'
chromedriver_path = '/opt/homebrew/bin/chromedriver'

print('Welcome to dBI. Connecting to API...')
c = f.connect_to_api(key['api_key'], headers['redirect_uri'], headers['token_path'])
print('API Connected.')
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Do Any Testing Here so you don't have to go through the Input Section
data = f.get_portfolio(c, headers['td_acct_num'], True)
stock_list = []
for idx in data[0]:
    s = Position(idx)
    s2 = Stock_nb(s.symbol, s.cusip, s)
    stock_list.append(s2)


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


user_in = input('Do you want to:\n1. View Your Portfolio\n2. Perform Analysis on a Stock/Portfolio\nPlease enter the number of the task you want performed\n')
data = f.get_portfolio(c, headers['td_acct_num'], True)
if user_in == '1': # View the Portfolio
    print('Portfolio Loading...')

    #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
elif user_in == '1 --no-balances': # View the Portfolio without displaying any compromising financial info
    print('Portfolio Loading...')
    stock_list = []
    for idx in data[0]:
        s = Position(idx)
        s2 = Stock_nb(s.symbol, s.cusip, s)
        stock_list.append(s2)
        f.stocknb_tostring(stock_list)
    #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
elif user_in == '2': # Perform Data Analysis
    user_in = '0'
    user_in = input('Do you want to:\n1. Analyze a Single Stock\n2. Analyze your Portfolio\nAnalyze a Custom Portfolio\nPlease enter the number of the task you want performed\n')
    #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    if user_in == '1': # Analyze a Single Stock
        pass # prompt for stock symbol
        #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    elif user_in == '2': # Analyze the User's Portfolio
        pass
        #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    elif user_in == '3': # Analyze a Custom Portfolio
        pass # prompt for stocks