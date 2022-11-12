import pandas as pb #library for numbers
import yfinance as yf #yahoo finance
import datetime #library for dates, months days etc
from datetime import date, timedelta #specific date, specific time
import plotly.graph_objects as go #makes charts from data yfinance
import plotly.express as px 

stock_input = input('Type in the stock ticker \n Stock: ')


graph_type = input('Type 1 for Candlestick Graph, 2 for Bar Graph, 3 for Line Graph, & 4 for Scatterplot Graph \n Graph Type: ')
xslider_input = input('Type True for xslider, False for none \n Input: ')
xslider_input = eval(xslider_input)
button_input = input('Type Y for buttons, N for none \n Input: ')

today = date.today() #imports today date from module datetime, () is used when opening function

todays_date = today.strftime("%Y-%m-%d")  #formatting the date into a string time
end_date = todays_date #refers to the end of the year ago graph, meaning todays date

year_ago = date.today()-timedelta(days = 365) #finding the exact date of a year ago
year_ago = year_ago.strftime("%Y-%m-%d") #putting year_ago into date format eg 2022 11 05
start_date = year_ago #refers to the beginning of the year ago graph, meaning a year agos date

print('start_date', start_date)
print('end_date', end_date)



stock_data = yf.download(stock_input.upper(),start = start_date, end = end_date, progress = False) #downloading google stock, defining the start and end parameters using our previous variables, progress is false to set the data constand and not keep changing to the todays date  
stock_data['Date'] = stock_data.index #making a list of all stock prices each date
stock_data = stock_data[['Date','Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']] #Opening time for stocks, High is highest price, Low is lowest price, close is closing time, adjclose is adjusted price at end, and volumn is number of shares traded
stock_data.reset_index(drop = True, inplace = True) #indexing data, settings make stock visually look better
print(stock_data.head())

# Candlestick Graph
figure1 = go.Figure(data=[go.Candlestick(x = stock_data['Date'], open = stock_data['Open'], high = stock_data['High'],low = stock_data['Low'], close = stock_data['Close'])]) #specifying type of graph, adding graph parameters
figure1.update_layout(title = stock_input.upper() + ' Candlestick Graph', xaxis_rangeslider_visible = xslider_input) #adding title, deleting the xaxis scroll slider
if button_input == 'Y':
    figure1.update_xaxes(
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



#Bar Graph
figure2 = px.bar(stock_data,x='Date', y='Close') #for bar graph
figure2.update_layout(title = stock_input.upper() +  ' Bar Graph', xaxis_rangeslider_visible = xslider_input)
if button_input == 'Y':
    figure2.update_xaxes(
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




#Line graph with buttons
figure3 = px.line(stock_data,x='Date', y='Close') #for line graph
figure3.update_layout(title = stock_input.upper() + ' Line Graph', xaxis_rangeslider_visible = xslider_input)
if button_input == 'Y':
    figure3.update_xaxes(
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


#Scatterplot graph

figure4 = px.scatter(stock_data,x='Date', y='Close', range_x=[str(start_date),str(end_date)]) #scatterplot graph
figure4.update_layout(title = stock_input.upper() + ' Scatterplot Graph',xaxis_rangeslider_visible = xslider_input)
if button_input == 'Y':
    figure4.update_xaxes(
        rangebreaks = [dict( #breaking the dots in to scatterplots, so they arent connected
            bounds = ['sat','sun'] 
        )
        ]
        ,rangeselector = dict(
            buttons = list([
            dict(count=1, label = '1 month', step = 'month', stepmode = 'backward'),
            dict(count=3, label = '3 months', step = 'month', stepmode = 'backward'),
            dict(count=6, label = '6 months', step = 'month', stepmode = 'backward'),
            dict(count=1, label = '1 year', step = 'year', stepmode = 'backward'),
            dict(step = 'all')
            ])
        )
    )








# if graph_type == "1":
#     figure1.show()
#     print('Graph 1')

# if graph_type == "2":
#     figure2.show()
#     print('Graph 2')

# if graph_type == "3":
#     figure3.show()
#     print('Graph 3')

# if graph_type == "4":
#     figure4.show()
#     print('Graph 4')

match graph_type:
    case '1':
        figure1.show()
    case '2':
        figure2.show()
    case '3':
        figure3.show()
    case '4':
        figure4.show()    
