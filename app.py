from crypt import methods
from django.shortcuts import render,redirect
from flask import Flask, render_template,request,flash
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
# from requests import request
import config
import csv
from binance.enums import *


app=Flask(__name__)
app.secret_key=config.SECRET_KEY

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

@app.route('/buy',methods=['GET','POST'])
def buy():

    symbol=request.form['symbol']
    quantity=request.form['quantity']
    try:
        order = client.create_order(
        symbol=symbol,
        side=SIDE_BUY,
        type=ORDER_TYPE_LIMIT,
        quantity=quantity,
        price='0.00001')
    
    except Exception as e:
        flash(e.message,"error")

    
    return redirect('/')

@app.route('/sell')
def sell():
    return 'sell'

@app.route('/settings')
def settings():
    return 'settings'


if __name__=="__main__":
    app.run(debug=True)


