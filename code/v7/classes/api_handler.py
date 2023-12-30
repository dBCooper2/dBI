from tda.client import Client
from tda import auth as a
import json
import pandas as pd
import datetime as dt

class APIHandler:
    def __init__(self, key_path: str, out_path: str)->None: # Collect keys and tokens for API calls
        self.ak = None
        self.ru = None
        self.tp = None
        self.an = None

        try:
            with open(key_path) as f:
                login_dict = json.load(f)
                self.ak = login_dict['api_key'] # API KEY
                self.ru = login_dict['redirect_uri'] # REDIRECT URI
                self.tp = login_dict['token_path'] # TOKEN PATH
                self.an = login_dict['account_number'] # ACCOUNT NUMBER

        except FileNotFoundError:
            print('Program could not locate your API Key Data!')

        try:
            self.c = a.client_from_token_file(self.tp, self.ak)
        except FileNotFoundError:
            from selenium import webdriver
            with webdriver.Chrome() as driver:
                self.c = a.client_from_login_flow(driver, self.ak, self.ru, self.tp)
        
    # API Responds with an Account JSON, containing Positions, Balances and other Account-Specific Data. Returns a dictionary to be sorted by other functions
    def get_account_with_positions(self)->dict:
        acct = self.c.get_account(self.an, fields=self.c.Account.Fields.POSITIONS).json()
        return acct # returns the raw account dictionary
    
    # Filter the Dictionary to Return just the List of Positions
    def get_position_symbols(self, acct: dict)->list:
        positions_symbols = []
        for idx in acct['securitiesAccount']['positions']:
            if idx['instrument']['symbol'] == 'MMDA1':
                continue
            else: 
                positions_symbols.append(idx['instrument']['symbol'])
        
        return positions_symbols # returns a list of each symbol except mmda1, represented by strings


    
    # Creates a dataframe with the Stock Symbol as the index, with the date the api was accessed(calls datetime.now())
    def get_position_df(self, acct)->pd.DataFrame:
        if isinstance(acct, dict) == False:
                print(acct)
                print('acct is not a list!')
                exit()

        positions_list = []
        

        for idx in acct['securitiesAccount']['positions']:
            print(idx)
            if idx['instrument']['symbol'] == 'MMDA1':
                continue
            else: 
                idx['symbol'] = idx['instrument']['symbol']
                idx['cusip'] = idx['instrument']['cusip']
                idx['assetType'] = idx['instrument']['assetType']

                del(idx['instrument'])

                date_accessed = dt.datetime.now()
                idx['dateAccessed'] = date_accessed

                positions_list.append(idx)

        positions_df = pd.DataFrame(positions_list)
        positions_df.set_index('dateAccessed', inplace=True)
        

        return positions_df # Print the positions dataframe like in v6


    # Accesses the API to get fundamental data for a single Equity and returns a 1 row df to be appended to a larger dataset
    def get_instrument(self, symbol: str)->pd.DataFrame:
        inst = self.c.search_instruments(symbol, self.c.Instrument.Projection('fundamental')).json()
        inst = inst[symbol]
        inst['fundamental']['symbol'] = symbol
        inst['fundamental']['cusip'] = inst['cusip']
        inst['fundamental']['description'] = inst['description']
        inst['fundamental']['assetType'] = inst['assetType']

        date_accessed = [dt.datetime.now()]

        inst2 = inst['fundamental']
        inst_df = pd.DataFrame([inst2], index=date_accessed)
        return inst_df

    def get_candles(self, symbol: str, periods: str, start: dt, end: dt)->pd.DataFrame:
        data = None
        if periods == '1m':
            data = self.c.get_price_history_every_minute(symbol, start_datetime=start, end_datetime=end).json()['candles']
        elif periods == '5m':
            data = self.c.get_price_history_every_five_minutes(symbol, start_datetime=start, end_datetime=end).json()['candles']
        elif periods == '10m':
            data = self.c.get_price_history_every_ten_minutes(symbol, start_datetime=start, end_datetime=end).json()['candles']
        elif periods == '15m':
            data = self.c.get_price_history_every_fifteen_minutes(symbol, start_datetime=start, end_datetime=end).json()['candles']
        elif periods == '30m':
            data = self.c.get_price_history_every_thirty_minutes(symbol, start_datetime=start, end_datetime=end).json()['candles']
        elif periods == '1d':
            data = self.c.get_price_history_every_day(symbol, start_datetime=start, end_datetime=end).json()['candles']
        elif periods == '1w':
            data = self.c.get_price_history_every_week(symbol, start_datetime=start, end_datetime=end).json()['candles']
        elif periods == 'x':
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

    # Returns a List of Symbols from a TDAmeritrade Watchlist
    def get_watchlist(self)->list:
        pass