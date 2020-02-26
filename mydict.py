from pandas_datareader import data as pd
import yfinance as yf

try:
	yf.pdr_override()

	data = pd.get_data_yahoo("MSFT", start="2020-01-02", end="2020-02-25").to_html()
	print(data)
except Exception as e:
	raise