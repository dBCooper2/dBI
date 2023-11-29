# dBI - Business Intelligence Tools for tda-api and TDAmeritrade Developer Accounts

### Note: This Project is NOT FINISHED
The project is just a collection of functions and classes for now. This will be deleted and a release will be created when the project is finished.

## About
I started this project to apply the skills I have learned while studying at TTU to a real-life project. The goal of the dBI repository is to take API data from TD Ameritrade using Alex Golec's tda-api wrapper and my own python code to analyze the data using Python, and export it into several formats. When I started this project I had little experience with Pandas, Tableau and using Python with Excel, so this project will integrate all three of these technologies into the project. dBI will be able to...
- Access TD Ameritrade's API to view portfolio performance
- Compute expected returns for a stock using moving averages and regression
- Calculate portfolio performance using CAPM and other methods that are to be determined to improve the portfolio's performance.
- Visualize current and projected stock/portfolio performance through Python Libraries and Tableau
- Be callable via Tableau to generate data for dashboards
- Stash Excel/CSV/Pickle Files in a Database, and eventually store the raw values(I am currently doing a database project in school to learn this)

### Completed Features:
- The Program creates a Portfolio Object based on either a TD Ameritrade API Client Object via tda-api or a provided dictionary(And CSV/pkl files in the future). This Portfolio is represented by the Abstract Base Class AbstractPortfolio, which is extended by TD_Portfolio for handling the TD Account's Portfolio, and Test_Portfolio to handle test dictionaries and portfolios from CSV/pkl files.
- Portfolios contain individual DataFrames of the Positions in an account and their relevant data, along with an Instrument DataFrame, which contains fundamental data like the beta of each position and ratios like the PE ratio. Both of these DataFrames use the Stock's symbol as an index and the data points are columns. Lastly, Portfolios contain a DataFrame of Historical Data of each stock, using an index of the date the data was recorded in the TD API with each Stock's open, close, high and low price along with the volume of shares traded. These are labeled {symbol}_open/close/etc., with each being a separate column.
- Portfolios can perform a CAPM Analysis of the Portfolio. This entails calling a stock symbol to represent the bond market for the risk-free rate, and a symbol that tracks the S&P 500 for the market rate. Then, the Portfolio accesses each Beta from the Instruments DataFrame and the quantity of each stock in the Positions DataFrame(represented by 'longQuantity') and computes a weighted average of the Betas to create a Portfolio Beta. Then the Portfolio calculates a 1-day moving average of the stock's historical data to compute an expected return. Finally, these values are added to their own DataFrame and calculate the required rate of return using the CAPM Formula(Required Rate of Return = Risk-Free Rate + Beta * (Market Rate - Risk-Free Rate)), then these values are compared to the expected returns to see if the expected return is greater than the required return
- Portfolios can be exported to both CSV and Pickle(pkl) files provided an output path to save the files to.

### In Progress:
- The program will contain a GUI element for users forking the file that will contain instructions and steps to create a TD Developer account and the information required for the program to run. This is a contribution by @slizzed(https://github.com/slizzed) to improve his python skills.
- The CAPM function is a little crude right now and will be improved. A second capital asset pricing model will be created to use the formula:
(r_it - r_ft) = a_i + B_i * (r_mt - r_ft) + e_it
to better model r_it, the return of the asset.

### Planned:
- Result Data from Time Series Analysis will be graphed using MatplotLib
- Linear Optimization will be added to Portfolios to maximize a given data point(maximize dividend, maximize expected return, minimize portfolio beta, etc.)


## Installation and Running the Program
TODO

## How to Use
TODO

## Credits:
None of this would be possible without Alex Golec(https://github.com/alexgolec) and the team behind the tda-api. You can find the project here: https://github.com/alexgolec/tda-api and at https://tda-api.readthedocs.io

