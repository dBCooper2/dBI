# dBI - Business Intelligence Tools for tda-api and TDAmeritrade Developer Accounts

### Note: This Project is NOT FINISHED
The project is just a collection of functions and classes for now. This will be deleted and a release will be created when the project is finished.

### Completed Features:
- The program can access the TDAmeritrade API, and collects an Account from the API or from User Input. This is then used to create a Portfolio object, capturing the positions in the portfolio and their related performance data, as well as Historical Price data from a list of periods specified by the user, and Fundamental data like Betas, Dividend Yields and related ratios.
- The program can export the data into either an Excel Workbook with Positions Data, Instrument Data, and each Historical Data Table as separate, labeled worksheets, as well as a folder of CSV or Pickle files
- The Program can perform CAPM analysis on a Portfolio of Stocks, calculating the Expected Return of the entire portfolio, the Risk-Free Rate(For now I am using symbol BIV for bonds), and the Market Rate(For now I am using symbol SPY), and then calculates a Beta for the model for that day.

### In Progress:
- The program will need a persistent database to export the files into other software smoothly, check out the 'db' branch for the progress on that.
- The program will contain a GUI element for users forking the file that will contain instructions and steps to create a TD Developer account and the information required for the program to run. This is a contribution by @slizzed(https://github.com/slizzed) to improve his python skills.

### Planned:
- The program will calculate a moving average, linear regression and an exponential smoothing model on the Historical Data to determine the expected returns of each stock.
- These moving averages will be combined with any other necessary data to perform Portfolio Analysis on a Portfolio either pulled from a TDA Account or added via User Input
- Linear Optimization will be added to Portfolios to maximize a given data point(maximize dividend, maximize expected return, minimize portfolio beta, etc.)
- These graphs will be plotted either through a tableau dashboard or a built-in Python plotting Library.

## About
I started this project to apply the skills I have learned while studying at TTU to a real-life project. The goal of the dBI repository is to take API data from TD Ameritrade using Alex Golec's tda-api wrapper and my own python code to analyze the data using Python, and export it into several formats. When I started this project I had little experience with Pandas, Tableau and using Python with Excel, so this project will integrate all three of these technologies into the project. dBI will be able to...
- Take historical data of a stock and compute expected returns using Linear Regression, Moving Averages and Exponential Smoothing
- Perform Portfolio Analysis on a TD Ameritrade customer's portfolio to Calculate the Expected Return of the portfolio
- Perform Analysis on Individual Stocks or on a customer portfolio by accessing Historical Price and Instrument Data.
- Export the Data collected from the TD Ameritrade API and processed by the program into CSV and Excel Workbook Formats(And possibly SQL or SQLite in the Future)
- Export the data into Tableau to find insights and present the data visually

## Installation and Running the Program
This will be added in the future, if this repo gets attention I will write a guide to set up the project and run it right now, but currently it is not available as an executable. When the project is finished I will make it a downloadable and executable program.

## How to Use

## Credits:
None of this would be possible without Alex Golec(https://github.com/alexgolec) and the team behind the tda-api. You can find the project here: https://github.com/alexgolec/tda-api and at https://tda-api.readthedocs.io

