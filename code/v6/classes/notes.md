# Data needed for Instruments to perform CAPM:

### r_avg = SUM(r_i)/N
- r_avg: average(expected) return rate
- r_i: expected return at index i
- N: # of terms(indices)

### rho = root(sum(r_i-r_avg)^2/N-1)
- rho: standard deviation

### CV = rho/r_avg

### Weighted Average of...
- Expected/Average Return
- Beta

### r_i = r_rf+B*(r_m-r_rf)
- r_i: required return
- r_rf: risk-free rate of return
- B: Beta(weighted avg of portfolio betas)
- r_m: return % on the market

- create rm - rf in 

## V6 Current Functionality:
- Pulling API Data
- calculating a moving average of each column in the price history

## CAPM is REGRESSION
return - rrf = 

store flat files in the database without transferring values

graph betas at different periods as a time series