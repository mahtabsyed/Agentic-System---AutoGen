# filename: stock_prices.py
import yfinance as yf
import matplotlib.pyplot as plt

# Get the historical stock prices for META (formerly known as Facebook)
meta = yf.Ticker("META")
meta_data = meta.history(period="1y")

# Get the historical stock prices for Tesla
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="1y")

# Plotting the stock price change
plt.figure(figsize=(14, 7))
plt.plot(meta_data['Close'], label='META (Facebook)')
plt.plot(tesla_data['Close'], label='Tesla')
plt.title('Historical Stock Prices')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.legend()
plt.grid()
plt.show()