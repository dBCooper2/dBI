
from tda.client import Client
from classes.position import Position

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

        # get all instruments
        # TODO: merge the instruments and positions
