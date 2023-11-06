# author: Trevor Rowland
# Imports:
from tda.client import Client
from position import Position
from stock import Stock
# Contains a Portfolio Object made up of a Dictionary of Positions; key = Stock Symbol, Value = Position Obj
# - This object is meant to be used as the primary callee from analysis functions, calling for Stock Objects should 
#       come from those functions, this doesn;t need any HistData or Instrument data
# Parameters:
# - c: the Client Object created by tda-api. This is used to call the API for account data
# - is_simulated: a Boolean meant to differentiate if the stock should pull actual position data or make up its own with 
#       parameter sim_data
# - sim_data: a Dictionary in the format {'symbol1':{data}, 'symbol2':{data}, ..., 'symbolN':{data}} that simulates a 
#       portfolio of stocks to analyze
# - periods: The number of periods for the Price History Data, Accepted Vals = 1m, 5m, 10m, 15m, 30m, 1d, 1w
class Portfolio:
    def __init__(self, c: Client, is_simulated:bool, sim_data: dict, periods:str) -> None:
        self.stock_list = []
        if is_simulated == False: # if the portfolio is from the TD User's account
            pass # call get_account(), get list of stocks, call Stock() for each item
        elif is_simulated: # simulated portfolio
            stock_list = [sim_data.keys()]
            for stock in stock_list:
                continue
            pass


    def build_instruments_df(self): # take in list of instrument dfs, use concat() to put them together
        for instruments in self.stock_data:
            continue
        pass