from tda.client import Client

class PriceHistory:
    def __init__(self, c: Client, symbol: str, periods: str):
        self.__symbol = symbol
        self.__periods = periods
        data = self.__get_price_history(c)
        data2 = data['candles']
        self.__data = {self.__symbol:data2} #TODO: pull data(Do it in this class, not functions.py!)

        if isinstance(self.data, dict) & isinstance(self.data[self.__symbol], list):
            print('candles are now a list, inside of a dict with key value == stock symbol')

    def get_symbol(self):
        return self.__symbol

    def __build_dict(self):
        d = {self.__symbol : self.__data}

    def get_dict(self):
        return self.__build_dict()
    
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
        