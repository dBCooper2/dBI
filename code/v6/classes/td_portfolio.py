from dataclasses import dataclass
from tda.client import Client
import pandas as pd
import numpy as np
import os
import datetime as d

import functions as f
from classes.abstract_portfolio import AbstractPortfolio



# TODO: Migrate get_positions(), get_instruments() and get_ph() as class functions
class TD_Portfolio(AbstractPortfolio):
    def __init__(self, c: Client, account_number: str, periods: str, start: d, end: d, output_path: str, r_rf_symbol: str, r_m_symbol: str, ph_col: str)->None:
        super().__init__(c, periods, start, end, output_path, r_rf_symbol, r_m_symbol, ph_col)
        
        self.account_number = account_number
        self.acct = self.__get_account()
        self._positions_df = self.get_positions_df(self.acct)
        self._symbols_list = self._positions_df.index.to_list()
        self._instruments_df = self.get_instruments_df()

        # Create the Price Histories:
        # put it all in 1 df, horizontally concat
        dfs = []
        for symbol in self._symbols_list:
            ph_df = self.get_price_history_df(symbol)
            dfs.append(ph_df)

        df_dict = dict(zip(self._symbols_list, dfs))
        prefixed_dfs = [df.add_prefix(id_+'_') for id_, df in df_dict.items()]
        self._ph_df = pd.concat(prefixed_dfs, axis=1)

#------------------------------------------------------------------------------------------------------------------------
# API CALLS FOR DATA
#------------------------------------------------------------------------------------------------------------------------
    def __get_account(self)->dict: # Calls API, returns as a dict, c is the tda Client and an is the account number
        return self.c.get_account(self.account_number, fields=self.c.Account.Fields.POSITIONS).json()
    

    def get_positions_df(self, raw_acct_data: dict)->pd.DataFrame: # Calls API for all of the positions in a portfolio returns as a Dataframe of all positions, raw_acct_data is the result from get_account(c, an)
        raw_acct_data = raw_acct_data['securitiesAccount']['positions']
        positions_list = []
        for idx in raw_acct_data:
            if isinstance(idx, dict) == False:
                print(idx)
                print('idx is not a dictionary! It must be an index')
                exit()

            if idx['instrument']['symbol'] == 'MMDA1':
                continue
            else: 
                idx['symbol'] = idx['instrument']['symbol']
                idx['cusip'] = idx['instrument']['cusip']
                idx['assetType'] = idx['instrument']['assetType']

                del(idx['instrument'])
                positions_list.append(idx)

        positions_df = pd.DataFrame(positions_list)
        positions_df.set_index('symbol', inplace=True)
        # print(positions_df)
        return positions_df
    

    def get_instruments_df(self) -> pd.DataFrame: return super().get_instruments_df()
    def get_price_history_df(self, symbol: str) -> pd.DataFrame: return super().get_price_history_df(symbol)
#------------------------------------------------------------------------------------------------------------------------
# CAPM CALCULATIONS
#------------------------------------------------------------------------------------------------------------------------
    def capm(self)->pd.DataFrame: return super().capm()
    def __get_portfolio_exp_return(self) -> pd.DataFrame: return super().__get_portfolio_exp_return()
    def __get_weighted_betas(self) -> np.float64: return super().__get_weighted_betas()
#------------------------------------------------------------------------------------------------------------------------
# EXPORTING TO FILES:
#------------------------------------------------------------------------------------------------------------------------
    def all_to_csv(self) -> None: return super().all_to_csv()
    def all_to_pickle(self)->None: return super().all_to_pickle()
    def all_to_excel(self)->None: return super().all_to_excel()
