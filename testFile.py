import pandas as pd

bc = pd.read_csv('BTC-USD.csv')

bc['Date'] = pd.to_datetime(bc.Date)

bc.set_index('Date', inplace= True)

bc = bc[['Close']].loc['2017-01-01':]