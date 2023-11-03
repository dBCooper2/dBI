# author: Trevor Rowland
# Imports:
from tda.client import Client
# Contains a Historical_Data Object. This Object contains 
#   Price History for a given stock to be used for analysis 
#   in conjunction with a Portfolio Object, and will be nested 
#   inside of a Stock Object.
# Parameters:
#  - symbol: a string representation of a Stock's Ticker Symbol
#  - c: the Client Object created by tda-api. This will be used to 
#       call the API for Price History Data
# - periods: a string representation of the number of datapoints the
#       API call will include in the price history
#       Vals: 1m, 5m, 10m, 15m, 30m, 1d, 1w
class HistData:
    def __init__(self, symbol: str, c: Client, periods: str) -> None:
        pass