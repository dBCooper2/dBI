-- Accounts Table
CREATE TABLE Accounts (
    api_key VARCHAR(255),
    redirect_uri VARCHAR(255),
    account_number INT,
    token_path VARCHAR(255),
    PRIMARY KEY (api_key, redirect_uri, account_number, token_path)
);

-- Portfolios Table
CREATE TABLE Portfolios (
    portfolio_id INT PRIMARY KEY,
    account_api_key VARCHAR(255),
    account_redirect_uri VARCHAR(255),
    account_number INT,
    account_token_path VARCHAR(255),
    FOREIGN KEY (account_api_key, account_redirect_uri, account_number, account_token_path)
        REFERENCES Accounts(api_key, redirect_uri, account_number, token_path)
);

-- Instruments Table
CREATE TABLE Instruments (
    instrument_id INT PRIMARY KEY,
    instrument_name VARCHAR(255),
    symbol VARCHAR(10),
    asset_type VARCHAR(20),
    high_52 DECIMAL(10, 2),
    low_52 DECIMAL(10, 2),
    dividend_amount DECIMAL(10, 2),
    dividend_yield DECIMAL(5, 2),
    dividend_date DATE,
    pe_ratio DECIMAL(10, 4),
    peg_ratio DECIMAL(10, 2),
    pb_ratio DECIMAL(10, 4),
    pr_ratio DECIMAL(10, 5),
    pcf_ratio DECIMAL(10, 5),
    gross_margin_ttm DECIMAL(10, 5),
    gross_margin_mrq DECIMAL(10, 5),
    net_profit_margin_ttm DECIMAL(10, 5),
    net_profit_margin_mrq DECIMAL(10, 5),
    operating_margin_ttm DECIMAL(10, 5),
    operating_margin_mrq DECIMAL(10, 5),
    return_on_equity DECIMAL(10, 5),
    return_on_assets DECIMAL(10, 5),
    return_on_investment DECIMAL(10, 3),
    quick_ratio DECIMAL(10, 5),
    current_ratio DECIMAL(10, 5),
    interest_coverage DECIMAL(10, 5),
    total_debt_to_capital DECIMAL(10, 5),
    lt_debt_to_equity DECIMAL(10, 5),
    total_debt_to_equity DECIMAL(10, 5),
    eps_ttm DECIMAL(10, 5),
    eps_change_percent_ttm DECIMAL(10, 2),
    eps_change_year DECIMAL(10, 3),
    eps_change DECIMAL(10, 2),
    rev_change_year DECIMAL(10, 2),
    rev_change_ttm DECIMAL(10, 2),
    rev_change_in DECIMAL(10, 5),
    shares_outstanding DECIMAL(20, 2),
    market_cap_float DECIMAL(10, 3),
    market_cap DECIMAL(20, 2),
    book_value_per_share DECIMAL(10, 4),
    short_int_to_float DECIMAL(5, 2),
    short_int_day_to_cover DECIMAL(5, 2),
    div_growth_rate_3_year DECIMAL(5, 2),
    dividend_pay_amount DECIMAL(10, 2),
    dividend_pay_date DATE,
    beta DECIMAL(10, 5),
    vol_1_day_avg DECIMAL(20, 2),
    vol_10_day_avg DECIMAL(20, 2),
    vol_3_month_avg DECIMAL(20, 2)
);


-- Positions Table
CREATE TABLE Positions (
    position_id INT PRIMARY KEY,
    portfolio_id INT,
    instrument_id INT,
    symbol VARCHAR(10),
    asset_type VARCHAR(20),
    quantity INT,
    short_quantity DECIMAL(10, 2),
    average_price DECIMAL(10, 2),
    current_day_cost DECIMAL(10, 2),
    current_day_profit_loss DECIMAL(10, 2),
    current_day_profit_loss_percentage DECIMAL(5, 2),
    long_quantity DECIMAL(10, 2),
    settled_long_quantity DECIMAL(10, 2),
    settled_short_quantity DECIMAL(10, 2),
    previous_session_long_quantity DECIMAL(10, 2),
    FOREIGN KEY (portfolio_id) REFERENCES Portfolios(portfolio_id),
    FOREIGN KEY (instrument_id) REFERENCES Instruments(instrument_id)
);


-- Price History Table
CREATE TABLE PriceHistory (
    price_id INT PRIMARY KEY,
    instrument_id INT,
    portfolio_id INT,
    position_id INT,
    symbol VARCHAR(10),
    price_date TIMESTAMP,
    open_price DECIMAL(10, 2),
    high_price DECIMAL(10, 2),
    low_price DECIMAL(10, 2),
    close_price DECIMAL(10, 2),
    volume INT,
    datetime BIGINT,  -- Unix timestamp in milliseconds
    FOREIGN KEY (instrument_id) REFERENCES Instruments(instrument_id),
    FOREIGN KEY (portfolio_id) REFERENCES Portfolios(portfolio_id),
    FOREIGN KEY (position_id) REFERENCES Positions(position_id)
);
