from exchangeapi.huobi import rest_api

if __name__ == "__main__":
    #websocket.start()
    print(rest_api.get_kline('ethusdt',"1min",200));
    
    print('hello');