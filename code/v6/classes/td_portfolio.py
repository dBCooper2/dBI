from dataclasses import dataclass
from tda.client import Client
import pandas as pd
import numpy as np
import os
import datetime as d

import functions as f



# TODO: Migrate get_positions(), get_instruments() and get_ph() as class functions
class TD_Portfolio:
    def __init__(self, c: Client, account_number: str, periods: str, start: d, end: d, output_path: str)->None:
        self.c = c
        self.account_number = account_number
        self.periods = periods
        self.start = start # how far back to reach in the historical data
        self.end = end # today as a datetime obj
        self.output_path = output_path
        

        acct = self.__get_account()
        self.__positions_df = self.__get_positions_df(acct)
        self.__symbols_list = self.__positions_df.index.to_list()
        self.__instruments_df = self.__get_instruments_df(self.__symbols_list)

        # Create the Price Histories:
        # put it all in 1 df, horizontally concat
        dfs = []
        for symbol in self.__symbols_list:
            ph_df = self.__get_price_history_df(symbol)
            dfs.append(ph_df)

        df_dict = dict(zip(self.__symbols_list, dfs))
        prefixed_dfs = [df.add_prefix(id_+'_') for id_, df in df_dict.items()]
        self.__ph_df = pd.concat(prefixed_dfs, axis=1)

#------------------------------------------------------------------------------------------------------------------------
# API CALLS FOR DATA
#------------------------------------------------------------------------------------------------------------------------
    def __get_account(self)->dict: # Calls API, returns as a dict, c is the tda Client and an is the account number
        return self.c.get_account(self.account_number, fields=self.c.Account.Fields.POSITIONS).json()
    

    def __get_positions_df(self, raw_acct_data: dict)->pd.DataFrame: # Calls API for all of the positions in a portfolio returns as a Dataframe of all positions, raw_acct_data is the result from get_account(c, an)
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
    

    def __get_instruments_df(self, symbols: list)->pd.DataFrame: # Calls API and returns a DataFrame of all fundamental data
        inst_list = []
        for s in symbols:
            inst = self.c.search_instruments(s, self.c.Instrument.Projection('fundamental')).json()[s]
            inst['fundamental']['cusip'] = inst['cusip']
            inst['fundamental']['description'] = inst['description']
            inst['fundamental']['assetType'] = inst['assetType']
            for key, val in inst['fundamental'].items():
                inst[key] = val
            
            del inst['fundamental']
            inst_list.append(inst)

        inst_df = pd.DataFrame(inst_list)
        inst_df.set_index('symbol', inplace=True)
        # print(inst_df)
        return inst_df
    
    
    def __get_price_history_df(self, symbol: str)->pd.DataFrame: # Calls API for Historical Data of a Symbol
        data = None
        if self.periods == '1m':
            data = self.c.get_price_history_every_minute(symbol, start_datetime=self.start, end_datetime=self.end).json()['candles']
        elif self.periods == '5m':
            data = self.c.get_price_history_every_five_minutes(symbol, start_datetime=self.start, end_datetime=self.end).json()['candles']
        elif self.periods == '10m':
            data = self.c.get_price_history_every_ten_minutes(symbol, start_datetime=self.start, end_datetime=self.end).json()['candles']
        elif self.periods == '15m':
            data = self.c.get_price_history_every_fifteen_minutes(symbol, start_datetime=self.start, end_datetime=self.end).json()['candles']
        elif self.periods == '30m':
            data = self.c.get_price_history_every_thirty_minutes(symbol, start_datetime=self.start, end_datetime=self.end).json()['candles']
        elif self.periods == '1d':
            data = self.c.get_price_history_every_day(symbol, start_datetime=self.start, end_datetime=self.end).json()['candles']
        elif self.periods == '1w':
            data = self.c.get_price_history_every_week(symbol, start_datetime=self.start, end_datetime=self.end).json()['candles']
        elif self.periods == 'x':
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

