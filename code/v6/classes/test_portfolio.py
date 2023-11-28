from classes.abstract_portfolio import AbstractPortfolio
from tda.client import Client
import datetime as d
import numpy as np
import pandas as pd

class TestPortfolio(AbstractPortfolio):
    def __init__(self, c: Client, acct_dict, periods: str, start: d, end: d, output_path: str, r_rf_symbol: str, r_m_symbol: str, ph_col: str)->None:
        super().__init__(c, periods, start, end, output_path, r_rf_symbol, r_m_symbol, ph_col)
        self.acct = acct_dict
        self._positions_df = self.get_positions_df(self.acct)
        self._symbols_list = self._positions_df.index.to_list()
        self._instruments_df = self.get_instruments_df()

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
    def get_positions_df(self, acct_dict: dict)->pd.DataFrame:
        df = pd.DataFrame(acct_dict['data'])
        df.set_index(df['symbol'], inplace=True)
        return df


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