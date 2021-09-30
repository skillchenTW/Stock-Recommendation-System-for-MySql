import psycopg2
import pandas as pd

conn = psycopg2.connect(database="st",user="postgres",password="dba",host="localhost",port="5433")
cur = conn.cursor()
cur.execute("select stid,stname from ticker where selkey='Y' order by stid;")
result = cur.fetchall()
tickers = pd.DataFrame(result)
tickers.columns=['ticker','company']
tickers['ticker'] = tickers['ticker'] + ".TW"
tickers.to_csv('ticker/tw.csv')
#print(tickers)

print(tickers)