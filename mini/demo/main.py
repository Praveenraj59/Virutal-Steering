from flask import Flask, render_template, send_file
import matplotlib.pyplot as plt
import io
import numpy as np
import pandas as pd

from pandas_datareader import data as pdr

# Market Data
import yfinance as yf

#Graphing/Visualization
import datetime as dt
import plotly.graph_objs as go


app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot.png')
def plot_png():
    fig = create_figure()  
    
    # Raw Package

# Override Yahoo Finance
    yf.pdr_override()

# Create input field for our desired stock


# Retrieve stock data frame (df) from yfinance API at an interval of 1m
    df = yf.download(tickers=aapl,period='1d',interval='1m')

    print(df)

# Declare plotly figure (go)
    fig=go.Figure()

    fig.add_trace(go.Candlestick(x=df.index,
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'], name = 'market data'))

    fig.update_layout(
        title= str(stock)+' Live Share Price:',
        yaxis_title='Stock Price (USD per Shares)')

    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=15, label="15m", step="minute", stepmode="backward"),
                dict(count=45, label="45m", step="minute", stepmode="backward"),
                dict(count=1, label="HTD", step="hour", stepmode="todate"),
                dict(count=3, label="3h", step="hour", stepmode="backward"),
                dict(step="all")
            ])
        )
    )

    fig.show()




fig.savefig('my_plot.png')
    
output = io.BytesIO()
fig.savefig(output, format='png')
output.seek(0)
return send_file(output, mimetype='image/png')

def create_figure():
    # Example of creating a simple plot
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 4, 9])
    return fig

if _name_ == '_main_':
    app.run(debug=True)