import pandas as pd
import sqlalchemy
import pymysql

pymysql.install_as_MySQLdb()

nifty = pd.read_html('https://en.wikipedia.org/wiki/NIFTY_50')[1]
nifty.to_csv('ticker/nifty.csv')
bovespa = pd.read_html('https://en.wikipedia.org/wiki/List_of_companies_listed_on_B3')[0]
bovespa.to_csv('ticker/bovespa.csv')
rts = pd.read_html('https://en.wikipedia.org/wiki/RTS_Index')[1]
rts.to_csv('ticker/rts.csv')

tw = pd.read_csv('ticker/tw.csv')
tw_ = tw.ticker.to_list()
print(tw_)
nifty_ = nifty.Symbol.to_list()

#Company Name | Symbol | Sector
#print(nifty)
# Company Ticker | Industry | Headquarters
#print(bovespa)
#Company| Ticker symbol | Stock type | Industry
#print(rts)