# Import as: "import analysis_functions as af"
import pandas as pd
import datetime as dt


def moving_avg(data: pd.DataFrame, periods: int): # periods is how far back you want the Moving Average to go
    # find a moving average for each column in the DF
    # sort DF by datetime
    data = data.sort_values(by='datetime')

    data['open_moving_avg'] = data['open'].rolling(window=periods).mean()
    data['close_moving_avg'] = data['close'].rolling(window=periods).mean()
    data['high_moving_avg'] = data['high'].rolling(window=periods).mean()
    data['low_moving_avg'] = data['low'].rolling(window=periods).mean()

    data.dropna() # Clear all NaN values
    
    return data

def exp_smoothing(data: pd.DataFrame, alpha: float):
    
    # sort df by datetime
    data = data.sort_values(by='datetime')

    # perform the smoothing
    data['open_ewm'] = data['open'].ewm(alpha=alpha, adjust=False).mean()
    data['close_ewm'] = data['close'].ewm(alpha=alpha, adjust=False).mean()
    data['high_ewm'] = data['high'].ewm(alpha=alpha, adjust=False).mean()
    data['low_ewm'] = data['low'].ewm(alpha=alpha, adjust=False).mean()

    return data

def linear_regression(data: pd.DataFrame): 
    pass