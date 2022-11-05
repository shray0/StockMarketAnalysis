import pandas as pb #library for numbers
import yfinance as yf #yahoo finance
import datetime #library for dates, months days etc
from datetime import date, timedelta #specific date, specific time
import plotly.graph_objects as go #makes charts from data yfinance
import plotly.express as px 

today = date.today() #imports today date from module datetime, () is used when opening function

todays_date = today.strftime("%Y-%m-%d")  #formatting the date into a string time
end_date = todays_date #refers to the end of the year ago graph, meaning todays date

year_ago = date.today()-timedelta(days = 365) #finding the exact date of a year ago
year_ago = year_ago.strftime("%Y-%m-%d") #putting year_ago into date format eg 2022 11 05
start_date = year_ago #refers to the beginning of the year ago graph, meaning a year agos date

print('start_date', start_date)
print('end_date', end_date)

stock_data = yf.download('GOOG',start = start_date, end = end_date, progress = False) #downloading google stock, defining the start and end parameters using our previous variables, progress is false to set the data constand and not keep changing to the todays date  
stock_data['Date'] = stock_data.index #making a list of all stock prices each date
stock_data = stock_data[['Date','Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']] #Opening time for stocks, High is highest price, Low is lowest price, close is closing time, adjclose is adjusted price at end, and volumn is number of shares traded
stock_data.reset_index(drop = True, inplace = True) #indexing data, settings make stock visually look better
print(stock_data.head())

# figure = go.Figure(data=[go.Candlestick(x = stock_data['Date'], open = stock_data['Open'], high = stock_data['High'],low = stock_data['Low'], close = stock_data['Close'])]) #specifying type of graph, adding graph parameters
# figure.update_layout(title = 'Google Candlestick Graph', xaxis_rangeslider_visible = False) #adding title, deleting the xaxis scroll slider
# figure.show()

# figure = px.bar(stock_data,x='Date', y='Close') #for bar graph
# figure.update_layout(title = 'Google Bar Graph', xaxis_rangeslider_visible = False)
# figure.show()

figure = px.line(stock_data,x='Date', y='Close') #for line graph
figure.update_layout(title = 'Google Line Graph', xaxis_rangeslider_visible = True)
figure.update_xaxes(
    rangeselector = dict(
        buttons = list([
           dict(count=1, label = '1 month', step = 'month', stepmode = 'backward'),
           dict(count=3, label = '3 months', step = 'month', stepmode = 'backward'),
           dict(count=6, label = '6 months', step = 'month', stepmode = 'backward'),
           dict(count=1, label = '1 year', step = 'year', stepmode = 'backward'),
           dict(step = 'all')
        ])
    )
)
figure.show()
