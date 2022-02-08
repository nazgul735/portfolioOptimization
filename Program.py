import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import pandas_datareader as pdr
pdr.get_data_fred('GS10')
plt.style.use('fivethirtyeight')

portfolio = ['BABA', 'FB', 'GEVO']
weight = np.arrawy([0.2, 0.2, 0.2])
firstInvestment = '2022-01-01'
today = datetime.today().strftime('%Y-%m-d%')


df = pd.DataFrame()

for stock in portfolio:
    pd[stock] = web.DataReader(
        stock, data_source='yahoo', start=firstInvestment, end=today)['Adj Close']

df
