
from tda.client import Client
import pandas as pd

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

        self.__positions_dict = dict()
        for position in positions_list: # position is the position_dictionary
            if position['instrument']['symbol'] == 'MMDA1':
                print('MMDA1 Not Added')
                continue
            else:
                p = Position(position)
                self.__positions_dict[p.get_symbol()] = p.get_data()
                # data should now be in the format {'symbol':{data}} and skip

        # Come up with a way to check the validity of the positions(Checkpoint 2)

        # get all instruments
        # You now have a dictionary of positions you can pull 
        self.__instruments_dict = dict()
        self.__price_history_dict = dict()
        for key in self.__positions_dict.keys(): # key is the stock's symbol
            if key == 'MMDA1':
                print('MMDA1 wasn\'t sorted out, exiting...')
            else:
                # get instruments
                i = Instrument(key, c.search_instruments(key, c.Instrument.Projection('fundamental')).json())
                if key == i.get_symbol(): # if symbols match
                    self.__instruments_dict[i.get_symbol()] = i.get_data()
                else:
                    self.__instruments_dict[i.get_symbol()] = i.get_data() # Just get 1 for simplicity
                    break
                # get price histories
                ph = PriceHistory(c, key, periods)
                if key == ph.get_symbol(): # if symbols match
                    self.__price_history_dict[ph.get_symbol()] = ph.df
                else:
                    print('didn\'t create the dict')

        # create dataframes of the dictionaries                    
        self.positions_df = self.dict_to_df(self.__positions_dict)
        self.instruments_df = self.dict_to_df(self.__instruments_dict)
        self.merged_i_p_df = self.merge_positions_and_instuments(self.positions_df, self.instruments_df)
        

    def dict_to_df(self, ps: dict):
        return pd.DataFrame.from_dict(ps, orient='index')
    
    
    def merge_positions_and_instuments(self, pos: dict, inst: dict):
        pass

    def get_one_price_history(self, symbol:str):
        return self.__price_history_dict[symbol]
    
    def get_all_price_history(self):
        return self.__price_history_dict