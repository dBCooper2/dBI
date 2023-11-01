class Position:
    def __init__(self, symbol, qty, price, chg, cost, mkt_value, gain):
        self.symbol = symbol
        self.qty = qty
        self.price = price
        self.chg = chg
        self.cost = cost
        self.mkt_value = mkt_value
        self.gain = gain

class Stock:
    def __init__(self, prev_close, todays_open, days_range, avg_vol, last_time, last_size, percent_below_high, hist_volatility, mkt_cap, shares_outstanding, eps_ttm_gaap, pe_ratio_ttm_gaap, ann_div_yield, ex_div_pay_date, beta, percent_held_by_institutions, short_interest):
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