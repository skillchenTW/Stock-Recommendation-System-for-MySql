import pandas as pd
import sqlalchemy
import pymysql
import yfinance as yf

indices = ['TW','Nifty50','RTSI','Bovespa']

pymysql.install_as_MySQLdb()

tw = pd.read_csv('ticker/tw.csv')
tw_ = tw.ticker.to_list()
#print(tw_)

nifty = pd.read_csv('ticker/nifty.csv')
nifty_ = nifty.Symbol.to_list()
nifty_ = [xticker + '.NS' for xticker in nifty_]
#print(nifty_)

bovespa = pd.read_csv('ticker/bovespa.csv')
bovespa_ = bovespa['Ticker'].to_list()
bovespa_ = [xticker + '.SA' for xticker in bovespa_]
#print(bovespa_)

rts = pd.read_csv('ticker/rts.csv')
rts_ = rts['Ticker symbol'].to_list()
rts_ = [xticker + '.ME' for xticker in rts_]
#print(rts_)


mapper ={'TW':tw_, 'Nifty50':nifty_, 'Bovespa':bovespa_, 'RTSI':rts_}

for index in indices:
    engine = sqlalchemy.create_engine('mysql://root:F9n3v47t@localhost:3306/'+index)
    for symbol in mapper[index]:
        df = yf.download(symbol, start='2020-01-01')
        df = df.reset_index()
        df.to_sql(symbol, engine)