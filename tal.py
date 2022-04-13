import numpy
import talib
from numpy import genfromtxt

close=numpy.random.random(100)
# print(close)


# moving average
moving_average=talib.SMA(close,timeperiod=10)
#print(moving_average)

# rsi indicator
rsi=talib.RSI(close)
#print(rsi)


# reading data from csv file
my_data=genfromtxt('candlestick.csv',delimiter=',')
#print(my_data)

# reading a specific field
closePrice=my_data[:,4]
#print(closePrice)

# rsi of close price
rsi=talib.RSI(close)
print(rsi)
