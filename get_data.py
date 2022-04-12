from symtable import Symbol

from sqlalchemy import Interval
import config


from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
client = Client(config.API_KEY,config.API_SECRET)


# prices=client.get_all_tickers()
# #print(prices)

# for price in prices:
#     print(price)

candles=client.get_klines(symbol='BTCUSDT',interval=Client.KLINE_INTERVAL_30MINUTE)
print(len(candles))