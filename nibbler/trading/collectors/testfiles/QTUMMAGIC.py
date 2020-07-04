import pymysql
import time
import pandas as pd
from tqdm import tqdm
from datetime import datetime, timedelta

def QTUM():
    print('QTUMMAGIC START')
    try:
        data = pd.read_csv(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/QTUM/1m/QTUM1m.csv')
    #if the file is being populated it wont be found, thus a timeout is needed while it populates
    except FileNotFoundError:
        time.sleep(600)
        data = pd.read_csv(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/QTUM/1m/QTUM1m.csv')

        #set up the main connection
    my_conn = pymysql.connect(
        host='nibbler.cxadmpob69hk.ap-southeast-2.rds.amazonaws.com',
        port=3306,
        db='CoinData',
        user='Nibbler',
        password='Nibbler123',
        local_infile=1)

    my_cursor = my_conn.cursor()
    #selecting the last date time value from the database
    my_cursor.execute(''' select count(*) from QTUM; ''')
    result = my_cursor.fetchall()
    a = str(result).strip("(,)")
    my_cursor.close()
    try:
        result = int((a))
    except ValueError:
        pass
    print('QTUM the database length is equal to :',result)
    print('QTUM the csv length is equal to:', len(data))


    if result == 0 or result == None:
        
        print('====QTUM DATABASE IS EMPTY TIME TO POPULATE=======')


        my_cursor = my_conn.cursor()
        start1 = time.time()
        #pushing data into the database from the CSV file
        my_cursor.execute(''' LOAD DATA LOCAL INFILE '/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/QTUM/1m/QTUM1m.csv' IGNORE INTO TABLE QTUM
                            FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                            LINES TERMINATED BY '\n'
                            IGNORE 1 LINES;''')
        my_cursor.execute('SHOW WARNINGS')     

        my_conn.commit()
        end1 = time.time()
        my_cursor.close()

        my_cursor = my_conn.cursor()
        #getting the length of the database file
        my_cursor.execute(''' select COUNT(*) FROM QTUM; ''')
        Clean_results = my_cursor.fetchall()
        Clean_results = str(Clean_results).strip("(,)")
        Clean_results = int(Clean_results)
        my_cursor.close()
        print('total values pushed', Clean_results)

        print('=====PUSHED ENTIRE HISTORY IN:', end1-start1)

        if Clean_results != len(data):
            print('something went wrong, probably a datta error')
    gap = len(data) - result
    if result < len(data) and result > 0:
        print('this means we can a single value or we have a data error')
        #if the result is less than the data by one
        print('gap is equal to', gap,'therefore we need to push', gap, 'points to the database')
        #get the last 20 candles
    
        x = gap*-1
        to_push = []
        fuckyou = list(range(0,gap))
        for i in fuckyou:
            lastpoints = data.iloc[x][0], data.iloc[x][1], data.iloc[x][2], float(data.iloc[x][3]), float(data.iloc[x][4]), float(data.iloc[x][5]), float(data.iloc[x][6]), float(data.iloc[x][7])
            print(lastpoints)
            to_push.append(lastpoints)
            x = x+1
            

        y = 0
        for i in to_push:
            pair_1 = to_push[y][0]
            pair_2 = to_push[y][1]
            Date_Time = str(round(to_push[y][2], 0)) #need to change these value to equal that to the databse for each shitcoin
            Open_price = str(round(to_push[y][3], 4))
            High_price = str(round(to_push[y][4], 4))
            Low_price = str(round(to_push[y][5], 4))
            Close_price = str(round(to_push[y][6], 4))
            Volume = str(round(to_push[y][7], 4))
            y = y+1
            start2 = time.time()
            my_cursor = my_conn.cursor()
            my_cursor.execute('INSERT INTO QTUM VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (pair_1, pair_2, Date_Time, Open_price, High_price, Low_price, Close_price, Volume))
            my_conn.commit()
            end2 = time.time()

    if result > len(data):
        print('somQTUMing went wrong, database is somehow longer than the csv, deleting all')
        my_cursor = my_conn.cursor()
        my_cursor.execute(''' DELETE FROM QTUM; ''')
        my_conn.commit()
        my_cursor.close()
        print('data has been wiped, will repopulate next update')
    if result == len(data):

        print('SAME LENGTH DO NOTHING')

    print('QTUMMAGIC DONE')

QTUM()