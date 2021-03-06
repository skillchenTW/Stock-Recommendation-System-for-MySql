

--查詢股價資料
SELECT * FROM TW.`2330.tw` order by Date desc;

--抓取各資料庫有多少支股票資料
select count(*) as TOTALNUMBEROFTABLES FROM INFORMATION_SCHEMA.TABLES WHERE Table_SCHEMA='tw';
select count(*) as TOTALNUMBEROFTABLES FROM INFORMATION_SCHEMA.TABLES WHERE Table_SCHEMA='Bovespa';
select count(*) as TOTALNUMBEROFTABLES FROM INFORMATION_SCHEMA.TABLES WHERE Table_SCHEMA='nifty50';
select count(*) as TOTALNUMBEROFTABLES FROM INFORMATION_SCHEMA.TABLES WHERE Table_SCHEMA='rtsi';

-- 抓取最大日期
SELECT MAX(Date) as MaxDate FROM TW.`2330.tw`;