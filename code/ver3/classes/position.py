# author: Trevor Rowland
from tda.client import Client
# Contains a Position Object. A Position is a Stock held by the Account, 
#   and only contains data relating to the stock's performance in the
#   portfolio. This class should only generate data from the account and 
#   will be added to a Portfolio Object as a List
# Parameters:
# - symbol: a string representation of the Stock's Ticker Symbol. Used for accessing key-value pairs
# - data: a dictionary that is a subdictionary of the Portfolio's account json returned by the API
class Position:
    def __init__(self, symbol: str, data: dict) -> None:
        pass
