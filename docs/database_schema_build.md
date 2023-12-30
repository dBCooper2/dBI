# Entities

(taken from <https://quant.stackexchange.com/questions/61699/how-to-structure-a-stock-market-data-database>)

- Company: Companies are the corporate entity, NOT THE STOCK
- Instrument: This is the stock, uniquely identified by its CUSIP, branch other stock tables off this one later
- Vendor: Party Responsible for getting the data to me(TDAmeritrade, Schwab, Yfinance, ...)
- 