import pymysql
import time
import pandas as pd
def trialer():
    while 1 < 2:
        try:
            data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/BTC1m.csv')
            print('file exists')

        except FileNotFoundError:
            print('still not here, gonna wait longer, waiting five minutes')
            time.sleep(600)
            data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/BTC1m.csv')
            print('five minutes up')

        #set up the main connection
        my_conn = pymysql.connect(
            host='nibbler.cxadmpob69hk.ap-southeast-2.rds.amazonaws.com',
            port=3306,
            db='CoinData',
            user='Nibbler',
            password='Nibbler123',
            local_infile=True)
        #look at the csv file here and get last data point
        last_csv_pair_1 = data.pair_1.iloc[-1]
        last_csv_pair_2 = data.pair_2.iloc[-1]
        last_csv_Date_Time = int(data.Date_Time.iloc[-1])
        last_csv_Open_price = int(data.Open_price.iloc[-1])
        last_csv_High_price = int(data.High_price.iloc[-1])
        last_csv_Low_price = int(data.Low_price.iloc[-1])
        last_csv_Close_price = int(data.Close_price.iloc[-1])
        last_csv_Volume = int(data.Volume.iloc[-1])


        #get the last data point from the database, if it doesnt exist just remake the table
            #CREAT AN ERROR FOR THIS
            #CREATE TABLE `THETA` (
            # `id` int NOT NULL AUTO_INCREMENT,
            # `pair_1` varchar(20) NOT NULL,
            # `pair_2` varchar(20) NOT NULL,
            # `Date_Time` varchar(20)NOT NULL,
            # `Open_price` varchar(20) NULL,
            # `High_price` varchar(20) NULL,
            # `Low_price` varchar(20) NULL,
            # `Close_price` varchar(20) NULL,
            # `Volume` varchar(20) NULL,
            # PRIMARY KEY (`id`, `Date_Time`)
            # ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
        my_cursor = my_conn.cursor()
        my_cursor.execute(''' select Date_Time from BTC order by Date_Time desc limit 1; ''')
        result = my_cursor.fetchone()
        a = str(result).strip("(,)")
        try:
            result = int(float(a))
        except ValueError:
            pass
        print(result)

        my_cursor.close()
        #used for if the dataset is empty
        if result == None:
            print('result is none')
            my_cursor = my_conn.cursor()

            print('Database is empty, lets populate oooohhyeahhh')
            start1 = time.time()
            my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/BTC1m.csv' IGNORE INTO TABLE BTC
                                FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                                LINES TERMINATED BY '\r\n'
                                IGNORE 1 LINES;''')

            my_conn.commit()
            end1 = time.time()
            my_cursor.close()
            print('the database has been bleached')
            print('time to push if result = none ', end1-start1)
            new_boy = 1

            if new_boy == 1:
                while 1 < 2:
                    my_cursor = my_conn.cursor()
                    print('RESULT=NONE WHILE LOOP')
                    print('pushing new data')
                    start2 = time.time()
                    my_cursor.execute('INSERT INTO BTC VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                    end2 = time.time()
                    my_cursor.close()

                    print('the database has been updated')
                    print('result =  none while loop time', end2-start2)
                    break
        #used to append the last value
        if result != None and result != last_csv_Date_Time:
            my_cursor = my_conn.cursor()
            print('deleting, bad bad stop this +++++++++++++++++')
            my_cursor.execute('DELETE FROM BTC;')
            start3 = time.time()
            my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/BTC1m.csv' IGNORE INTO TABLE BTC
                                FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                                LINES TERMINATED BY '\r\n'
                                IGNORE 1 LINES;''')
            
            end3 = time.time()
            my_conn.commit()

            print('result doesnt equal initial push time', end3-start3)
            print('the database has been updated')
            my_cursor.execute(''' select count(*) from BTC; ''')
            result1 = my_cursor.fetchone()
            a1 = str(result1).strip("(,)")
            result1 = int(float(a1))
            d1 = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/BTC1m.csv')
            data_length = len(d1.Date_Time-1)
            print(data_length)
            print(result1)
            if result1 != len(data):
            
                my_cursor = my_conn.cursor()
                print('LOAD LOCAL FAILED, TRYING AGAIN')
                my_cursor.execute('DELETE FROM BTC;')
                start3 = time.time()
                my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/BTC1m.csv' IGNORE INTO TABLE BTC
                                    FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                                    LINES TERMINATED BY '\r\n'
                                    IGNORE 1 LINES;''')
                
                end3 = time.time()
                my_conn.commit()
            if result1 == len(data):
                while 1 < 2:
                    my_cursor = my_conn.cursor()

                    print('IN NOT EQUAL LOOP')
                    print('pushing new data')
                    start4 = time.time()
                    my_cursor.execute('INSERT INTO BTC VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                    end4 = time.time()
                    print('not equal while loop time', end4-start4)
                    my_cursor.close()
                    print('the database has been updated')
                    break
            else:
                break

            
        
        if result == last_csv_Date_Time:

               print('================================')

               print('NO NEW ENTRIES, CLOSING CONNECTION')
               print('================================')

               time.sleep(10)
               my_conn.close()
        

