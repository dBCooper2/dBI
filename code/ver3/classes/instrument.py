# author: Trevor Rowland
# Imports:
from tda.client import Client
# Contains an Instrument Object. This class contains relevant ratios and data for a stock.
# Parameters:
# symbol: the string representation of a Stock's ticker symbol
# c: the Client Object created by tda-api. This will be used to create a Client.Instrument.Projection 
#   object and call the API
# projection: a string that will be passed into the Client.Instrument.Projection constructor to make the
#   correct API query parameter
class Instrument:
    def __init__(self, symbol: str, c: Client, projection: str) -> None:
        pass