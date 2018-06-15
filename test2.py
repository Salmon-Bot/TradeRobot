from exchangeapi.huobi import rest_api
import talib as ta
import numpy as np
import pandas as pd
import json

if __name__ == "__main__":
    #websocket.start()
    print(rest_api.get_kline('ethusdt',"1min",10))
    
    result = rest_api.get_kline('ethusdt',"1min",50)
    
    print(result.get('data'))

    df = pd.DataFrame(result.get('data'), columns=['id', 'open', 'close', 'low', 'high', 'amount', 'vol', 'count'])
    print(df)
    dm = df.sort_values(by = 'id',axis = 0,ascending = True)
    
    print(dm)


    #print(ta.EMA(df['close'],5))
    dm['ema10']= ta.EMA(dm['close'],10)
    dm['sma10']= ta.SMA(dm['close'],10)
    print(dm)