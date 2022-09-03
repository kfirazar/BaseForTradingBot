import datetime
import time

import mysql.connector

import apikey
from apikey import GetApiKey
import requests
con = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="KFIRnoya4!",
    database = "coins",
    port = '3306'
)
cur = con.cursor()
cur.close()
"""
cur = con.cursor()
cur.execute("SELECT * FROM players")
rows = cur.fetchall()
for r in rows:
    print(f'ID : {r[0]} Name : {r[1]}')
#cur.execute("SELECT * FROM TetrisDb")
#cur.execute("INSERT INTO ScoreBoard (NickName,Date,Score) VALUES(Kfir,31/12/2021/,-1)")
#mycursor.execute()
#mycursor.execute("CREATE TABLE ScoreBoard_DB (name VARCHAR(50)),score int UNSIGNED , PersonId int PRIMARY KEY AUTO_INCREMENT)")
#mycursor.execute("CREATE DATABASE TetrisDb")
#for x in mycursor:
#    print(x)"""
cur = con.cursor()
def PrintDb():
    cur.execute("Show databases")
    for db in cur:
        print(db)
def AddNewCoin():#symbol,buy,withdraw
    sql = "INSERT INTO coins.coindata (Symbol ,OgBuyPrice, WithDraw)VALUES (%s,%s,%s,%s,%s)"
    value = ('PlutoCoin' , '100000' , '1000000')
    return sql, value


def CheckCon():
    if con:
        print('Connected')
        return True
    else:
        print('Not connected')
        return False

def ExectuteSqlFunc(comm,x1):
    try:
        
        comm = str(comm).lower()#('search,Symbol,OgBuyPrice)
        if comm == 'search':
            x1  = str(x1).upper()#Symbol
            #x2  = str(x2).upper()#OgBuyPrice
            sql = """SELECT Symbol,OgBuyPrice,Amount FROM coins.coindata WHERE Symbol = %s"""
            values = (x1,)
            cur.execute(sql , (values))
            result = cur.fetchone()
            print(result)
            sql = None
        elif comm == "add":#('add',None,None)
            Date = datetime.datetime.now().__str__()  # datetime.date.today()
            print(Date)
            Symbol = input("Symbol:")
            OgBuyPrice = float(input("OgBuyPrice:"))
            WithDraw = float(input("WithDraw"))
            Amount = float(input("Coin/s amount:"))
            sql = "INSERT INTO coins.coindata (Symbol ,OgBuyPrice, WithDraw,Date,Amount)VALUES (%s,%s,%s,%s,%s)"
            values = (Symbol.upper() , OgBuyPrice , WithDraw , Date , Amount)
            cur.execute(sql , values)
            con.commit()

    except:
        pass
        #print("Oops...")
    finally:
        con.close()
def CheckCurrentValue():
    try:
        sql = "SELECT * FROM coins.coindata"
        cur.execute(sql)
        list = cur.fetchall()
        for x in list: #0 = Symbol , 1 = BuyPrice , 2 = WithDraw
            print(x)
            #if(x[])

    except:
        print('Oops...')
    finally:
        con.close()
"""
headers = {
 'X-CMC_PRO_API_KEY' : apikey.code,
  'Accepts':'application/json'
}
params = {
    'start' : '1',
    'limit' : '5',
    'convert': 'USD'
}
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
json = requests.get(url,params=params,headers=headers).json()
data_coin_list = json["data"]
for coin in data_coin_list:
    print(coin['symbol'], coin['quote']['USD']['price'])
    """
def CheckPrice():
    headers = {
        'X-CMC_PRO_API_KEY': apikey.code ,
        'Accepts': 'application/json'
    }
    params = {
        'start': '1' ,
        'limit': '100' ,
        'convert': 'USD'
    }
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    json = requests.get(url , params=params , headers=headers).json()
    data_coin_list = json["data"]
    for coin in data_coin_list:
        values = (coin['symbol'] ,)
        sql = """SELECT Symbol,OgBuyPrice,Amount FROM coins.coindata WHERE Symbol = %s"""
        cur.execute(sql , (values))
        result = cur.fetchone()
        if result != None:
            print(result)

    #ExectuteSqlFunc('search' , (coin['symbol']))




menu = [
'1 : ExecuteSql',
'2: CheckPriceMarket' ,
]

#print(f'Access command by line number \n {menu}')
if __name__ == '__main__':
    print(f'Access command by line number \n' + '-' * 30)
    for command in menu:
        print(command)
    CheckPrice()
    #ExectuteSqlFunc('add',None)
    #ExectuteSqlFunc('add',None)
