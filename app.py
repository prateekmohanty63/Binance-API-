from django.shortcuts import render
from flask import Flask, render_template
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import config
import csv
from binance.enums import *


app=Flask(__name__)

client = Client(config.API_KEY,config.API_SECRET)


@app.route('/')
def index():
    title='CoinView'
    print(client)

    info=client.get_account()
    #print(info)

    exchange_info=client.get_exchange_info()
    symbols=exchange_info['symbols']

    balances=info['balances']
    print(balances)


    return render_template('index.html',title=title)

@app.route('/buy')
def buy():
    order = client.create_order(
    symbol='BNBBTC',
    side=SIDE_BUY,
    type=ORDER_TYPE_LIMIT,
    timeInForce=TIME_IN_FORCE_GTC,
    quantity=100,
    price='0.00001')
    return 'buy'

@app.route('/sell')
def sell():
    return 'sell'

@app.route('/settings')
def settings():
    return 'settings'


if __name__=="__main__":
    app.run(debug=True)


