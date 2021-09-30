import sqlalchemy
import pymysql

pymysql.install_as_MySQLdb()

indices = ['TW','CN','Nifty50','RTSI','Bovespa']

def schemacreator(index):
    engine = sqlalchemy.create_engine('mysql://root:F9n3v47t@localhost:3306/')
    engine.execute(sqlalchemy.schema.CreateSchema(index))

def job1():
    # 建立資料表Schema
    for index in indices:
        schemacreator(index)



if __name__ == "__main__":
    job1()


