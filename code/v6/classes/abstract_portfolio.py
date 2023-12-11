from abc import ABC, abstractmethod
from tda.client import Client
import datetime as d
import pandas as pd
import numpy as np
import os

from classes.price_history import PriceHistory


class AbstractPortfolio(ABC):
    @abstractmethod
    def __init__(self, c: Client, periods: str, start: d, end: d, output_path: str,r_rf_symbol: str, r_m_symbol: str, ph_col: str) -> None:
        self.c = c
        self.periods = periods
        self.start = start # how far back to reach in the historical data
        self.end = end # today as a datetime obj
        self.output_path = output_path
        self.r_rf_symbol = r_rf_symbol
        self.r_m_symbol = r_m_symbol
        self.ph_col = ph_col

        self._symbols_list = []
        self._positions_df = pd.DataFrame()
        self._instruments_df = pd.DataFrame()
        self._ph_df = pd.DataFrame()

    @abstractmethod
    def get_instruments_df(self)->pd.DataFrame: # Calls API and returns a DataFrame of all fundamental data
        inst_list = []
        for s in self._symbols_list:
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
    
    @abstractmethod
    def get_price_history_df(self, symbol: str)->pd.DataFrame: # Calls API for Historical Data of a Symbol
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
    @abstractmethod
    def capm(self):
        # Calculate Expected Returns for _c_phdf(these are r_m and r_rf), then create columns Concatenate __c_phdf to __s_phdf horizontally and 
        
        print('Checkpoint 3a: Can we call the API for r_m and r_rf values...')
        
        # Get Risk-Free Rate
        __r_rf_df = self.get_price_history_df(self.r_rf_symbol)
        __r_rf_df = __r_rf_df.filter(like=self.ph_col) #filter everything except the column we want to check
        __r_rf_df = __r_rf_df.add_prefix(self.r_rf_symbol+'_') # col_names are <stock_name>_<open/close/high/low/volume>

        # Calculate r_rf Moving Average
        __r_rf_df[self.r_rf_symbol + '_' + self.ph_col + '_t-1'] = __r_rf_df[self.r_rf_symbol + '_' + self.ph_col].shift(1)
        __r_rf_df[self.r_rf_symbol + '_r_rf'] = (__r_rf_df[self.r_rf_symbol + '_' + self.ph_col]/__r_rf_df[self.r_rf_symbol + '_' + self.ph_col + '_t-1'])-1
        __r_rf_df = __r_rf_df.filter(like='r_rf')

        __r_rf_df_cleaned = __r_rf_df.dropna(how='all') # drop NaN Values
        __r_rf_df_cleaned = __r_rf_df_cleaned.rename(columns={self.r_rf_symbol + '_r_rf' : 'r_rf'})
        #print('Checkpoint 3a: r_rf Accessed and Cleaned into 1 Column...')

        __r_m_df = self.get_price_history_df(self.r_m_symbol)
        __r_m_df = __r_m_df.filter(like=self.ph_col)
        __r_m_df = __r_m_df.add_prefix(self.r_m_symbol+'_')

        # Calculate r_m Moving Average
        __r_m_df[self.r_m_symbol + '_' + self.ph_col + '_t-1'] = __r_m_df[self.r_m_symbol + '_' + self.ph_col].shift(1)
        __r_m_df[self.r_m_symbol + '_r_m'] = (__r_m_df[self.r_m_symbol + '_' + self.ph_col]/__r_m_df[self.r_m_symbol + '_' + self.ph_col + '_t-1'])-1

        __r_m_df = __r_m_df.filter(like='r_m')

        __r_m_df_cleaned = __r_m_df.dropna(how='all')
        __r_m_df_cleaned = __r_m_df_cleaned.rename(columns={self.r_m_symbol + '_r_m' : 'r_m'})

        #print('Checkpoint 3a: r_m Accessed and Cleaned into 1 Column...\nCheckpoint 3a Passed.\n')
        #print('Checkpoint 3b: Filter Instruments into a Weighted Portfolio Beta...')

        __b_wa = self.__get_weighted_beta() # Create the Portfolio Beta, returns a float representing the weighted average of a beta
        
        #print('Checkpoint 3c: Assembling Final DataFrame...')
        # Final DataFrame Should be r_i, r_rf, and (r_m-r_rf)
        __r_m_minus_r_rf_df = pd.concat([__r_m_df_cleaned, __r_rf_df_cleaned], axis=1)
        __r_m_minus_r_rf_df['r_m-r_rf'] = __r_m_minus_r_rf_df['r_m']-__r_m_minus_r_rf_df['r_rf']
        
        __capm_df = pd.concat([__r_rf_df_cleaned, __r_m_minus_r_rf_df['r_m-r_rf']], axis=1)

        __capm_df['beta_wa'] = __b_wa
        __capm_df['r_i'] = __capm_df['r_rf'] + __capm_df['beta_wa']*__capm_df['r_m-r_rf']
        #print(__capm_df.head())

        comparison_df = self.__get_portfolio_exp_return()

        __capm_df = pd.concat([__capm_df, comparison_df], axis=1)

        __capm_df['is_r_exp_>_r_i'] = comparison_df['r_exp'] > __capm_df['r_i']

        return __capm_df

    # 1. Perform a Moving Average on each Price History to calculate Return %'s
    # 2. add each % to a column and perform a weighted Average on each row
    # 3. return the 2 column DF of (datetime, Weighted_exp_return)
    def __get_portfolio_exp_return(self)->pd.DataFrame:
        exp_ret_df = self._ph_df.copy()
        #print(exp_ret_df.head())
        exp_ret_df = exp_ret_df.filter(like=self.ph_col)
        #print(exp_ret_df.head())
        #print('Checkpoint 3b: Created Copy...')
        
        for col_name in exp_ret_df.columns:
            exp_ret_df[col_name+'_t-1'] = exp_ret_df[col_name].shift(1)
            exp_ret_df[col_name+'_r_exp'] = (exp_ret_df[col_name] / exp_ret_df[col_name+'_t-1'])-1

        __r_exp_df = exp_ret_df.filter(like='_r_exp')
        __r_exp_df_cleaned = __r_exp_df.dropna(how='all')
        #print('Checkpoint 3b: Cleaned DataFrame. Adding Weights...')

        num_shares_list = self._positions_df['longQuantity'].to_list() # These are all floats
        num_shares_list = [float(val) for val in num_shares_list]
        __r_exp_df_weighted = __r_exp_df_cleaned.mul(num_shares_list, axis=1)
        #print('Checkpoint 3b: Weights Added. Computing Average...')
        
        sum_shares = sum(num_shares_list)
        __r_exp_df_weighted['portfolio_r_exp'] = __r_exp_df_weighted.sum(axis=1) / sum_shares
        __final_rexp = __r_exp_df_weighted.filter(like='portfolio')
        __final_rexp = __final_rexp.rename(columns={'portfolio_r_exp' : 'r_exp'})
        #print('Checkpoint 3b: Created r_i DataFrame')
        
        return __final_rexp


    def __get_weighted_beta(self)->np.float64:
        df = pd.concat([self._instruments_df['beta'], self._positions_df['longQuantity']], axis=1)
        df['weighted_beta'] = df['beta'] * df['longQuantity']
        weighted_avg_of_betas = (np.float64) (df['weighted_beta'].sum() / df['longQuantity'].sum()) # This is a weighted Portfolio Beta that goes into every row of the beta column
        return weighted_avg_of_betas

