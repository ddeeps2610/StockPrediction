#!/usr/bin/python

import os, sys

import matplotlib.pyplot as plt
import mathUtil
import dataUtil


def plotBollinger(df, window=20):
    rMean = mathUtil.getRollingMean(df, window=window)
    rStd = mathUtil.getRollingStd(df, window=window)
    upperBand, lowerBand = mathUtil.getBollingerBands(rMean, rStd)

    #print rMean, rStd
    #print upperBand, lowerBand

    ax = df.plot(title='Bollinger Bands')
    rMean.plot(label='Rolling Mean', ax=ax)
    upperBand.plot(label='Upper band', ax=ax)
    lowerBand.plot(label='Lower band', ax=ax)
    
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend(loc='upper left')
    plt.show()
