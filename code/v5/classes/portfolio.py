
from tda.client import Client
from classes.position import Position
from classes.instrument import Instrument

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

        self.positions = dict()
        for position in positions_list: # position is the position_dictionary
            p = Position(position)
            self.positions[p.get_symbol()] = p.get_data()
            # data should now be in the format {'symbol':{data}}

        # Come up with a way to check the validity of the positions(Checkpoint 2)

        # get all instruments
        # You now have a dictionary of positions you can pull 
        self.instruments = dict()
        for key in self.positions.keys(): # key is the stock's symbol
            if key == 'MMDA1':
                # print('skipped MMDA1')
                break
            else:
                i = Instrument(key, c.search_instruments(key, c.Instrument.Projection('fundamental')).json())
                self.instruments[i.get_symbol] = i.get_data()
        

        # TODO: merge the instruments and positions

    
"""
    def get_price_history(c: Client, symbol: str, periods: str):
        if periods == '1m':
            data = c.get_price_history_every_minute(symbol)
        elif periods == '5m':
            data = c.get_price_history_every_five_minutes(symbol)
        elif periods == '10m':
            data = c.get_price_history_every_ten_minutes(symbol)
        elif periods == '15m':
            data = c.get_price_history_every_fifteen_minutes(symbol)
        elif periods == '30m':
            data = c.get_price_history_every_thirty_minutes(symbol)
        elif periods == '1d':
            data = c.get_price_history_every_day(symbol)
        elif periods == '1w':
            data = c.get_price_history_every_week(symbol)
        elif periods == 'x': # If we don't want Hist Data
            return {}
        else:
            print("wrong period format!")
            return None
        return data.json()
"""