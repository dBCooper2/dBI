# Contents
This folder contains an update to my previous project, https://github.com/dBCooper2/portfolio_viewing_script

This project made calls to the TDAmeritrade API using the tda-api wrapper

These functions are out of date and will no longer work on my machine, so I will be rewriting them in ver2 in anticipation of the schwab API releasing, these are just references that will be trimmed in later pushes

# TODOs:
- Write Class Files for Stock, Instrument and Position to reflect API response jsons
- Write Functions to convert either the classes or the jsons into a Pandas Dataframe for...
    - Instruments
    - Positions
    - Stock Object(Name, Symbol, Historical Data, ID's to Instruments and Positions Object)
- Write functions to export data into CSV's, Excel Files
- Some Form of Database Connection