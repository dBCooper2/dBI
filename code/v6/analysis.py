import pandas as pd
import functions as f

def moving_avg(df: pd.DataFrame, symbol: str, periods: int)->int: # perform a moving average on a price history, key is the key is the column to run a moving avg on and periods is the # of periods
    return df[symbol].rolling(periods).mean()

def exp_smoothing(df: pd.DataFrame, damp: float)->int: # perform exponential smoothing on a dataframe, with damp as a float
    return -1

def wa(p_df: pd.DataFrame, i_df: pd.DataFrame, p_col: str, i_col: str)->float: #pass in a position and instrument df, then find the weighted average of either the betas or the expected returns(using param to indicate column)
    weights = p_df[p_col].to_list()
    val_to_avg = i_df[i_col].to_list()

    if len(weights) == len(val_to_avg):
        for w in weights:
            print(w)

    pass

# Pass in a dataframe of stock items, quantity 0 -- Look at DS 3620 Slides and Labs!
def min_beta(df: pd.DataFrame): # Perform Integer Optimization on a List of stocks that keeps 
    # Integer Optimization: You can't purchase Portions of a Stock
    pass