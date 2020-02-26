from pandas_datareader import data as pd
import yfinance as yf

try:
	yf.pdr_override()

	data = pd.get_data_yahoo("MSFT", interval="1m").to_html()
	print(data)
except Exception as e:
	raise