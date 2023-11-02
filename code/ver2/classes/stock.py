#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Library Imports
from tda.client import Client
import functions as f

# Intra-Project Imports
import instrument as Instrument
import hist_data as HistData
import position as Position
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Stock Objects Contain the Symbol, Instrument Obj, and historical data
# TODO:Build Struct to output the data in a cleaner way
class Stock:
	def __init__(self, symbol: str, cusip: str, c: Client, periods: str, p: Position):
		self.symbol = symbol
		self.cusip = cusip
		self.position_data = vars(p)
		self.position_data.__delattr__['symbol']
		self.position_data.__delattr__['cusip']
		
		instrument_data = f.get_instrument(c, symbol, 'fundamental')
		self.instruments = Instrument(symbol, instrument_data)
		hist_data_for_obj = f.get_stock_hist_data(c, symbol, periods)
		self.hist_data = HistData(symbol, cusip, hist_data_for_obj['candles'])
		print(self)
		
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Stock_nb Objects Contain the Symbol, CUSIP but contain no position data that reveals cash amounts(so just P/L %s)
class Stock_nb:
	def __init__(self, symbol: str, cusip: str, p: Position):
		self.symbol = symbol
		self.cusip = cusip
		self.position_data = p.currentDayProfitLossPercentage
		print(self)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Addt'l Stock Classes, not sure if I need to implement these yet
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