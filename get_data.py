from hashlib import new
from operator import delitem
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

# fetching candle stick data

candles=client.get_klines(symbol='BTCUSDT',interval=Client.KLINE_INTERVAL_30MINUTE)
print(len(candles))


# creating file for writing data
csvfile=open('candlestick.csv','w',newline='')
historical_Data=open('historicalData.csv','w',newline='')


# writing using csv
candlestick_writer= csv.writer(csvfile, delimiter=',',)
historicalData_writer=csv.writer(historical_Data,delimiter=',')


# iterating through data
for candlestick in candles:
    candlestick_writer.writerow(candlestick)


# get historical data
candle_history=client.get_historical_klines('BTCUSDT',Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
# print(candle_history)


# write historical data into file
for candle_data in candle_history:
    historicalData_writer.writerow(candle_data)
