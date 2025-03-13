import pandas as pd 
import yfinance as yf
import matplotlib.pyplot as plt

ticker = 'TSLA'
stock_data = yf.download(ticker, start='2023-01-01', end='2023-12-31')
print(stock_data.head())

stock_data['20_MA'] = stock_data['Close'].rolling(window=20).mean()
print(stock_data.tail())

plt.figure(figsize=(12, 6))
plt.plot(stock_data['Close'], label='Close Price', color='blue')
plt.plot(stock_data['20_MA'], label='20 Day Moving Average', color='orange')
plt.title(f'{ticker} Stock Price and 20 Day Moving Average')
plt.xlabel('Date')
plt.ylabel('Price(USD)')
plt.legend
plt.show()

stock_data['Daily Return'] = stock_data['Close'].pct_change()

avg_daily_return = stock_data['Daily Return'].mean()

print(f"The average daily return for {ticker} is {avg_daily_return}")




