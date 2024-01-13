create table Portfolios(
    p_id char(10) primary key not null,
    acct_data_path char(100),
    token_path char(100)
);

create table Symbols(
    symbol_id char(10) primary key not null,
    portfolio_id char(10),
    symbol char(10)
    positions_pkl blob, -- Position Data for the symbol stored as a PKL file
    instruments_pkl blob, -- Instrument Data for the symbol stored as a PKL file
    foreign key (portfolio_id) references Portfolios(p_id)
);

create table CandleData(
    ph_id char(10) not null,
    s_id char(10) not null,
    periods char(3) not null,
    symbol char(10),
    datetime_unix float,
    candles_open float(10,10),
    candles_close float(10,10),
    candles_high float(10,10),
    candles_low float(10,10),
    candles_volume float(10,10),
    primary key (ph_id, s_id, periods),
    foreign key (s_id) references Symbols(symbol_id)
);

