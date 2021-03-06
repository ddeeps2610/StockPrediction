#!/usr/bin/python

import os, sys
import pandas as pd
import matplotlib.pyplot as plt


import mathUtil
import dataUtil
import models


def testRun(stocks):
    # Slice the data for the required duration
    data = dataUtil.sliceData(stocks, '2017-07-01', '2017-09-01')
  
    # Plot Normalized
    dataUtil.plotStocks(data)
    dataUtil.plotStocks(dataUtil.normalize(data), title="Normalized stock prices", yLabel="Normalized price")
 
    rMean_SPY = mathUtil.getRollingMean(data['SPY'], window=20)
    rStd_SPY = mathUtil.getRollingStd(data['SPY'], window=20)
    upperBand, lowerBand = mathUtil.getBollingerBands(rMean_SPY, rStd_SPY)
  
    #plot
    ax = data['SPY'].plot(title='Bollinger Bands', label='SPY')
    rMean_SPY.plot(label='Rolling mean', ax=ax)
    upperBand.plot(label='upper band', ax=ax)
    lowerBand.plot(label='lower band', ax=ax)

    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend(loc='upper left')
    plt.show()
  

def runPlotBollinger(stocks):
    models.plotBollinger(stocks['SPY'], window=20)
    
def testDailyReturns(stocks):
    dailyReturns = mathUtil.computeDailyReturns(stocks) 
    dataUtil.plotStocks(dailyReturns, title='Daily Returns')

def testCumulativeReturns(stocks):
    cumReturns = mathUtil.computeCumulativeReturns(stocks)
    dataUtil.plotStocks(cumReturns, title='Cumulative Returns')

if __name__ == '__main__':
    startDate = '2015-01-01'
    endDate = '2017-09-01'
    dates = pd.date_range(startDate, endDate)
    symbols = ['HCP', 'SPY', 'GOOG', 'FB', 'AAPL', 'GBTC', 'TSLA']
    stocks = dataUtil.getData(symbols, dates)

    #testRun(stocks)
    runPlotBollinger(stocks)
    testDailyReturns(stocks)
    testCumulativeReturns(stocks) 
