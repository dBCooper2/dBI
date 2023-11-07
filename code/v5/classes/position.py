# NOTE: Data is received as a sub-dictionary from the 'positions':[positions] section of the get_account() API call

class Position:
    def __init__(self, position_dict: dict) -> None:
        self.symbol = position_dict['instrument']['symbol']
        data = position_dict
        data['assetType'] = data['instrument']['assetType'] # Put Asset Type in the dict before deleting the 'instrument' sub-dict
        # NOTE: add cusip storage here if you need it later
        del data['instrument'] # delete the instruments sub-dict
        self.data = data

    def __build_dict(self):
        d = {self.symbol:self.data}

    def get_dict(self):
        return self.__build_dict()
    
    def get_symbol(self):
        return self.symbol
    
    def get_data(self):
        return self.data
