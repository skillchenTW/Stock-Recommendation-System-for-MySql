## Stock Recommendation System ##
#### 後台資料庫: MySql ####

### Countries (indices) we are working with ####
-   台灣 Taiwan (TW)
-   中國 China (CN)
-   印度 India (Nifty 50)
-   巴西 Brazil (Bovespa)
-   俄羅斯 Russia (RTSI)

### 程式簡介
    t01_CrTable.py                      | 建立資料表Schema
    t02_GetTickerList.py                | 抓取各個國家的股票代號清單    
                                          ticker\bovespa.csv    \ticker\nifty.csv  ticker\rts.csv
    t03_GetTwTicker.py                  | 抓取台灣股票代號清單          
                                          ticker\tw.csv
    t04_ImportTicker.py                 | 抓取各國股票清單
    t05_Macd_GoldenCross_RSI_Signals.py | MACD|Golden Cross|RSI 信號
    Recommender.py                      | 將t05xxx.py 類別化
    t06_testRecommender.py              | 測試Recommender     類是否可以正常執行
    AutoSend.py                         | 傳送郵件
    ticker\                             | 抓取各國的股票代號CSV,存放目錄
    sqlscript\                          | 關於MySql查詢語句
    
### Creds.py 範例說明
    sender = "send@copr.com.cn"
    receiver = "receive@corp.com.cn"
    emailserver = 'email.usercompany.com'
    password = 'password'

### MySql相關語法
```sql
SELECT table_name FROM information_schema.tables WHERE table_schema ="tw"
select count(*) as TOTALNUMBEROFTABLES FROM INFORMATION_SCHEMA.TABLES WHERE Table_SCHEMA='tw';
select count(*) as TOTALNUMBEROFTABLES FROM INFORMATION_SCHEMA.TABLES WHERE Table_SCHEMA='Bovespa';
select count(*) as TOTALNUMBEROFTABLES FROM INFORMATION_SCHEMA.TABLES WHERE Table_SCHEMA='nifty50';
select count(*) as TOTALNUMBEROFTABLES FROM INFORMATION_SCHEMA.TABLES WHERE Table_SCHEMA='rtsi';
```


```sql
SELECT * FROM TW.`2330.tw` order by Date desc;
SELECT MAX(Date) as MaxDate FROM TW.`2330.tw`;
```


(env) PS F:\Stock_Recommendation> python t06_testRecommender.py
執行日期: 2021/09/30 
==**印度 India (Nifty 50)**============================================

-   Decision GC Buying Signal for bpcl.ns
-   Decision MACD Buying Signal for drreddy.ns
-   Decision MACD Buying Signal for sunpharma.ns
-   Decision RSI/SMA Buying Signal for tataconsum.ns

==**俄羅斯 Russia (RTSI)**=============================================

-   Decision GC Buying Signal for upro.me

==**巴西 Brazil (Bovespa)**============================================

-   Decision RSI/SMA Buying Signal for brkm5.sa
-   Decision GC Buying Signal for cvcb3.sa
-   Decision MACD Buying Signal for sanb11.sa

==**台灣 Taiwan (TW)**=================================================

-   Decision MACD Buying Signal for 0061.tw
-   Decision GC Buying Signal for 00709.tw
-   Decision RSI/SMA Buying Signal for 00709.tw
-   Decision RSI/SMA Buying Signal for 00714.tw
-   Decision MACD Buying Signal for 008201.tw
-   Decision RSI/SMA Buying Signal for 00861.tw
-   Decision RSI/SMA Buying Signal for 00875.tw
-   Decision GC Buying Signal for 00878.tw
-   Decision GC Buying Signal for 1213.tw
-   Decision GC Buying Signal for 1235.tw
-   Decision RSI/SMA Buying Signal for 1418.tw
-   Decision MACD Buying Signal for 1456.tw
-   Decision GC Buying Signal for 1456.tw
-   Decision GC Buying Signal for 1472.tw
-   Decision MACD Buying Signal for 1514.tw
-   Decision MACD Buying Signal for 1589.tw
-   Decision GC Buying Signal for 1732.tw
-   Decision RSI/SMA Buying Signal for 1802.tw
-   Decision RSI/SMA Buying Signal for 2008.tw
-   Decision RSI/SMA Buying Signal for 2020.tw
-   Decision RSI/SMA Buying Signal for 2022.tw
-   Decision RSI/SMA Buying Signal for 2024.tw
-   Decision RSI/SMA Buying Signal for 2029.tw
-   Decision RSI/SMA Buying Signal for 2031.tw
-   Decision RSI/SMA Buying Signal for 2032.tw
-   Decision RSI/SMA Buying Signal for 2033.tw
-   Decision RSI/SMA Buying Signal for 2069.tw
-   Decision RSI/SMA Buying Signal for 2114.tw
-   Decision RSI/SMA Buying Signal for 2351.tw
-   Decision MACD Buying Signal for 2406.tw
-   Decision RSI/SMA Buying Signal for 2441.tw
-   Decision RSI/SMA Buying Signal for 2465.tw
-   Decision RSI/SMA Buying Signal for 2466.tw
-   Decision RSI/SMA Buying Signal for 2476.tw
-   Decision GC Buying Signal for 2504.tw
-   Decision MACD Buying Signal for 2538.tw
-   Decision MACD Buying Signal for 2605.tw
-   Decision RSI/SMA Buying Signal for 2611.tw
-   Decision RSI/SMA Buying Signal for 2614.tw
-   Decision GC Buying Signal for 2637.tw
-   Decision GC Buying Signal for 2723.tw
-   Decision GC Buying Signal for 2801.tw
-   Decision RSI/SMA Buying Signal for 3031.tw
-   Decision MACD Buying Signal for 3046.tw
-   Decision RSI/SMA Buying Signal for 3312.tw
-   Decision RSI/SMA Buying Signal for 3356.tw
-   Decision MACD Buying Signal for 3543.tw
-   Decision GC Buying Signal for 3665.tw
-   Decision GC Buying Signal for 3711.tw
-   Decision MACD Buying Signal for 4148.tw
-   Decision GC Buying Signal for 4164.tw
-   Decision GC Buying Signal for 4557.tw
-   Decision RSI/SMA Buying Signal for 5269.tw
-   Decision MACD Buying Signal for 5284.tw
-   Decision RSI/SMA Buying Signal for 5285.tw
-   Decision GC Buying Signal for 5388.tw
-   Decision GC Buying Signal for 6164.tw
-   Decision RSI/SMA Buying Signal for 6202.tw
-   Decision RSI/SMA Buying Signal for 6215.tw
-   Decision GC Buying Signal for 6257.tw
-   Decision RSI/SMA Buying Signal for 6257.tw
-   Decision RSI/SMA Buying Signal for 8110.tw
-   Decision RSI/SMA Buying Signal for 8150.tw
-   Decision RSI/SMA Buying Signal for 8261.tw
-   Decision MACD Buying Signal for 8473.tw
##### ===================================================================
