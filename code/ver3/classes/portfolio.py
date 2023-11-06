# author: Trevor Rowland
# Imports:
from tda.client import Client
from position import Position
# Contains a Portfolio Object made up of a Dictionary of Positions; key = Stock Symbol, Value = Position Obj
# - This object is meant to be used as the primary callee from analysis functions, calling for Stock Objects should 
#       come from those functions, this doesn;t need any HistData or Instrument data
# Parameters:
# - c: the Client Object created by tda-api. This is used to call the API for account data
class Portfolio:
    def __init__(self, c: Client) -> None:
        pass

    def build_instruments_df(): # take in list of instrument dfs, use concat() to put them together
        pass