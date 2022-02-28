from bdb import effective
from turtle import title
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
from pandas_datareader import data as web
import pandas as pd
from pypfopt import risk_models
from pypfopt import expected_returns
from pypfopt import discrete_allocation
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices

plt.style.use('fivethirtyeight')

portfolio = ['BABA', 'FB', 'GEVO']
weight = np.array([0.2, 0.2, 0.2])
firstInvestment = '2022-01-01'
today = datetime.today().strftime('%Y-%m-%d')


df = pd.DataFrame()

for stock in portfolio:
    pd[stock] = web.DataReader(
        stock, data_source='yahoo', start=firstInvestment, end=today)['Adj Close']

df

portfTitle = 'Portfolio Adj. Closing Prices'

theStocks = df
for i in theStocks.column.values:
    plt.plot(theStocks[i], label=i)

plt.title(title)
plt.xlabel('date', fontsize=12)
plt.ylabel('Adj price', fontsize=12)

plt.legend(theStocks.columns.values, loc='upper left')

dailyReturns = df.pct_change()


# covariance matrix

annual_cov_matrix = dailyReturns.cov()*252

# variance of portfolio
portfolio_var = np.dot(weight.T, np.dot(annual_cov_matrix, weight))


# volatility/stdv
portfolio_volatility = np.sqrt(portfolio_var)

# annual portfolio return

portfolioAnnualReturns = np.sum(dailyReturns.mean()*weight)*252

# annual return, risk and variance
percent_var = str(round(portfolio_var, 2)*100)+"%"
percent_volatility = str(round(portfolio_volatility, 2)*100)+"%"
percent_return = str(round(portfolioAnnualReturns, 2)*100)+"%"
print("Portfolio variance"+percent_var)
print("Portfolio volatility"+percent_volatility)
print("Portfolio return" + percent_return)

m = expected_returns.mean_historical_return(df)

S = risk_models.sample_cov(df)

# optimize max sharp rt

efficiant = EfficientFrontier(m, S)

weight = efficiant.max_sharpe()

cleaned_wight = efficiant.clean_weights()

print(cleaned_wight)

efficiant.portfolio_performance(verbose=True)

latest_price = get_latest_prices(df)

weight = cleaned_wight

da = discrete_allocation(weight, latest_price, total_portfolio_value=100000)

allocate, leftOver = da.lp_portfolio()
