import sqlalchemy
import pymysql
import ta 
import pandas as pd 
import numpy as np 
import yfinance as yf


pymysql.install_as_MySQLdb()
#indices = ['TW','Nifty50','RTSI','Bovespa']

class Recommender:    
    engine = sqlalchemy.create_engine('mysql://root:F9n3v47t@localhost:3306')

    def __init__(self,index):
        self.index = index 

    # 抓取該資料庫的資料表清單
    def gettables(self):
        query = f"""
            SELECT table_name FROM information_schema.tables
            WHERE table_schema = '{self.index}'
        """
        df = pd.read_sql(query,self.engine)
        df['Schema'] = self.index
        return df 

    def maxdate(self):
        req = self.index + "." + f"`{self.gettables().TABLE_NAME[0]}`"
        return pd.read_sql(f"SELECT MAX(Date) as MaxDate FROM {req}", self.engine)

    def updateDB(self):
        maxdate = self.maxdate()['MaxDate'][0]
        engine = sqlalchemy.create_engine('mysql://root:F9n3v47t@localhost:3306/'+ self.index)
        for symbol in self.gettables().TABLE_NAME:
            data = yf.download(symbol, start=maxdate)
            data = data[data.index > maxdate]
            data = data.reset_index()
            data.to_sql(symbol, engine, if_exists='append')
        print(f"{self.index} successfully updated")

    def getprices(self):
        prices = []
        for table , schema in zip(self.gettables().TABLE_NAME, self.gettables().Schema):
            sql = schema+'.'+f'`{table}`'        
            prices.append(pd.read_sql(f"SELECT '{table}' Ticker,Date, Close From {sql}", self.engine))        
        return prices    

    def MACDdecision(self,df):
        df['MACD_diff'] = ta.trend.macd_diff(df.Close)
        df['Decision MACD'] = np.where((df.MACD_diff > 0) & (df.MACD_diff.shift(1) < 0), True, False )

    def Goldencrossdecision(self,df):
        df['SMA20'] = ta.trend.sma_indicator(df.Close, window=20)
        df['SMA50'] = ta.trend.sma_indicator(df.Close, window=50)
        df['Signal'] = np.where(df['SMA20'] > df['SMA50'], True, False)
        df['Decision GC'] = df.Signal.diff()

    def RSI_SAMdecision(self,df):
        df['RSI'] = ta.momentum.rsi(df.Close, window=10)
        df['SMA200'] = ta.trend.sma_indicator(df.Close,window=200)
        df['Decision RSI/SMA'] = np.where((df.Close > df.SMA200) & (df.RSI < 30), True, False)

    def applytechnicals(self):
        prices = self.getprices()
        for frame in prices:
            self.MACDdecision(frame)
            self.Goldencrossdecision(frame)
            self.RSI_SAMdecision(frame)
        return prices

    def recommender(self):
        signals = []
        indicators = ['Decision MACD','Decision GC', 'Decision RSI/SMA']
        for symbol, frame in zip(self.gettables().TABLE_NAME,self.applytechnicals()):
            if frame.empty is False:
                for indicator in indicators:
                    if frame[indicator].iloc[-1] == True:
                        signals.append(f"{indicator} Buying Signal for " + symbol)    
        return signals

   
