#!/bin/env/python

import os, sys
import pandas as pd
import matplotlib.pyplot as plt


def readAllStocks(startDate="2017-01-01", endDate="2017-09-01"):
  """
  Returns all stocks in the pandas.
  """
  dataPath = "./data/"
  if (not os.path.exists(dataPath)):
    print "Path './data/' does not exist."
    return None

  # Data path exists. Proceed further.
  # Read all files in a pandas dataframe and return
  dates = pd.date_range(startDate, endDate)
  df = pd.DataFrame(index=dates)  
  
  # read Google stock
  symbols = ['GOOG', 'FB', 'AAPL', 'GBTC', 'TSLA']
  for symbol in symbols:
    dfStock = pd.read_csv("data/{}.csv".format(symbol), index_col="Date", parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
    dfStock.dropna()
    dfStock = dfStock.rename(columns={'Adj Close':symbol})
    df = df.join(dfStock, how='inner')
  return df


def plotStocks(df,title="Stock Prices", xLabel='Date', yLabel='Price'):
  plot = df.plot(title=title)
  plot.set_xlabel(xLabel)
  plot.set_ylabel(yLabel)
  plt.show()

def sliceData(df, startDate, endDate, columns=[]):
  if columns:
    return df.ix[startDate:endDate,columns]
  else:
    return df.ix[startDate:endDate]

def normalize(df):
  return df/df.ix[0]

###############################################################################
#                                     MAIN                                    #
###############################################################################
if __name__ == '__main__':
  stocks = readAllStocks()
  #if (not stocks.empty):
  #  print stocks.tail(15)
  
  # Plot latest data
  data = sliceData(stocks, '2017-07-01', '2017-09-01')
  
  # Plot Normalized
  plotStocks(data)
  plotStocks(normalize(data), title="Normalized stock prices", yLabel="Normalized price")
