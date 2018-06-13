import numpy as np
import pandas as pd

import talib as ta
from pandas.io.json import json_normalize  
import json  
import time  


# 使用talib库作为基础的指标库,只用获取对应的数据即可
def maCross(data, shortPeriod, longPeriod):
    '''
    ma cross 均线交叉
    '''
    talib.EMA()