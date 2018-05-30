from service import rest_api_service
from service import websocket_subscribe_service

if __name__ == "__main__":
    #websocket.start()
    print(rest_api_service.get_kline('ethusdt',"1min",200));
    
    print('hello');