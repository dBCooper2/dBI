from dataclasses import dataclass #TODO

class Instrument:
    def __init__(self, symbol: str, instrument_dict: dict) -> None:
        # format into {'symbol':{data:dict}}
        # skip adding assetType, already included in positions
        self.symbol = symbol
        
        data = instrument_dict[self.symbol]['fundamental']
        # add exchange to the dict
        data['exchange'] = instrument_dict[self.symbol]['exchange']
        # add decription to the dict
        data['description'] = instrument_dict[self.symbol]['description']
        # NOTE: add cusip here if needed

        # delete duplicate vals
        self.data = dict()
        self.data['symbol'] = self.symbol
        for key in data:
            self.data[key] = data[key]

    def __build_dict(self):
        d = {self.symbol:self.data}

    def get_dict(self):
        return self.__build_dict()
    
    def get_symbol(self): # Used to get a key
        return self.symbol
    
    def get_data(self): # Used to access the value
        return self.data