# author Trevor Rowland
# Imports:
from tda.client import Client

# Contains a Stock Object. A Stock is a collection of Data for a Stock, 
#   meant to be used with the Data Analysis tools or exporting specific data,
#   not for viewing a stock's performance in a Portfolio. This is meant as an 
#   interface to get more data about a specific stock in the portfolio.Stocks 
#   also contain a HistData object and an Instrument object that contain 
#   relevant ratios and price history to be combined with data in a portfolio for analysis.
# Parameters:
# - symbol: the stock's ticker symbol
# - c: the Client Object created by tda-api. This is used to call the API for historical data and Instrument Data
# - periods: the number of periods the nested HistData object should call data from
#       Vals: 1m, 5m, 10m, 15m, 30m, 1d, 1w
class Stock:
	def __init__(self, symbol: str, c: Client, periods: str):
		pass