#------------------------------------------------------------------------------------------------------------------------
# EXPORTING TO FILES:
#------------------------------------------------------------------------------------------------------------------------
    @abstractmethod
    def all_to_csv(self)->None:
        fpath = self.output_path + '/csv/'
        os.makedirs(fpath, exist_ok=True)

        self._positions_df.to_csv(os.path.join(fpath, 'Positions.csv'))
        self._instruments_df.to_csv(os.path.join(fpath, 'Instruments.csv'))
        self._ph_df.to_csv(os.path.join(fpath, 'All_Positions.csv'))
    
        iscd = fpath + '/price_histories/' # icsd = Individual Stock CSV Directory
        os.makedirs(iscd, exist_ok=True)
        for s in self._symbols_list:
            df = self._ph_df.filter(like=s)
            df.to_csv(os.path.join(iscd, f'{s}.csv'))
        pass
    
    @abstractmethod
    def all_to_pickle(self):
        fpath = self.output_path + '/pickles/'
        os.makedirs(fpath, exist_ok=True)

        self._positions_df.to_pickle(fpath+'/positions.pkl')
        self._instruments_df.to_pickle(fpath+'/instruments.pkl')

        iscp = fpath + '/price_histories/' # iscd = individual stock data pickles
        for s in self._symbols_list:
            ssd = self._ph_df.filter(like=s) # ssd = single stock data

            # remove the prefix 'name_'
            new_names = [col.replace(f'{s}_', '') for col in ssd.columns] # Copies the column names into a new array without the prefix
            ssd.rename(columns=dict(zip(ssd.columns, new_names)), inplace=True) # renames all the columns with the new names
            ssd['symbol'] = s # add a column with the stock's symbol

            ssd.to_pickle(iscp+f'{s}.pkl')

    @abstractmethod
    def all_to_excel(self):
        fpath = self.output_path + '/xlsx/'
        os.makedirs(fpath, exist_ok=True)

        with pd.ExcelWriter(fpath+'portfolio.xlsx') as writer:
            # Write each DataFrame to a different sheet
            self._positions_df.to_excel(writer, sheet_name='positions', index=False)
            self._instruments_df.to_excel(writer, sheet_name='instruments', index=False)

            for s in self._symbols_list:
                self._ph_df.filter(like=s).to_excel(writer, sheet_name=s, index=False)