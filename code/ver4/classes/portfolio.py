# author: Trevor Rowland
# Imports:
from tda.client import Client
import pandas as pd

#TODO: Write the Constructor, Use Drawings as a Reference
class Portfolio:
    def __init__(self, c: Client, is_simulated:bool, sim_data: dict) -> None:
        if is_simulated: # Pull positions from dict, instruments and price hist from API
            self.stock_list = list(sim_data.keys())
            self.prices_list = []
            for stock in self.stock_list:
                continue # get price history for each stock
            self.instruments_df = pd.DataFrame()
            self.positions_df = pd.DataFrame.from_dict(sim_data, orient='index')
        elif is_simulated == False: # Pull everything from API
            self.stock_list = []
            self.prices_list = []
            self.instruments_df = pd.DataFrame()
            self.positions_df = pd.DataFrame()
