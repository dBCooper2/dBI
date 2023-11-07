from tda.client import Client
import pandas as pd

# Acceptable Periods Values: '1m', '5m', '10m', '15m', '30m', '1d', '1w'
class PriceHistory:
    def __init__(self, c: Client, symbol: str, periods: str)->pd.DataFrame: # Arrow indicates expected return type, use it to stay on track
        self.symbol = symbol
        self.periods = periods

        self.candles = self.get_hist_data_json(c)['candles']

        if isinstance(self.candles, list):
            self.hist_data = pd.DataFrame(self.candles)
            # self.hist_data['datetime'] = pd.to_datetime(self.hist_data['datetime'], unit='ms') # Convert the 'datetime' column to a datetime object (assuming it's in Unix timestamp format)
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