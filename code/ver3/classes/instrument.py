# author: Trevor Rowland
# Imports:
from tda.client import Client
import pandas as pd
# Contains an Instrument Object. This class contains relevant ratios and data for a stock.
# Parameters:
# symbol: the string representation of a Stock's ticker symbol
# c: the Client Object created by tda-api. This will be used to create a Client.Instrument.Projection 
#   object and call the API
# projection: a string that will be passed into the Client.Instrument.Projection constructor to make the
#   correct API query parameter
class Instrument:
    def __init__(self, symbol: str, c: Client, projection: str) -> None:
        self.symbol = symbol
        self.projection = projection
        instrument_data = self.get_instrument_json(c)
        # Convert to  Dataframe Row with index=self.symbol
        self.instrument_data = pd.DataFrame.from_dict(instrument_data, orient='index')


    def get_instrument_json(self, c: Client):
        if self.projection == 'fundamental':
            proj = c.Instrument.Projection(self.projection)
            data = c.search_instruments(self.symbol, proj).json()
            data_sorted = {self.symbol:data[self.symbol]['fundamental']} # converts dictionary into {'symbol':{data}} for df constructor
        else:
            data_sorted = None
            print("These endpoints have not been constructed yet!")
        return data_sorted