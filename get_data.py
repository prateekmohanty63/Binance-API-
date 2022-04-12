from symtable import Symbol
import csv

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


csvfile=open('candlestick.csv','w',newline='')

# writing using csv
candlestick_writer= csv.writer(csvfile, delimiter=',',)


for candlestick in candles:
    candlestick_writer.writerow(candlestick)