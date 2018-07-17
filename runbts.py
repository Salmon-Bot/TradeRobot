import time
import threading
import talib as ta
import numpy as np
import pandas as pd
import json
from strategy import trend
from exchangeapi.huobi import rest_api
from common.email import email_handler

class huobiThread (threading.Thread):
    def __init__(self, threadID, symbol,period,lines,shortPeriod,longPeriod,delay=600):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.symbol = symbol
        self.period = period
        self.lines = lines
        self.shortPeriod = shortPeriod
        self.longPeriod = longPeriod
        self.delay = delay

    def run(self):
        print ("开始线程：" + self.threadID)
        monitor(self.symbol,self.period,self.lines,self.shortPeriod,self.longPeriod,self.delay)
        print ("退出线程：" + self.threadID)


def monitor(symbol,period,lines,shortPeriod,longPeriod,delay=600):
    # 作为多线程的执行方法，对选定的交易对按照一定的周期进行监控，并且邮件通知,
    # 因为火币对频繁调用有一定的限制所以不能一直的去读取
    flag = 0; # 1 向上穿越 2下穿越，0 初始value
    while(True):
        # 检测 btsusdt 交易对，用来为比特股账户的操作提供依据
        result = rest_api.get_kline(symbol,period,lines)
        # print(result.get('data'))
        if result is None:
            continue

        df = pd.DataFrame(result.get('data'), columns=['id', 'open', 'close', 'low', 'high', 'amount', 'vol', 'count']).sort_values(by = 'id',axis = 0,ascending = True)
       
        ret = trend.MACross(df, 'close', shortPeriod, longPeriod); 
        str = ""
        if ret == '向上穿越' and flag != 1:
            str="火币交易对:"+symbol+", 周期:"+period+" 向上穿越"
            flag = 1
            
        elif ret == '向下穿越' and flag !=2:
            str="火币交易对:"+symbol+", 周期:"+period+" 向上穿越"
            flag = 2
        else:
            str=""
        print(flag)
        if not str == "":
            email_handler.send_mail(str, str)    
        time.sleep(delay)
    

if __name__ == "__main__":
    # 创建两个线程
    #thread1 = huobiThread("btsusdt-30min", 'btsusdt', '1min', 200, 7, 25,1)
    thread2 = huobiThread("btsusdt-30min", 'btsusdt', '15min', 200, 7, 25,2)
    thread3 = huobiThread("btsusdt-60min", 'btsusdt', '60min', 200, 7, 25,2)

    #thread1.start()
    thread2.start()
    thread3.start()


