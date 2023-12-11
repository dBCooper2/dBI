from tda.client import Client
import pandas as pd
import datetime as d
# Price History
class PriceHistory:
    def __init__(self, c: Client, symbol: str, periods: str, start: d, end: d) -> None:
        self.c = c
        self.periods = periods
        self.start = start
        self.end = end
        self.candles = self.get_price_history_df(symbol)
    
    def get_price_history_df(self, symbol: str)->pd.DataFrame: # Calls API for Historical Data of a Symbol
        data = None
        if self.periods == '1m':
            data = self.c.get_price_history_every_minute(symbol, start_datetime=self.start, end_datetime=self.end).json()['candles']
        elif self.periods == '5m':
            data = self.c.get_price_history_every_five_minutes(symbol, start_datetime=self.start, end_datetime=self.end).json()['candles']
        elif self.periods == '10m':
            data = self.c.get_price_history_every_ten_minutes(symbol, start_datetime=self.start, end_datetime=self.end).json()['candles']
        elif self.periods == '15m':
            data = self.c.get_price_history_every_fifteen_minutes(symbol, start_datetime=self.start, end_datetime=self.end).json()['candles']
        elif self.periods == '30m':
            data = self.c.get_price_history_every_thirty_minutes(symbol, start_datetime=self.start, end_datetime=self.end).json()['candles']
        elif self.periods == '1d':
            data = self.c.get_price_history_every_day(symbol, start_datetime=self.start, end_datetime=self.end).json()['candles']
        elif self.periods == '1w':
            data = self.c.get_price_history_every_week(symbol, start_datetime=self.start, end_datetime=self.end).json()['candles']
        elif self.periods == 'x':
            return data
        else:
            print("wrong period format!")
            return None
        if isinstance(data, list):
            df = pd.DataFrame(data)
            #print(df.index)
            df['datetime'] = pd.to_datetime(df['datetime'], unit='ms') # convert millis to DateTime object
            df.set_index('datetime', inplace=True)
            return df
        else:
            print('data is not a list, refactor')
            exit()