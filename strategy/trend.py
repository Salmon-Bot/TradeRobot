import numpy as np
import pandas as pd

import talib as ta
from pandas.io.json import json_normalize  
import json  
import time  


# 使用talib库作为基础的指标库,只用获取对应的数据即可
def SMA(df, period=5, type='close'):
    '''均线
    '''

    # df = df.sort_values(by = 'id',axis = 0,ascending = True)
    df['ma']= ta.SMA(df[type],period)
    return df

def MACross(df, type='close', shortPeriod=5, longPeriod=20):
    '''均线交叉
    '''
    df['short'] = ta.SMA(df[type],shortPeriod)
    df['long'] = ta.SMA(df[type],longPeriod)
    shortMA = df['short']
    longMA = df['long']
    #print(df)
    if len(df) <= 2 :
        return '数据不足'
    if shortMA[0] > longMA[0] and shortMA[1] < longMA[1] :
        return '向上穿越';
    elif shortMA[0] < longMA[0] and shortMA[1] > longMA[1] :
        return '向下穿越'
    return '非穿越'
