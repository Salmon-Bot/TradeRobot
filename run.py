import time
import talib as ta
import numpy as np
import pandas as pd
import json
from strategy import trend
from exchangeapi.huobi import rest_api
from common.email import email_handler

if __name__ == "__main__":
    
    while(True):
        result = rest_api.get_kline('ethusdt',"1min",100)
        # print(result.get('data'))
        df = pd.DataFrame(result.get('data'), columns=['id', 'open', 'close', 'low', 'high', 'amount', 'vol', 'count']).sort_values(by = 'id',axis = 0,ascending = True)
        # print(df)

        ret = trend.MACross(df, 'close', 5, 10);
        print(ret)
        if ret :
            email_handler.send_mail("huobi 十五分钟均线交叉", "火币十五分钟均线交叉")
        time.sleep(10)