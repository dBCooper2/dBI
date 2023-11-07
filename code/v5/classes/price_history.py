from tda.client import Client

class PriceHistory:
    def __init__(self, c: Client, symbol: str, periods: str) -> None:
        self.symbol = symbol
        self.periods = periods
        self.data = {} #TODO: pull data(Do it in this class, not functions.py!)
        pass

    def __build_dict(self):
        d = {self.symbol : self.data}

    def get_dict(self):
        return self.__build_dict()