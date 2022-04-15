from django.shortcuts import render
from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    title='CoinView'
    return render_template('index.html',title=title)

@app.route('/buy')
def buy():
    return 'buy'

@app.route('/sell')
def sell():
    return 'sell'

@app.route('/settings')
def settings():
    return 'settings'


if __name__=="__main__":
    app.run(debug=True)


