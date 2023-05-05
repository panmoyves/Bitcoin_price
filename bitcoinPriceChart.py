# primary we need to install and import the following liberies 
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot 
import matplotlib.pyplot as plt
import datetime
from pycoingecko import CoinGeckoAPI
from typing import Dict
from mplfinance.original_flavor import candlestick2_ochl

dict_ = {'a': [11, 21, 31], 'b': [12, 22, 32]}
df = pd.DataFrame(dict_)
type(df)
print(df.mean())


cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id = 'bitcoin', vs_currency = 'usd', days =45)
type(bitcoin_data)

bitcoin_price_data = bitcoin_data['prices']

bitcoin_price_data[0:5]

#now its time to turn the data in to Pandas Dataframe
data = pd.DataFrame(bitcoin_price_data, columns= ['TimeStamp', 'Price'])

#now we need to convert the timestamp to datetime

data['date'] = data['TimeStamp'].apply(lambda d: datetime.date.fromtimestamp(d/1000.0))

#now we can fine the max and min
candlestick_data = data.groupby(data.date, as_index=False).agg({"Price": ['min', 'max', 'first', 'last']})

#now we can plot the candlestic chart

fig = go.Figure(data=[go.Candlestick(x=candlestick_data['date'],
                open=candlestick_data['Price']['first'], 
                high=candlestick_data['Price']['max'],
                low=candlestick_data['Price']['min'], 
                close=candlestick_data['Price']['last'])
                ])

fig.update_layout(xaxis_rangeslider_visible=False)

fig.show()