# Project Documentation 

#### (From Phind.com, 12/24/23)

## API Handler Structure

We discussed the creation of an `APIHandler` class to handle all interactions with the API. This class would handle fetching account data, positions, balances, historical stock data, and instrument data. However, if the `APIHandler` class becomes too large or complex, it could be broken down into smaller classes such as `Portfolio`, `Positions`, and `Instruments`.

## Regression Modeling and Visualization

For regression modeling and creating visualizations, we suggested creating a `RegressionModeler` class for handling all regression modeling tasks and a `Visualizer` class for handling all visualization tasks. The `RegressionModeler` class would use sklearn for regression modeling, while the `Visualizer` class would use MPLFinance for creating plots.

## SQL Database Structure for Tableau

When preparing the SQL database for use with Tableau, we recommended normalizing the data, using appropriate data types, including a unique identifier for each row, structuring the data in a way that supports analysis, ensuring consistency, and using a star schema.
