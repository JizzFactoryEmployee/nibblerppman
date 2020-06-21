# import the module
import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd
import time
import pymysql
def HIGHENERGY():
    while True: 
        start = time.time()
        data = pd.read_csv(r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\THETA1m.csv')
        length = len(data)
        # create sqlalchemy engine
        engine = create_engine("mysql+pymysql://{user}:{pw}@nibbler.cxadmpob69hk.ap-southeast-2.rds.amazonaws.com/{db}"
                            .format(user="Nibbler",
                                    pw="Nibbler123",
                                    db="CoinData"))

        try:
            sql = "SELECT * FROM THETA"


        except pymysql.err.ProgrammingError:
            
            sql = '''CREATE TABLE `THETA` (
            `id` int NOT NULL,
            `pair_1` text NOT NULL,
            `pair_2` text NOT NULL,
            `Date_Time` double NOT NULL,
            `Open_price` double  NULL,
            `High_price` double  NULL,
            `Low_price` double  NULL,
            `Close_price` double  NULL,
            `Volume` double  NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
            SELECT * FROM THETA;
            '''
        old_results = pd.read_sql(sql, engine.connect())
        a = data.Date_Time.iloc[-1]
        b= 0
        try:
            b = old_results.Date_Time.iloc[-1]
        except IndexError:
            pass

        while 1 <2:
            if b != a:
                print('old does not equal new, starting the pushy-pushy-bot')

                data.to_sql('THETA', con = engine, if_exists = 'replace', index=False)

                end = time.time()
                print('CSV had:', length*8, 'points', length, 'per column')
                speedyboi = end-start
                print('Time to push BTC1m took:',speedyboi)
                print('pushypushy-bot pushed',length*8/speedyboi, 'data points per second')
                break   
            else:
                print('nothing new')
                break

import mysql.connector
from mysql.connector.constants import ClientFlag
def inlinepush():
    while 1 < 2 : 
        data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/THETA1m.csv')
        
        length = len(data.Date_Time)

        my_conn = pymysql.connect(
            host='nibbler.cxadmpob69hk.ap-southeast-2.rds.amazonaws.com',
            port=3306,
            db='CoinData',
            user='Nibbler',
            password='Nibbler123',
            local_infile=True
        )

        my_cursor = my_conn.cursor()
        my_cursor.execute('select Date_Time from THETA order by Date_Time;')
        result = my_cursor.fetchone()
        csv_last =  data.Date_Time.iloc[-1]

        a = str(result)
        b = ''.join(i for i in a if i.isdigit())
        dataframe_last = 0

        try:
            dataframe_last = int(b)

        except ValueError:
            time.sleep(10)
            dataframe_last = int(b)


        while 1 < 2:

            if dataframe_last != csv_last:
                print('old doesnt equal new, starting pushy-pushy-2.0')
                my_cursor.execute('DROP TABLE IF EXISTS `THETA`;')
                my_cursor.execute('''CREATE TABLE `THETA`(
                                    `pair_1` varchar(20) NOT NULL,
                                    `pair_2` varchar(20) NOT NULL,
                                    `Date_Time` decimal(15,0)NOT NULL,
                                    `Open_price` varchar(20) NULL,
                                    `High_price` varchar(20) NULL,
                                    `Low_price` varchar(20) NULL,
                                    `Close_price` varchar(20) NULL,
                                    `Volume` varchar(20) NULL
                                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;''')
                start = time.time()

                my_cursor.execute(''' 
                                    LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/THETA1m.csv' INTO TABLE THETA FIELDS TERMINATED BY ',' IGNORE 1 LINES
                                ''')
                my_conn.commit()
                end = time.time()
                speedyboi = end-start
                print('Time to push THETA took:',speedyboi)
                print('pushypushy-bot pushed',length*8/speedyboi, 'data points per second')
                break
            else:
                print('nothing new, destroying connection')
                my_conn.close()
                time.sleep(10)

    

inlinepush()