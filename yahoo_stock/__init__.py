import pandas_datareader.data as web
import pandas as pd
import datetime
from fbprophet import Prophet

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 12, 31)

df = web.DataReader("078930.KS", "yahoo", start, end)
print(df)

"""
 df.Capacity = df.Capacity.str.replace(r"\[.*\]", "")
 """
stock = df[0]
print(stock.head())
stock['Close'].plot(figsize=(12,6), grid=True)
df = pd.DataFrame({'ds': stock['Volume'], 'y': stock['Close']})
print(df)
prophet = Prophet(yearly_sessionality=True, daily_sessonality=True)
prophet.fit(df)
future = prophet.make_future_dataframe(perods=30)
forecast = prophet.predict(future)
prophet.plot(forecast)
