#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Imports
import pandas as pd
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Class that takes the 'candles' key(name of data points from API) from tda-api and translates it into a dict to be converted 
# takes in list of indeterminate length
# each list item is a dict with keys: open: double, high: double, low: double, close: double, volume: int64, datetime: int64
# create pandas dataframe, rows are datetime vals, cols are open, high, low, close and volume
class HistData:
	def __init__(self, symbol: str, candles_list: list):
		self.symbol = symbol
		if isinstance(candles_list, list):
			self.hist_data = pd.DataFrame(candles_list)
			self.hist_data['datetime'] = pd.to_datetime(self.hist_data['datetime'], unit='ms') # Convert the 'datetime' column to a datetime object (assuming it's in Unix timestamp format)
			self.hist_data.set_index('datetime', inplace=True) # Set the 'datetime' column as the index
		else:
			print('candles are not in list format, exiting...')
			exit()
			