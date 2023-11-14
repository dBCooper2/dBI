# Notes for Ceagan:

The Schema.sql file is just a template I had ChatGPT generate for me, I do plan on creating a functional db once I have finished the DS 3860 Project

The current Model is:
- Tables: Users, Portfolio, Positions, Instruments, Price Histories, Experiments
- Users is the user account, containing an API key, redirect uri, account number and token path(this logs the user in automatically when main.py is run)
- Portfolio is a Collection Object that contains Positions that the User is holding and the related Price Histories and Instruments
- Instruments are a Collection of fundamental data about a stock/position
- Price Histories are a Collection of Historical Data Points(price @ open, close, high/low for a predetermined amount of periods)
- Positions contain data like Profit/Loss Percentages for Stocks the user is already holding
- Each one of these is a dataframe that will be inserted into the database(I am still learning how to do this properly)

### - Relationships: 
- Users:Portfolio is 1:1
- Portfolio:Positions is 1:M
- Portfolio:Instrument is 1:M
- Portfolio: Price History is 1:M