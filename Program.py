from turtle import title
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
from pandas_datareader import data as web
import pandas as pd
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
plt.show()

dailyReturns = df.pct_change()
dailyReturns
