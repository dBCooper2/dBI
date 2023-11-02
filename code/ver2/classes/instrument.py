#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Instruments contain the ratio's required for Data Analysis
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