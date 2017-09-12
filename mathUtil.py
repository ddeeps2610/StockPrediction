#!/usr/bin/python
import pandas as pd


def getRollingMean(data, window):
    return data.rolling(window=window, center=False).mean()

def getRollingStd(data, window):
    return data.rolling(window=window, center=False).std()

def getBollingerBands(rMean, rStd):
    upperBand = rMean + rStd * 2
    lowerBand = rMean - rStd * 2
    return upperBand, lowerBand

def getBands(alpha, rMean, rStd):
    upperBand = rMean + rStd * alpha
    lowerBand = rMean - rStd * alpha
    return upperBand, lowerBand

def computeDailyReturns(df):
    dailyReturns = (df/ df.shift(1)) - 1
    dailyReturns.ix[0, :] = 0
    return dailyReturns

def computeCumulativeReturns(df):
    return (df/df[0]) - 1
