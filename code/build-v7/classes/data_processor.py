from classes.api_handler import APIHandler

import pandas as pd
import datetime as dt
import logging as l

class DataProcessor:
    def __init__(self, path_to_files: str) -> None:
        self.p = path_to_files

    def positions_to_csv(self, df: pd.DataFrame) -> None:
        today = dt.date.today().strftime()
        filename = self.op + f'/Positions_{today}.csv'

        l.info('Attempting to Save to CSV...')
        try:
            df.to_csv(filename, index=True)
        except Exception as e:
            l.error(e)
            exit()

    def positions_to_pkl(self, df: pd.DataFrame) -> None:
        today = dt.date.today().strftime()
        filename = self.op + f'/Positions_{today}.pkl'

        l.info('Attempting to Save to PKL...')
        try:
            df.to_pickle(filename, index=True)
        except Exception as e:
            l.error(e)
            exit()

    def instruments_to_csv(self, df: pd.DataFrame) -> None:
        today = dt.date.today().strftime()
        filename = self.op + f'/Instruments_{today}.csv'

        l.info('Attempting to Save to CSV...')
        try:
            df.to_csv(filename, index=True)
        except Exception as e:
            l.error(e)
            exit()

    def instruments_to_pkl(self, df: pd.DataFrame) -> None:
        today = dt.date.today().strftime()
        filename = self.op + f'/Instruments_{today}.pkl'

        l.info('Attempting to Save to PKL...')
        try:
            df.to_pickle(filename, index=True)
        except Exception as e:
            l.error(e)
            exit()

    def candles_to_csv(self, symbol: str, df: pd.DataFrame) -> None:
        today = dt.date.today().strftime()
        filename = self.op + f'/Candles_{symbol}_{today}.csv'
        try:
            df.to_csv(filename, index=True)
        except Exception as e:
            l.error(e)
            exit()

    def candles_to_pkl(self, symbol: str, df: pd.DataFrame) -> None:
        today = dt.date.today().strftime()
        filename = self.op + f'/Candles_{symbol}_{today}.pkl'
        try:
            df.to_pickle(filename, index=True)
        except Exception as e:
            l.error(e)
            exit()

    def get_df_from_file(self, filename: str, ) -> pd.DataFrame:
        fp = self.p + f'/{filename}'
        
        try:
            filetype = filename[:-4]
        except IndexError as e:
            l.error(e)
            l.error("Index Out of Bounds! Check that the file has an extension!")

        df = pd.DataFrame()

        if filetype == ".csv":
            df = pd.read_csv(fp)
        elif filetype == ".pkl":
            df = pd.read_pickle(fp)
        elif filetype == "xlsx" & filename[:-5] == ".xlsx":
            # TODO: Add Later
            df = {} # df will now be a dict of all the dataframes in the excel file
            df = self.__clean_xl_sheet(fp)
            pass
        else:
            l.error("invalid file type! Exiting...")
            exit()
        
        return df
    
    def __clean_xl_sheet(self, fp: str) ->dict:
        # Go through the Excel File and append each sheet to the dict as a key-value pair 'sheetName' : DataFrame
        pass