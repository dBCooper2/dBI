# TODO: Refactor v5 into dataclass objects to clean up your code
## db, tableau and external sources that connect to the program should be stored in a separate package

# Classes should only contain the attrs, no api calls from within
# Excel Files are named 'portfolio-MM-DD-YYYY

# Do I need classes?
- Do everything in DataFrames and Portfolio, skip nested Position, Instrument and Price History Classes
- Pickle Everything that stays inside of Python
- CAPM is just a regression model, calculate r_i with the historical data, r_rf call down a T-Bill Symbol, r_m call down an exchange value and Beta is the independent variable
- US10Y, US5Y and US1Y are the symbols for r_rf, use SPY for r_m
####    - UPDATE: Use BIV for now instead of Bonds
- tda-api discord used Yahoo in the past so circle back on this

# DONE: 
- Slice DataFrames into just 1 data point from the Price History
- Calculate Expected Returns for each equity
- Calculate a Weighted Average of these Returns to merge all the positions together
    - Weighted Average is done by multiplying the expected returns by the Number of Shares, then Summing them and dividing by the total number of shares
- Find a library to run regression on the result r_m, r_rf, and r_i DataFrame
    - Result DataFrame is Created
    - I have access to a DataFrame of r_i, r_rf, r_m-r_rf, and calculated betas
        - Redo to create a list of betas from a regression model

# TODOs:
- Graphing the Results
- Calculate Betas using Regression instead of the CAPM Formula
- Graph those results
- 

