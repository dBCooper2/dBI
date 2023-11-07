# author: Trevor Rowland
# Imports:
from tda.client import Client
import pandas as pd

from classes.price_history import PriceHistory
from classes.position import Position
from classes.instrument import Instrument
import functions as f

#TODO: Write the Constructor, Use Drawings as a Reference
class Portfolio:
    def __init__(self, c: Client, is_simulated:bool, sim_data: dict, periods: str, headers: dict) -> None:
        if is_simulated: # Pull positions from dict, instruments and price hist from API
            self.stock_list = list(sim_data.keys()) # These should be strs of the stock's symbol
            self.prices_list = []
            instruments_dict = {}

            for stock in self.stock_list:
                self.prices_list.append(PriceHistory(c, stock, periods))
                instruments_dict[stock] = Instrument(c, stock)

            self.instruments_df = pd.DataFrame.from_dict(instruments_dict, orient='index')
            self.positions_df = pd.DataFrame.from_dict(sim_data, orient='index')

        elif is_simulated == False: # Pull everything from API
            # this is a lot, for documentation purposes:
            #   - f.get_portfolio calls the API to get the position data
            #   - f.get_headers pulls the account number
            #   - then the whole thing is returned as a list of [positions, balances] so we call [0] to return just the positions
            #   - Then we need to filter out the useless keys and get the positions only, so we access ['securities']['positions']
            acct_data = f.get_portfolio(c, headers['td_acct_num'], False) # This is just the position data

            if isinstance(acct_data, list):
                # Stock symbols are buried, dig for them
                self.stock_list = []
                print(acct_data)
                # Add addtl cusip list here if needed later
                
                self.prices_list = []
                instruments_dict = {}
                positions_dict = {}
                
                for stock in acct_data:
                    self.prices_list.append(PriceHistory(c, stock, periods))
                    instruments_dict[stock] = Instrument(c, stock)
                    positions_dict[stock] = Position(c, self.acct_data[stock])

                for stock in positions_dict.keys():
                    self.stock_list.append(stock)

                self.instruments_df = pd.DataFrame.from_dict(instruments_dict, orient='index')
                self.positions_df = pd.DataFrame.from_dict(positions_dict, orient='index')
            else:
                print('you aren\'t getting a dictionary from calling the list index from get_portfolio')
            
            

            
