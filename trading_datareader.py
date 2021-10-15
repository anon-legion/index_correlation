# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 11:35:15 2021

@author: =GV=
"""
import datetime as dt
import matplotlib.pyplot as plt
import pandas_datareader as web
import seaborn as sns


base_currency = 'USD'
metric = 'Close'
start = dt.datetime(2018, 1, 1)
end = dt.datetime.now()

tickers = ['BTC', 'ETH']
indeces =  ['^GSPC', '^IXIC', '^DJI', 'DX-Y.NYB', '^TNX']
col_names = []

first = True

for index in indeces:
    data = web.DataReader(f'{index}', 'yahoo', start, end)
    if first:
        combined = data[[metric]].copy()
        col_names.append(index)
        combined.columns = col_names
        first = False
    else:
        combined = combined.join(data[metric])
        col_names.append(index)
        combined.columns = col_names
        
for ticker in tickers:
    data = web.DataReader(f'{ticker}-{base_currency}', 'yahoo', start, end)
    combined = combined.join(data[metric])
    col_names.append(ticker)
    combined.columns = col_names
        

# plt.yscale('log')

# for  index in indeces:
#     plt.plot(combined[index], label=index)

# for ticker in tickers:
#     plt.plot(combined[ticker], label=ticker)
    
# plt.legend(loc='upper right')

combined = combined.pct_change().corr(method='pearson')
sns.heatmap(combined, annot=True, cmap='coolwarm')
plt.show()

