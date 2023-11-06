# author: Trevor Rowland
# Imports:
from tda.client import Client
import pandas as pd
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
        self.symbol = symbol
        self.periods = periods
        self.candles = self.get_hist_data_json(c)
        if isinstance(self.candles, list):
            self.hist_data = pd.DataFrame(self.candles)
            self.hist_data['datetime'] = pd.to_datetime(self.hist_data['datetime'], unit='ms') # Convert the 'datetime' column to a datetime object (assuming it's in Unix timestamp format)
            self.hist_data.set_index('datetime', inplace=True) # Set the 'datetime' column as the index
        else:
            print('candles are not in list format, exiting...')
            exit()

    def get_hist_data_json(self, c: Client):
        if self.periods == '1m':
            data = c.get_price_history_every_minute(self.symbol)
        elif self.periods == '5m':
            data = c.get_price_history_every_five_minutes(self.symbol)
        elif self.periods == '10m':
            data = c.get_price_history_every_ten_minutes(self.symbol)
        elif self.periods == '15m':
            data = c.get_price_history_every_fifteen_minutes(self.symbol)
        elif self.periods == '30m':
            data = c.get_price_history_every_thirty_minutes(self.symbol)
        elif self.periods == '1d':
            data = c.get_price_history_every_day(self.symbol)
        elif self.periods == '1w':
            data = c.get_price_history_every_week(self.symbol)
        elif self.periods == 'x': # If we don't want Hist Data
            return {}
        else:
            print("wrong period format!")
            return None
        return data.json()