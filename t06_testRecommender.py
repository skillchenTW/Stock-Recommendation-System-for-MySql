import sqlalchemy
import pymysql
import ta 
import pandas as pd 
import numpy as np 
import Recommender as reco

print("==印度 India (Nifty 50)============================================")
niftyinstance = reco.Recommender('Nifty50')
print(niftyinstance.recommender())
# print("     ******************************************************        ")
# df = niftyinstance.applytechnicals()
# print(df)
print("==俄羅斯 Russia (RTSI)=============================================")
rtsiinstance = reco.Recommender('RTSI')
print(rtsiinstance.recommender())
print("==巴西 Brazil (Bovespa)============================================")
bovespainstance = reco.Recommender('Bovespa')
print(bovespainstance.recommender())
print("==台灣 Taiwan (TW)=================================================")
twinstance = reco.Recommender('TW')
print(twinstance.recommender())
print("===================================================================")

