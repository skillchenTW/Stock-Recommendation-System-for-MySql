import sqlalchemy
import pymysql
import ta 
import pandas as pd 
import numpy as np 

pymysql.install_as_MySQLdb()

indices = ['TW','Nifty50','RTSI','Bovespa']

engine = sqlalchemy.create_engine('mysql://root:F9n3v47t@localhost:3306')


# tw = pd.read_csv('ticker/tw.csv')
# tw_ = tw.ticker.to_list()
# #print(tw_)

# nifty = pd.read_csv('ticker/nifty.csv')
# nifty_ = nifty.Symbol.to_list()
# nifty_ = [xticker + '.NS' for xticker in nifty_]
# #print(nifty_)

# bovespa = pd.read_csv('ticker/bovespa.csv')
# bovespa_ = bovespa['Ticker'].to_list()
# bovespa_ = [xticker + '.SA' for xticker in bovespa_]
# #print(bovespa_)

# rts = pd.read_csv('ticker/rts.csv')
# rts_ = rts['Ticker symbol'].to_list()
# rts_ = [xticker + '.ME' for xticker in rts_]
# #print(rts_)


# mapper ={'TW':tw_, 'Nifty50':nifty_, 'Bovespa':bovespa_, 'RTSI':rts_}


# 抓取該資料庫的資料表清單
def gettables(index):
    query = f"""
        SELECT table_name FROM information_schema.tables
        WHERE table_schema = '{index}'
    """
    df = pd.read_sql(query,engine)
    df['Schema'] = index
    return df 

def getprices(which):
    prices = []
    for table , schema in zip(which.TABLE_NAME, which.Schema):
        sql = schema+'.'+f'`{table}`'        
        prices.append(pd.read_sql(f"SELECT Date, Close From {sql}", engine))
    return prices

def MACDdecision(df):
    df['MACD_diff'] = ta.trend.macd_diff(df.Close)
    df['Decision MACD'] = np.where((df.MACD_diff > 0) & (df.MACD_diff.shift(1) < 0), True, False )

def Goldencrossdecision(df):
    df['SMA20'] = ta.trend.sma_indicator(df.Close, window=20)
    df['SMA50'] = ta.trend.sma_indicator(df.Close, window=50)
    df['Signal'] = np.where(df['SMA20'] > df['SMA50'], True, False)
    df['Decision GC'] = df.Signal.diff()

def RSI_SAMdecision(df):
    df['RSI'] = ta.momentum.rsi(df.Close, window=10)
    df['SMA200'] = ta.trend.sma_indicator(df.Close,window=200)
    df['Decision RSI/SMA'] = np.where((df.Close > df.SMA200) & (df.RSI < 30), True, False)

def applytechnicals(which):
    prices = getprices(which)
    for frame in prices:
        MACDdecision(frame)
        Goldencrossdecision(frame)
        RSI_SAMdecision(frame)
    return prices

def recommender(which):
    indicators = ['Decision MACD','Decision GC', 'Decision RSI/SMA']
    for symbol, frame in zip(which.TABLE_NAME,applytechnicals(which)):
        if frame.empty is False:
            for indicator in indicators:
                if frame[indicator].iloc[-1] == True:
                    print(f"{indicator} Buying Signal for " + symbol)


# nifty = gettables('Nifty50')
# df = applytechnicals(nifty)[0]
# #print(df)
# recommender(nifty)

indices = ['TW','Nifty50','RTSI','Bovespa']
for indice in indices:
    recommender(gettables(indice))
# recommender(gettables("Rts"))
# recommender(gettables("Nifty50"))
# recommender(gettables("Bovespa"))