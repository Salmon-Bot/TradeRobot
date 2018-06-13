from exchangeapi.huobi import rest_api
import talib as ta
import numpy as np
import pandas as pd
import json

if __name__ == "__main__":
    #websocket.start()
    print(rest_api.get_kline('ethusdt',"1min",10))
    
    result = rest_api.get_kline('ethusdt',"1min",10)
    
    print(result.get('data'))
    df = pd.DataFrame(list(result.get('data')))
    print(df)