#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Classes for the Program
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Imports
from tda.client import Client
import functions as f
import pandas as pd
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Positions Object: Contains Data from get_account() API calls
class Position:
    def __init__(self, symbol: str, cusip: str, position_data: dict):
        self.symbol = symbol
        if self.symbol != position_data['instrument']['symbol']:
            print('The Symbols Stopped Matching! Check your Code!')
            exit()
        self.cusip = position_data['instrument']['cusip']
        self.type = position_data['instrument']['assetType']

        self.shortQuantity = position_data['shortQuantity']
        self.averagePrice = position_data['averagePrice']
        self.currentDayCost = position_data['currentDayCost']
        self.currentDayProfitLoss = position_data['currentDayProfitLoss']
        self.currentDayProfitLossPercentage = position_data['currentDayProfitLossPercentage']
        self.longQuantity = position_data['longQuantity']
        self.settledLongQuantity = position_data['settledLongQuantity']
        self.settledShortQuantity = position_data['settledShortQuantity']
        self.marketValue = position_data['marketValue']
        self.maintenanceRequirement = position_data['maintenanceRequirement']
        self.previousSessionLongQuantity = position_data['previousSessionLongQuantity']

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Instrument:
    def __init__(self, symbol: str, json: dict):
        f = 'fundamental'
        self.symbol = symbol
        if self.symbol != json[symbol]['symbol']:
            print('The Symbols Stopped Matching! Check your Code!')
            exit()
        self.cusip = json[symbol]['cusip']
        self.description = json[symbol]['description']
        self.exchange = json[symbol]['exchange']
        self.assetType = json[symbol]['assetType']

        self.high52 = json[symbol][f]['high52']
        self.low52 = json[symbol][f]['low52']
        self.marketCap = json[symbol][f]['marketCap']
        #self.dividendAmount = json[symbol][f]['dividentAmount']
        #self.dividendYield = json[symbol][f]['dividendYield']
        #self.dividendDate = json[symbol][f]['dividendDate']
        #self.dividendPayAmount = json[symbol][f]['dividendPayAmount']
        #self.divGrowthRate3Year = json[symbol][f]['divGrowthRate3Year']
        #self.dividendPayDate = json[symbol][f]['dividendPayDate']
        self.beta = json[symbol][f]['beta']
        self.peRatio = json[symbol][f]['peRatio']
        self.pegRatio = json[symbol][f]['pegRatio']
        self.pbRatio = json[symbol][f]['pbRatio']
        self.prRatio = json[symbol][f]['prRatio']
        self.pcfRatio = json[symbol][f]['pcfRatio']
        self.quickRatio = json[symbol][f]['quickRatio']
        self.currentRatio = json[symbol][f]['currentRatio']
        self.grossMarginTTM = json[symbol][f]['grossMarginTTM']
        self.grossMarginMRQ = json[symbol][f]['grossMarginMRQ']
        self.netProfitMarginTTM = json[symbol][f]['netProfitMarginTTM']
        self.netProfitMarginMRQ = json[symbol][f]['netProfitMarginMRQ']
        self.operatingMarginTTM = json[symbol][f]['operatingMarginTTM']
        self.operatingMarginMRQ = json[symbol][f]['operatingMarginMRQ']
        self.returnOnEquity = json[symbol][f]['returnOnEquity']
        self.returnOnAssets = json[symbol][f]['returnOnAssets']
        self.returnOnInvestment = json[symbol][f]['returnOnInvestment']
        self.interestCoverage = json[symbol][f]['interestCoverage']
        self.totalDebtToCapital = json[symbol][f]['totalDebtToCapital']
        self.ltDebtToEquity = json[symbol][f]['ltDebtToEquity']
        #self.totalDebtToEquity = jsont[symbol][f]['totalDebtToEquity']
        self.epsTTM = json[symbol][f]['epsTTM']
        self.epsChangePercentTTM = json[symbol][f]['epsChangePercentTTM']
        self.epsChangeYear = json[symbol][f]['epsChangeYear']
        self.epsChange = json[symbol][f]['epsChange']
        self.revChangeYear = json[symbol][f]['revChangeYear']
        self.revChangeTTM = json[symbol][f]['revChangeTTM']
        self.revChangeIn = json[symbol][f]['revChangeIn']
        self.sharesOutstanding = json[symbol][f]['sharesOutstanding']
        self.marketCapFloat =  json[symbol][f]['marketCapFloat']
        self.bookValuePerShare = json[symbol][f]['bookValuePerShare']
        self.shortIntToFloat = json[symbol][f]['shortIntToFloat']
        self.shortIntDayToCover = json[symbol][f]['shortIntDayToCover']
        self.vol1DayAvg = json[symbol][f]['vol1DayAvg']
        self.vol10DayAvg = json[symbol][f]['vol10DayAvg']
        self.vol3MonthAvg = json[symbol][f]['vol3MonthAvg']

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Class that takes the 'candles' key from tda-api and translates it into a dict to be converted 
# takes in list of indeterminate length
# each list item is a dict with keys: open: double, high: double, low: double, close: double, volume: int64, datetime: int64
# create pandas dataframe, rows are datetime vals, cols are open, high, low, close and volume
# Pseudocode:
"""
indices = []
for item in candles_list:
    append datetime
"""
class HistData:
	def __init__(self, symbol: str, cusip: str, candles_list: list):
		self.symbol = symbol
		self.cusip = cusip
		if isinstance(candles_list, list):
			self.hist_data = pd.DataFrame(candles_list)
			self.hist_data['datetime'] = pd.to_datetime(self.hist_data['datetime'], unit='ms') # Convert the 'datetime' column to a datetime object (assuming it's in Unix timestamp format)
			self.hist_data.set_index('datetime', inplace=True) # Set the 'datetime' column as the index
		else:
			print('candles are not in list format, exiting...')
			exit()
		
		
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Stock Objects Contain the Symbol, Instrument Obj, and historical data
# TODO:Add Positions Data for the Stock Later
class Stock:
	def __init__(self, symbol: str, cusip: str, c: Client, periods: str):
		self.symbol = symbol
		self.cusip = cusip
		instrument_data = f.get_instrument(c, symbol, 'fundamental')
		self.instruments = Instrument(symbol, instrument_data)
		hist_data_for_obj = f.get_stock_hist_data(c, symbol, periods)
		self.hist_data = HistData(symbol, cusip, hist_data_for_obj['candles'])
		print(self)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Portfolio: Portfolios contain a List of Stock Objects Representing the Positions the Account is holding, as well as a Balances Object containing available funds in the Account
