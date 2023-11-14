from tda.client import Client
import pandas as pd

class PriceHistory:
    def __init__(self, c: Client, symbol: str, periods: str):
        self.__symbol = symbol
        self.__periods = periods

        __response_dict = self.__get_price_history(c) # This returns {'candles':[{data},{data},{data}]}
        
        for d in __response_dict['candles']: # d is a dictionary
            # insert the symbol
            d['symbol'] = self.__symbol
        # convert to {'symbol':[{data}, {data}, {data}]}
        self.__data = {self.__symbol:__response_dict['candles']}
        # print(self.__data)

        self.df = self.__build_price_history_df(self.__data)


    def get_symbol(self):
        return self.__symbol

    def __build_price_history_df(self, ph: dict):
        df = pd.DataFrame.from_records(ph[self.__symbol])

        df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
        df.set_index('datetime', inplace=True)
        
        return df

    def __dump_json_to_file(self, data):
        with open('price_history_check.json', 'w') as file:
            import json
            json.dump(self.__data, file)
    
    def __get_price_history(self, c: Client):
        if self.__periods == '1m':
            __data = c.get_price_history_every_minute(self.__symbol)
            return __data.json()
        elif self.__periods == '5m':
            __data = c.get_price_history_every_five_minutes(self.__symbol)
            return __data.json()
        elif self.__periods == '10m':
            __data = c.get_price_history_every_ten_minutes(self.__symbol)
            return __data.json()
        elif self.__periods == '15m':
            __data = c.get_price_history_every_fifteen_minutes(self.__symbol)
            return __data.json()
        elif self.__periods == '30m':
            __data = c.get_price_history_every_thirty_minutes(self.__symbol)
            return __data.json()
        elif self.__periods == '1d':
            __data = c.get_price_history_every_day(self.__symbol)
            return __data.json()
        elif self.__periods == '1w':
            __data = c.get_price_history_every_week(self.__symbol)
            return __data.json()
        elif self.__periods == 'x':
            return {}
        else:
            print("wrong period format!")
            return None
        