#------------------------------------------------------------------------------------------------------------------------
# CAPM CALCULATIONS
#------------------------------------------------------------------------------------------------------------------------
    # CAPM: Perform CAPM TODO: REDO TO FIND REQUIRED RETURN
    #   - Calculate Expected Return % for the Portfolio, the Risk Free Rate and the 
    # r_rf_symbol: Risk-Free Rate to gather Data on
    # r_m_symbol: Market Rate to gather data on
    # ph_col: column to use to track expected return(open, close, high, low)
    def capm(self, r_rf_symbol: str, r_m_symbol: str, ph_col: str):
        # Calculate Expected Returns for _c_phdf(these are r_m and r_rf), then create columns Concatenate __c_phdf to __s_phdf horizontally and 
        print('Checkpoint 3a: Can we call the API for r_m and r_rf values...')
        df = pd.DataFrame()
        __r_rf_df = self.__get_price_history_df(r_rf_symbol)
        __r_rf_df = __r_rf_df.filter(like=ph_col) #filter everything except the column we want to check

        __r_rf_df = __r_rf_df.add_prefix(r_rf_symbol+'_')
        # Calculate r_rf Moving Average
        __r_rf_df[r_rf_symbol + '_' + ph_col + '_t-1'] = __r_rf_df[r_rf_symbol + '_' + ph_col].shift(1)
        __r_rf_df[r_rf_symbol + '_r_rf'] = (__r_rf_df[r_rf_symbol + '_' + ph_col]/__r_rf_df[r_rf_symbol + '_' + ph_col + '_t-1'])-1

        __r_rf_df = __r_rf_df.filter(like='r_rf')

        __r_rf_df_cleaned = __r_rf_df.dropna(how='all')
        __r_rf_df_cleaned = __r_rf_df_cleaned.rename(columns={r_rf_symbol + '_r_rf' : 'r_rf'})
        print('Checkpoint 3a: r_rf Accessed and Cleaned into 1 Column...')

        __r_m_df = self.__get_price_history_df(r_m_symbol)
        __r_m_df = __r_m_df.filter(like=ph_col)

        __r_m_df = __r_m_df.add_prefix(r_m_symbol+'_')
        # Calculate r_m Moving Average
        __r_m_df[r_m_symbol + '_' + ph_col + '_t-1'] = __r_m_df[r_m_symbol + '_' + ph_col].shift(1)
        __r_m_df[r_m_symbol + '_r_m'] = (__r_m_df[r_m_symbol + '_' + ph_col]/__r_m_df[r_m_symbol + '_' + ph_col + '_t-1'])-1

        __r_m_df = __r_m_df.filter(like='r_m')

        __r_m_df_cleaned = __r_m_df.dropna(how='all')
        __r_m_df_cleaned = __r_m_df_cleaned.rename(columns={r_m_symbol + '_r_m' : 'r_m'})
        print('Checkpoint 3a: r_m Accessed and Cleaned into 1 Column...\nCheckpoint 3a Passed.\n')

        # Replace this with Calculating Weighted Beta from Instruments, then calculate required rate of return
        print('Checkpoint 3b: Filter Instruments into a Weighted Portfolio Beta...')
        __b_wa = self.get_weighted_betas()
        
        print('Checkpoint 3c: Assembling Final DataFrame...')
        # Final DataFrame Should be r_i, r_rf, and (r_m-r_rf)
        __r_m_minus_r_rf_df = pd.concat([__r_m_df_cleaned, __r_rf_df_cleaned], axis=1)
        __r_m_minus_r_rf_df['r_m-r_rf'] = __r_m_minus_r_rf_df['r_m']-__r_m_minus_r_rf_df['r_rf']
        
        __capm_df = pd.concat([__r_rf_df_cleaned, __r_m_minus_r_rf_df['r_m-r_rf']], axis=1)

        __capm_df['beta_wa'] = __b_wa
        __capm_df['r_i'] = __capm_df['r_rf'] + __capm_df['beta_wa']*__capm_df['r_m-r_rf']
        #print(__capm_df.head())

        comparison_df = self.__get_portfolio_exp_return(ph_col)

        __capm_df = pd.concat([__capm_df, comparison_df], axis=1)

        __capm_df['is_r_i_<_r_exp'] = __capm_df['r_i'] < comparison_df['r_exp']

        return __capm_df

    # 1. Perform a Moving Average on each Price History to calculate Return %'s
    # 2. add each % to a column and perform a weighted Average on each row
    # 3. return the 2 column DF of (datetime, Weighted_exp_return)
    def __get_portfolio_exp_return(self, ph_col: str)->pd.DataFrame:
        exp_ret_df = self.__ph_df.copy()
        #print(exp_ret_df.head())
        exp_ret_df = exp_ret_df.filter(like=ph_col)
        #print(exp_ret_df.head())
        print('Checkpoint 3b: Created Copy...')
        
        for col_name in exp_ret_df.columns:
            exp_ret_df[col_name+'_t-1'] = exp_ret_df[col_name].shift(1)
            exp_ret_df[col_name+'_r_exp'] = (exp_ret_df[col_name] / exp_ret_df[col_name+'_t-1'])-1

        __r_exp_df = exp_ret_df.filter(like='_r_exp')
        __r_exp_df_cleaned = __r_exp_df.dropna(how='all')
        print('Checkpoint 3b: Cleaned DataFrame. Adding Weights...')

        num_shares_list = self.__positions_df['longQuantity'].to_list() # These are all floats
        num_shares_list = [float(val) for val in num_shares_list]
        __r_exp_df_weighted = __r_exp_df_cleaned.mul(num_shares_list, axis=1)
        print('Checkpoint 3b: Weights Added. Computing Average...')
        
        sum_shares = sum(num_shares_list)
        __r_exp_df_weighted['portfolio_r_exp'] = __r_exp_df_weighted.sum(axis=1) / sum_shares
        __final_rexp = __r_exp_df_weighted.filter(like='portfolio')
        __final_rexp = __final_rexp.rename(columns={'portfolio_r_exp' : 'r_exp'})
        print('Checkpoint 3b: Created r_i DataFrame')
        
        return __final_rexp


    def get_weighted_betas(self)->np.float64:
        print(self.__instruments_df.head())
        print(self.__instruments_df['beta'].head())
        print(self.__positions_df['longQuantity'].head())
        df = pd.concat([self.__instruments_df['beta'], self.__positions_df['longQuantity']], axis=1)
        print(df.head())
        df['weighted_beta'] = df['beta'] * df['longQuantity']

        weighted_avg_betas = (np.float64) (df['weighted_beta'].sum() / df['longQuantity'].sum())
        
        return weighted_avg_betas
    

#------------------------------------------------------------------------------------------------------------------------
# EXPORTING TO FILES:
#------------------------------------------------------------------------------------------------------------------------
    def all_to_csv(self)->None:
        os.makedirs(self.output_path, exist_ok=True)

        self.__positions_df.to_csv(os.path.join(self.output_path, 'Positions.csv'))
        self.__instruments_df.to_csv(os.path.join(self.output_path, 'Instruments.csv'))
        self.__ph_df.to_csv(os.path.join(self.output_path, 'All_Positions.csv'))
    
        iscd = self.output_path + '/Positions' # icsd = Individual Stock CSV Directory
        for s in self.__symbols_list:
            df = self.ph_df.loc[self.ph_df['symbol'] == s]
            df.to_csv(os.path.join(iscd, f'{s}.csv'), index=False) 
        return
    

    def all_to_pickle(self):
        path = self.output_path + '/pickles'
        self.__positions_df.to_pickle(path+'/positions.pkl')
        self.__instruments_df.to_pickle(path+'/instruments.pkl')
        self.__ph_df.to_pickle(path+'all_ph.pkl')


    def all_to_excel(self):
        pass


