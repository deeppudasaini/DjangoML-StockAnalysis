import pandas as pd
import requests
import json
import matplotlib.pyplot as plt
import plotly.graph_objects as go
url = "https://twelve-data1.p.rapidapi.com/time_series"

querystring = {"symbol":"AMZN","interval":"1day","outputsize":"30","format":"json"}

headers = {
    'x-rapidapi-key': "0ec2caeb83msh6e33b962033e669p1d1f91jsn809f4fccd578",
    'x-rapidapi-host': "twelve-data1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)


dff=pd.DataFrame(response.json()['values'])

# plt.plot(dff['open'],dff['close'])
# plt.candle(dff['close'][:10], dff['open'][:10])
plt = go.Figure(data=[go.Candlestick(x=dff['datetime'],
                open=dff['open'],
                high=dff['high'],
                low=dff['low'],
                close=dff['close'])])

plt.show()
print(dff)

