# dBI - Version 7

- Intended to be imported as a python package for assisting in data analysis

Redo this part later:
- Tracks stocks in the user's portfolio as well as in a watchlist
- Stores Position and Instrument Data for each Equity in an SQLite Database for tracking historical data over time
- Historical Price Data(candles) are pulled from the API when needed, but not stored locally
- Additional Functionality includes: Visualizations for Candle Charts using MPLFinance, CAPM calculations using regression via sklearn

## Deliverables

### Objects

- **APIHandler**

    The APIHandler Class is in charge of all API Calls. It contains functions to get the positions, balances and watchlists from a TD Account, as well as the ability to retrieve fundamental data on equities, along with candle data for charts and data analysis.

- **DataProcessor**

- **DatabaseManager**

- **Visualizer**

- **RegressionModeler**

### Tools
