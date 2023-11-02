# Prompts User for what they want to do with the app
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Imports
import functions as f
from classes.hist_data import HistData
from classes.instrument import Instrument
from classes.position import Position
from classes.stock import Stock, Stock_nb

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