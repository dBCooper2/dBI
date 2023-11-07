
from tda.client import Client
from classes.position import Position
from classes.instrument import Instrument
from classes.price_history import PriceHistory

# ONLY ACCESS POSITION AND INSTRUMENT DATA, CONNECT PRICE HISTORIES LATER
class Portfolio:
    def __init__(self, c: Client, acct_data: dict, periods: str) -> None:
        # get all positions
        #   Sorting acct_data: PASS IN RAW JSON!!!
        positions_list = acct_data['securitiesAccount']['positions']
        if isinstance(positions_list, list):
            print('this is a list. Passed Checkpoint 1')
        else:
            print('Failed Checkpoint 1. Positions Data from API is not of type list')
            exit()

        self.__positions = dict()
        for position in positions_list: # position is the position_dictionary
            p = Position(position)
            self.__positions[p.get_symbol()] = p.get_data()
            # data should now be in the format {'symbol':{data}}

        # Come up with a way to check the validity of the positions(Checkpoint 2)

        # get all instruments
        # You now have a dictionary of positions you can pull 
        self.__instruments = dict()
        self.__price_histories = dict()
        for key in self.__positions.keys(): # key is the stock's symbol
            if key == 'MMDA1':
                # print('skipped MMDA1')
                break
            else:
                # get instruments
                i = Instrument(key, c.search_instruments(key, c.Instrument.Projection('fundamental')).json())
                if key == i.get_symbol: # if symbols match
                    self.__instruments[i.get_symbol()] = i.get_data()
                # get price histories
                ph = PriceHistory(c, key, periods)
                if key == ph.get_symbol: # if symbols match
                    self.__price_histories[ph.get_symbol()] = ph.get_dict()
        
    