class Portfolio:
	def __init__(self):
		pass
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Stock GUI Object: This Object is for Displaying a Quick Look at a Stock for a later GUI Implementation
# Taken from portfolio_viewing_script repo
"""
Key:
- symbol: stock ticker symbol
- pps: Price Per Share
- ns: Number of Shares
- tv: Total Value of Shares
- pp: Purchase Price of Shares
- pla: P/L Amount for the Day
- plp: P/L Percentage for the Day
- pl_vs_sp: P/L Percentage vs the S&P 500 Index
- pl_vs_n: P/L Percentage vs the NASDAQ Index
- pl_vs_dji: P/L Percentage vs the DOW Jones Industrial
"""
class Stock_GUI:
	def __init__(self, symbol, name, pps, ns, tv, pp, pla, plp, pl_vs_sp, pl_vs_n, pl_vs_dji):
		self.symbol = symbol
		self.pps = pps
		self.ns = ns 
		self.tv = tv 
		self.pp = pp 
		self.pla = pla 
		self.plp = plp
		self.pl_vs_sp = pl_vs_sp
		self.pl_vs_n = pl_vs_n
		self.pl_vs_dji = pl_vs_dji
		self.struct = self.build_dict()
	
	# Configure the Dictionary for Sorting the Stocks in the Main Program 
	def build_dict(self):
		struct = {
				'symbol':self.symbol,
				'vals':
					{ 'pps'       : self.pps,
					  'ns'        : self.ns,
					  'tv'        : self.tv,
					  'pp'        : self.pp,
					  'pla'       : self.pla,
					  'plp'       : self.plp,
					  'pl_vs_sp'  : self.pl_vs_sp,
					  'pl_vs_n'   : self.pl_vs_n,
					  'pl_vs_dji' : self.pl_vs_dji
					}
				}
		return struct
	
	# Public Getter to Access the Dictionary in the Main Program
	def get_dict(self):
		return self.struct
		
	def to_string(self):
		ret_string = ''
		
		ret_string += '\x1b[1;33m' + self.symbol
		ret_string += '\x1b[0;37m\nQuantity:\t' + '{:.0f}'.format(self.ns)
		ret_string += '\tCurrent Price:\t' + '{:.2f}'.format(float(self.pps))
		ret_string += '\nBought At:\t' + '{:.2f}'.format(float(self.pp))
		ret_string += '\tTotal Value:\t' + '{:.2f}'.format(float(self.tv))
		
		if self.pla > 0:
			ret_string += '\nP/L Amount:\t\x1b[0;32m' + '{:.2f}'.format(float(self.pla))
			ret_string += '\x1b[0;37m\tP/L Percent:\t\x1b[0;32m' + '{:.2f}'.format(float(self.plp)) + '%\x1b[0;37m'
			
		elif self.pla < 0:
			ret_string += '\nP/L Amount:\t\x1b[0;31m' + '{:.2f}'.format(float(self.pla))
			ret_string += '\x1b[0;37m\tP/L Percent:\t\x1b[0;31m' + '{:.2f}'.format(float(self.plp)) + '%\x1b[0;37m'
			
		else:
			ret_string += '\nP/L Amount:\t' + '{:.2f}'.format(float(self.pla))
			ret_string += '\tP/L Percent:\t' + '{:.2f}'.format(float(self.plp)) + '%\x1b[0;37m'
			
		return ret_string

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Stock Class Using Data from TDAmeritrade's Website, Not sure if I need this yet        
"""
class Stock:
    def __init__(self, symbol, prev_close, todays_open, days_range, avg_vol, last_time, last_size, percent_below_high, hist_volatility, mkt_cap, shares_outstanding, eps_ttm_gaap, pe_ratio_ttm_gaap, ann_div_yield, ex_div_pay_date, beta, percent_held_by_institutions, short_interest):
        self.symbol = symbol
        self.prev_close = prev_close
        self.todays_open = todays_open
        self.days_range = days_range
        self.avg_vol = avg_vol
        self.last_time = last_time
        self.last_size = last_size
        self.percent_below_high = percent_below_high
        self.hist_volatility = hist_volatility
        self.mkt_cap = mkt_cap
        self.shares_outstanding = shares_outstanding
        self.eps_ttm_gaap = eps_ttm_gaap
        self.pe_ratio_ttm_gaap = pe_ratio_ttm_gaap
        self.ann_div_yield = ann_div_yield
        self.ex_div_pay_rate = ex_div_pay_date
        self.beta = beta
        self.percent_held_by_institutions = percent_held_by_institutions
        self.short_interest = short_interest
"""