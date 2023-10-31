# This Class implements a Nested Dictionary to represent a stock
# 	- Each Dictionary follows this convention:
#		example_stock = {'symbol': self.symbol,
#						 'vals': {dict with all the info}}

# Key:
# - symbol: stock ticker symbol
# - pps: Price Per Share
# - ns: Number of Shares
# - tv: Total Value of Shares
# - pp: Purchase Price of Shares
# - pla: P/L Amount for the Day
# - plp: P/L Percentage for the Day
class Stock:
	def __init__(self, symbol, pps, ns, tv, pp, pla, plp):
		self.symbol = symbol
		self.pps = pps
		self.ns = ns 
		self.tv = tv 
		self.pp = pp 
		self.pla = pla 
		self.plp = plp
		self.struct = self.build_dict()
	
	# Configure the Dictionary for Sorting the Stocks in the Main Program 
	def build_dict(self):
		struct = {
				'symbol':self.symbol,
				'vals':
					{ 'pps' : self.pps,
					  'ns'  : self.ns,
					  'tv'  : self.tv,
					  'pp'  : self.pp,
					  'pla' : self.pla,
					  'plp' : self.plp
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
		
	
	# Private Getters for the individual Values of the Stocks
	def get_symbol(self): # Made Public for the sorting methods
		return self.symbol
	
	def __get_pps(self):
		return self.pps
	
	def __get_ns(self):
		return self.ns
		
	def __get_tv(self):
		return self.tv
	
	def __get_pp(self):
		return self.pp
	
	def __get_pla(self):
		return self.pla
	
	def __get_plp(self):
		return self.plp
	
	# Private Setters for the individual Values of the Stocks
	def __set_symbol(self, symbol):
		self.symbol = symbol
	
	def __set_pps(self, pps):
		self.pps = pps
	
	def __set_ns(self, ns):
		self.ns = ns
	
	def __set_tv(self, tv):
		self.tv = tv
	
	def __set_pp(self, pp):
		self.pp = pp
	
	def __set_pla(self, pla):
		self.pla = pla
	
	def __set_plp(self, plp):
		self.plp = plp
