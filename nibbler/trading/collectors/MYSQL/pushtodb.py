import pymysql
import csv
import pandas as pd 
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class CSVpusher():
   def BTCpush():
      while 1 < 2:
        try:
            data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/BTC1m.csv')
            print('file exists')

        except FileNotFoundError: 
            print('file not here yet')
         #takes about 8 minutes for BTC, with 40k points, set it to 10 mins just in case
            time.sleep(600)
            data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/BTC1m.csv')
            print('file is here maybe')
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
            my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/BTC1m.csv' INTO TABLE BTC
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
            print('result doesnt equal none, gonna push the data')
            my_cursor = my_conn.cursor()
            my_cursor.execute('DELETE FROM BTC;')
            start3 = time.time()
            my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/BTC1m.csv' INTO TABLE BTC
                                FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                                LINES TERMINATED BY '\r\n'
                                IGNORE 1 LINES;''')
            end3 = time.time()
            my_conn.commit()
            my_cursor.close()
            print('result doesnt equal initial push time', end3-start3)
            print('the database has been updated')
            new_boy = 1

            if new_boy == 1:
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

        
        
        if result == last_csv_Date_Time:

               print('================================')

               print('NO NEW ENTRIES, CLOSING CONNECTION')
               print('================================')

               time.sleep(10)
               my_conn.close()      
   def ETHpush():
      while 1 < 2:
            try:
                  data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/ETH1m.csv')
                  print('file exists')

            except FileNotFoundError: 
                  print('file not here yet')

                  time.sleep(600)
                  data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/ETH1m.csv')
                  print('file is here maybe')
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
            my_cursor.execute(''' select Date_Time from ETH order by Date_Time desc limit 1; ''')
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
                  my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/ETH1m.csv' INTO TABLE ETH
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
                        my_cursor.execute('INSERT INTO ETH VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                        end2 = time.time()
                        my_cursor.close()

                        print('the database has been updated')
                        print('result =  none while loop time', end2-start2)
                        break
            #used to append the last value
            if result != None and result != last_csv_Date_Time:
                  print('result doesnt equal none, gonna push the data')
                  my_cursor = my_conn.cursor()
                  my_cursor.execute('DELETE FROM ETH;')
                  start3 = time.time()
                  my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/ETH1m.csv' INTO TABLE ETH
                                    FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                                    LINES TERMINATED BY '\r\n'
                                    IGNORE 1 LINES;''')
                  end3 = time.time()
                  my_conn.commit()
                  my_cursor.close()
                  print('result doesnt equal initial push time', end3-start3)
                  print('the database has been updated')
                  new_boy = 1

                  if new_boy == 1:
                     while 1 < 2:
                        my_cursor = my_conn.cursor()

                        print('IN NOT EQUAL LOOP')
                        print('pushing new data')
                        start4 = time.time()
                        my_cursor.execute('INSERT INTO ETH VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                        end4 = time.time()
                        print('not equal while loop time', end4-start4)
                        my_cursor.close()

                        print('the database has been updated')
                        break

            
            
            if result == last_csv_Date_Time:

                     print('================================')

                     print('NO NEW ENTRIES, CLOSING CONNECTION')
                     print('================================')

                     time.sleep(10)
                     my_conn.close()
   def ADApush():
      while 1 < 2:
            try:
                  data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/ADA1m.csv')
                  print('file exists')

            except FileNotFoundError: 
               print('file not here yet')

               time.sleep(300)
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/ADA1m.csv')
               print('file is here maybe')

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
            my_cursor.execute(''' select Date_Time from ADA order by Date_Time desc limit 1; ''')
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
                  my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/ADA1m.csv' INTO TABLE ADA
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
                        my_cursor.execute('INSERT INTO ADA VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                        end2 = time.time()
                        my_cursor.close()

                        print('the database has been updated')
                        print('result =  none while loop time', end2-start2)
                        break
            #used to append the last value
            if result != None and result != last_csv_Date_Time:
                  print('result doesnt equal none, gonna push the data')
                  my_cursor = my_conn.cursor()
                  my_cursor.execute('DELETE FROM ADA;')
                  start3 = time.time()
                  my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/ADA1m.csv' INTO TABLE ADA
                                    FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                                    LINES TERMINATED BY '\r\n'
                                    IGNORE 1 LINES;''')
                  end3 = time.time()
                  my_conn.commit()
                  my_cursor.close()
                  print('result doesnt equal initial push time', end3-start3)
                  print('the database has been updated')
                  new_boy = 1

                  if new_boy == 1:
                     while 1 < 2:
                        my_cursor = my_conn.cursor()

                        print('IN NOT EQUAL LOOP')
                        print('pushing new data')
                        start4 = time.time()
                        my_cursor.execute('INSERT INTO ADA VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                        end4 = time.time()
                        print('not equal while loop time', end4-start4)
                        my_cursor.close()

                        print('the database has been updated')
                        break

            
            
            if result == last_csv_Date_Time:

                     print('================================')

                     print('NO NEW ENTRIES, CLOSING CONNECTION')
                     print('================================')

                     time.sleep(10)
                     my_conn.close()
   def ATOMpush():
         while 1 < 2:
               try:
                     data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/ATOM1m.csv')
                     print('file exists')

               except FileNotFoundError: 
                     print('file not here yet')

                     time.sleep(300)
                     data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/ATOM1m.csv')
                     print('file is here maybe')
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
               my_cursor.execute(''' select Date_Time from ATOM order by Date_Time desc limit 1; ''')
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
                     my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/ATOM1m.csv' INTO TABLE ATOM
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
                           my_cursor.execute('INSERT INTO ATOM VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                           end2 = time.time()
                           my_cursor.close()

                           print('the database has been updated')
                           print('result =  none while loop time', end2-start2)
                           break
               #used to append the last value
               if result != None and result != last_csv_Date_Time:
                     print('result doesnt equal none, gonna push the data')
                     my_cursor = my_conn.cursor()
                     my_cursor.execute('DELETE FROM ATOM;')
                     start3 = time.time()
                     my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/ATOM1m.csv' INTO TABLE ATOM
                                       FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                                       LINES TERMINATED BY '\r\n'
                                       IGNORE 1 LINES;''')
                     end3 = time.time()
                     my_conn.commit()
                     my_cursor.close()
                     print('result doesnt equal initial push time', end3-start3)
                     print('the database has been updated')
                     new_boy = 1

                     if new_boy == 1:
                        while 1 < 2:
                           my_cursor = my_conn.cursor()

                           print('IN NOT EQUAL LOOP')
                           print('pushing new data')
                           start4 = time.time()
                           my_cursor.execute('INSERT INTO ATOM VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                           end4 = time.time()
                           print('not equal while loop time', end4-start4)
                           my_cursor.close()

                           print('the database has been updated')
                           break

               
               
               if result == last_csv_Date_Time:

                        print('================================')

                        print('NO NEW ENTRIES, CLOSING CONNECTION')
                        print('================================')

                        time.sleep(10)
                        my_conn.close()
   def BATpush():
         while 1 < 2:
               try:
                     data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/BAT1m.csv')
                     print('file exists')

               except FileNotFoundError: 
                     print('file not here yet')

                     time.sleep(300)
                     data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/BAT1m.csv')
                     print('file is here maybe')
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
               my_cursor.execute(''' select Date_Time from BAT order by Date_Time desc limit 1; ''')
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
                     my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/BAT1m.csv' INTO TABLE BAT
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
                           my_cursor.execute('INSERT INTO BAT VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                           end2 = time.time()
                           my_cursor.close()

                           print('the database has been updated')
                           print('result =  none while loop time', end2-start2)
                           break
               #used to append the last value
               if result != None and result != last_csv_Date_Time:
                     print('result doesnt equal none, gonna push the data')
                     my_cursor = my_conn.cursor()
                     my_cursor.execute('DELETE FROM BAT;')
                     start3 = time.time()
                     my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/BAT1m.csv' INTO TABLE BAT
                                       FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                                       LINES TERMINATED BY '\r\n'
                                       IGNORE 1 LINES;''')
                     end3 = time.time()
                     my_conn.commit()
                     my_cursor.close()
                     print('result doesnt equal initial push time', end3-start3)
                     print('the database has been updated')
                     new_boy = 1

                     if new_boy == 1:
                        while 1 < 2:
                           my_cursor = my_conn.cursor()

                           print('IN NOT EQUAL LOOP')
                           print('pushing new data')
                           start4 = time.time()
                           my_cursor.execute('INSERT INTO BAT VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                           end4 = time.time()
                           print('not equal while loop time', end4-start4)
                           my_cursor.close()

                           print('the database has been updated')
                           break

               
               
               if result == last_csv_Date_Time:

                        print('================================')

                        print('NO NEW ENTRIES, CLOSING CONNECTION')
                        print('================================')

                        time.sleep(10)
                        my_conn.close()
   def BCHpush():
      while 1 < 2:
            try:
                  data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/BCH1m.csv')
                  print('file exists')

            except FileNotFoundError: 
                  print('file not here yet')

                  time.sleep(300)
                  data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/BCH1m.csv')
                  print('file is here maybe')
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
            my_cursor.execute(''' select Date_Time from BCH order by Date_Time desc limit 1; ''')
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
                  my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/BCH1m.csv' INTO TABLE BCH
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
                        my_cursor.execute('INSERT INTO BCH VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                        end2 = time.time()
                        my_cursor.close()

                        print('the database has been updated')
                        print('result =  none while loop time', end2-start2)
                        break
            #used to append the last value
            if result != None and result != last_csv_Date_Time:
                  print('result doesnt equal none, gonna push the data')
                  my_cursor = my_conn.cursor()
                  my_cursor.execute('DELETE FROM BCH;')
                  start3 = time.time()
                  my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/BCH1m.csv' INTO TABLE BCH
                                    FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                                    LINES TERMINATED BY '\r\n'
                                    IGNORE 1 LINES;''')
                  end3 = time.time()
                  my_conn.commit()
                  my_cursor.close()
                  print('result doesnt equal initial push time', end3-start3)
                  print('the database has been updated')
                  new_boy = 1

                  if new_boy == 1:
                     while 1 < 2:
                        my_cursor = my_conn.cursor()

                        print('IN NOT EQUAL LOOP')
                        print('pushing new data')
                        start4 = time.time()
                        my_cursor.execute('INSERT INTO BCH VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                        end4 = time.time()
                        print('not equal while loop time', end4-start4)
                        my_cursor.close()

                        print('the database has been updated')
                        break

            
            
            if result == last_csv_Date_Time:

                     print('================================')

                     print('NO NEW ENTRIES, CLOSING CONNECTION')
                     print('================================')

                     time.sleep(10)
                     my_conn.close()
   def BNBpush():
      while 1 < 2:
         try:
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/BNB1m.csv')
               print('file exists')

         except FileNotFoundError: 
               print('file not here yet')

               time.sleep(300)
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/BNB1m.csv')
               print('file is here maybe')
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
               #  CREATE TABLE `THETA` (
               #  `pair_1` varchar(20) NOT NULL,
               #  `pair_2` varchar(20) NOT NULL,
               #  `Date_Time` double NOT NULL,
               #  `Open_price` varchar(20) NULL,
               #  `High_price` varchar(20) NULL,
               #  `Low_price` varchar(20) NULL,
               #  `Close_price` varchar(20) NULL,
               #  `Volume` varchar(20) NULL
               #  ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
         my_cursor = my_conn.cursor()
         my_cursor.execute(''' select Date_Time from BNB order by Date_Time desc limit 1; ''')
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
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/BNB1m.csv' INTO TABLE BNB
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
                     my_cursor.execute('INSERT INTO BNB VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end2 = time.time()
                     my_cursor.close()

                     print('the database has been updated')
                     print('result =  none while loop time', end2-start2)
                     break
         #used to append the last value
         if result != None and result != last_csv_Date_Time:
               print('result doesnt equal none, gonna push the data')
               my_cursor = my_conn.cursor()
               my_cursor.execute('DELETE FROM BNB;')
               start3 = time.time()
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/BNB1m.csv' INTO TABLE BNB
                                 FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                                 LINES TERMINATED BY '\r\n'
                                 IGNORE 1 LINES;''')
               end3 = time.time()
               my_conn.commit()
               my_cursor.close()
               print('result doesnt equal initial push time', end3-start3)
               print('the database has been updated')
               new_boy = 1

               if new_boy == 1:
                  while 1 < 2:
                     my_cursor = my_conn.cursor()

                     print('IN NOT EQUAL LOOP')
                     print('pushing new data')
                     start4 = time.time()
                     my_cursor.execute('INSERT INTO BNB VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end4 = time.time()
                     print('not equal while loop time', end4-start4)
                     my_cursor.close()

                     print('the database has been updated')
                     break

         
         
         if result == last_csv_Date_Time:

                  print('================================')

                  print('NO NEW ENTRIES, CLOSING CONNECTION')
                  print('================================')

                  time.sleep(10)
                  my_conn.close()
   def DASHpush():
      while 1 < 2:
         try:
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/DASH1m.csv')
               print('file exists')

         except FileNotFoundError: 
               print('file not here yet')

               time.sleep(300)
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/DASH1m.csv')
               print('file is here maybe')
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
               #  CREATE TABLE `THETA` (
               #  `pair_1` varchar(20) NOT NULL,
               #  `pair_2` varchar(20) NOT NULL,
               #  `Date_Time` double NOT NULL,
               #  `Open_price` varchar(20) NULL,
               #  `High_price` varchar(20) NULL,
               #  `Low_price` varchar(20) NULL,
               #  `Close_price` varchar(20) NULL,
               #  `Volume` varchar(20) NULL
               #  ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
         my_cursor = my_conn.cursor()
         my_cursor.execute(''' select Date_Time from DASH order by Date_Time desc limit 1; ''')
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
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/DASH1m.csv' INTO TABLE DASH
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
                     my_cursor.execute('INSERT INTO DASH VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end2 = time.time()
                     my_cursor.close()

                     print('the database has been updated')
                     print('result =  none while loop time', end2-start2)
                     break
         #used to append the last value
         if result != None and result != last_csv_Date_Time:
               print('result doesnt equal none, gonna push the data')
               my_cursor = my_conn.cursor()
               my_cursor.execute('DELETE FROM DASH;')
               start3 = time.time()
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/DASH1m.csv' INTO TABLE DASH
                                 FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                                 LINES TERMINATED BY '\r\n'
                                 IGNORE 1 LINES;''')
               end3 = time.time()
               my_conn.commit()
               my_cursor.close()
               print('result doesnt equal initial push time', end3-start3)
               print('the database has been updated')
               new_boy = 1

               if new_boy == 1:
                  while 1 < 2:
                     my_cursor = my_conn.cursor()

                     print('IN NOT EQUAL LOOP')
                     print('pushing new data')
                     start4 = time.time()
                     my_cursor.execute('INSERT INTO DASH VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end4 = time.time()
                     print('not equal while loop time', end4-start4)
                     my_cursor.close()

                     print('the database has been updated')
                     break

         
         
         if result == last_csv_Date_Time:

               print('================================')

               print('NO NEW ENTRIES, CLOSING CONNECTION')
               print('================================')

               time.sleep(10)
               my_conn.close()
   def EOSpush():
      while 1 < 2:
         try:
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/EOS1m.csv')
               print('file exists')

         except FileNotFoundError: 
               print('file not here yet')

               time.sleep(600)
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/EOS1m.csv')
               print('file is here maybe')
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
               #  CREATE TABLE `THETA` (
               #  `pair_1` varchar(20) NOT NULL,
               #  `pair_2` varchar(20) NOT NULL,
               #  `Date_Time` double NOT NULL,
               #  `Open_price` varchar(20) NULL,
               #  `High_price` varchar(20) NULL,
               #  `Low_price` varchar(20) NULL,
               #  `Close_price` varchar(20) NULL,
               #  `Volume` varchar(20) NULL
               #  ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
         my_cursor = my_conn.cursor()
         my_cursor.execute(''' select Date_Time from EOS order by Date_Time desc limit 1; ''')
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
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/EOS1m.csv' INTO TABLE EOS
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
                     my_cursor.execute('INSERT INTO EOS VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end2 = time.time()
                     my_cursor.close()

                     print('the database has been updated')
                     print('result =  none while loop time', end2-start2)
                     break
         #used to append the last value
         if result != None and result != last_csv_Date_Time:
               print('result doesnt equal none, gonna push the data')
               my_cursor = my_conn.cursor()
               my_cursor.execute('DELETE FROM EOS;')
               start3 = time.time()
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/EOS1m.csv' INTO TABLE EOS
                                 FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                                 LINES TERMINATED BY '\r\n'
                                 IGNORE 1 LINES;''')
               end3 = time.time()
               my_conn.commit()
               my_cursor.close()
               print('result doesnt equal initial push time', end3-start3)
               print('the database has been updated')
               new_boy = 1

               if new_boy == 1:
                  while 1 < 2:
                     my_cursor = my_conn.cursor()

                     print('IN NOT EQUAL LOOP')
                     print('pushing new data')
                     start4 = time.time()
                     my_cursor.execute('INSERT INTO EOS VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end4 = time.time()
                     print('not equal while loop time', end4-start4)
                     my_cursor.close()

                     print('the database has been updated')
                     break

         
         
         if result == last_csv_Date_Time:

               print('================================')

               print('NO NEW ENTRIES, CLOSING CONNECTION')
               print('================================')

               time.sleep(10)
               my_conn.close()
   def ETCpush():
      while 1 < 2:
         try:
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/ETC1m.csv')
               print('file exists')

         except FileNotFoundError: 
               print('file not here yet')

               time.sleep(300)
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/ETC1m.csv')
               print('file is here maybe')
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
               #  CREATE TABLE `THETA` (
               #  `pair_1` varchar(20) NOT NULL,
               #  `pair_2` varchar(20) NOT NULL,
               #  `Date_Time` double NOT NULL,
               #  `Open_price` varchar(20) NULL,
               #  `High_price` varchar(20) NULL,
               #  `Low_price` varchar(20) NULL,
               #  `Close_price` varchar(20) NULL,
               #  `Volume` varchar(20) NULL
               #  ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
         my_cursor = my_conn.cursor()
         my_cursor.execute(''' select Date_Time from ETC order by Date_Time desc limit 1; ''')
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
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/ETC1m.csv' INTO TABLE ETC
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
                     my_cursor.execute('INSERT INTO ETC VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end2 = time.time()
                     my_cursor.close()

                     print('the database has been updated')
                     print('result =  none while loop time', end2-start2)
                     break
         #used to append the last value
         if result != None and result != last_csv_Date_Time:
               print('result doesnt equal none, gonna push the data')
               my_cursor = my_conn.cursor()
               my_cursor.execute('DELETE FROM ETC;')
               start3 = time.time()
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/ETC1m.csv' INTO TABLE ETC
                                 FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                                 LINES TERMINATED BY '\r\n'
                                 IGNORE 1 LINES;''')
               end3 = time.time()
               my_conn.commit()
               my_cursor.close()
               print('result doesnt equal initial push time', end3-start3)
               print('the database has been updated')
               new_boy = 1

               if new_boy == 1:
                  while 1 < 2:
                     my_cursor = my_conn.cursor()

                     print('IN NOT EQUAL LOOP')
                     print('pushing new data')
                     start4 = time.time()
                     my_cursor.execute('INSERT INTO ETC VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end4 = time.time()
                     print('not equal while loop time', end4-start4)
                     my_cursor.close()

                     print('the database has been updated')
                     break

         
         
         if result == last_csv_Date_Time:

               print('================================')

               print('NO NEW ENTRIES, CLOSING CONNECTION')
               print('================================')

               time.sleep(10)
               my_conn.close()
   def IOTApush():
      while 1 < 2:
         try:
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/IOTA1m.csv')
               print('file exists')

         except FileNotFoundError: 
               print('file not here yet')

               time.sleep(300)
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/IOTA1m.csv')
               print('file is here maybe')
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
               #  CREATE TABLE `THETA` (
               #  `pair_1` varchar(20) NOT NULL,
               #  `pair_2` varchar(20) NOT NULL,
               #  `Date_Time` double NOT NULL,
               #  `Open_price` varchar(20) NULL,
               #  `High_price` varchar(20) NULL,
               #  `Low_price` varchar(20) NULL,
               #  `Close_price` varchar(20) NULL,
               #  `Volume` varchar(20) NULL
               #  ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
         my_cursor = my_conn.cursor()
         my_cursor.execute(''' select Date_Time from IOTA order by Date_Time desc limit 1; ''')
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
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/IOTA1m.csv' INTO TABLE IOTA
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
                     my_cursor.execute('INSERT INTO IOTA VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end2 = time.time()
                     my_cursor.close()

                     print('the database has been updated')
                     print('result =  none while loop time', end2-start2)
                     break
         #used to append the last value
         if result != None and result != last_csv_Date_Time:
               print('result doesnt equal none, gonna push the data')
               my_cursor = my_conn.cursor()
               my_cursor.execute('DELETE FROM IOTA;')
               start3 = time.time()
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/IOTA1m.csv' INTO TABLE IOTA
                                 FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                                 LINES TERMINATED BY '\r\n'
                                 IGNORE 1 LINES;''')
               end3 = time.time()
               my_conn.commit()
               my_cursor.close()
               print('result doesnt equal initial push time', end3-start3)
               print('the database has been updated')
               new_boy = 1

               if new_boy == 1:
                  while 1 < 2:
                     my_cursor = my_conn.cursor()

                     print('IN NOT EQUAL LOOP')
                     print('pushing new data')
                     start4 = time.time()
                     my_cursor.execute('INSERT INTO IOTA VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end4 = time.time()
                     print('not equal while loop time', end4-start4)
                     my_cursor.close()

                     print('the database has been updated')
                     break

         
         
         if result == last_csv_Date_Time:

               print('================================')

               print('NO NEW ENTRIES, CLOSING CONNECTION')
               print('================================')

               time.sleep(10)
               my_conn.close()
     
   def IOSTpush():
      while 1 < 2:
         try:
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/IOST1m.csv')
               print('file exists')

         except FileNotFoundError: 
               print('file not here yet')

               time.sleep(300)
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/IOST1m.csv')
               print('file is here maybe')
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
               #  CREATE TABLE `THETA` (
               #  `pair_1` varchar(20) NOT NULL,
               #  `pair_2` varchar(20) NOT NULL,
               #  `Date_Time` double NOT NULL,
               #  `Open_price` varchar(20) NULL,
               #  `High_price` varchar(20) NULL,
               #  `Low_price` varchar(20) NULL,
               #  `Close_price` varchar(20) NULL,
               #  `Volume` varchar(20) NULL
               #  ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
         my_cursor = my_conn.cursor()
         my_cursor.execute(''' select Date_Time from IOST order by Date_Time desc limit 1; ''')
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
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/IOST1m.csv' INTO TABLE IOST
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
                     my_cursor.execute('INSERT INTO IOST VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end2 = time.time()
                     my_cursor.close()

                     print('the database has been updated')
                     print('result =  none while loop time', end2-start2)
                     break
         #used to append the last value
         if result != None and result != last_csv_Date_Time:
               print('result doesnt equal none, gonna push the data')
               my_cursor = my_conn.cursor()
               my_cursor.execute('DELETE FROM IOST;')
               start3 = time.time()
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/IOST1m.csv' INTO TABLE IOST
                                 FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                                 LINES TERMINATED BY '\r\n'
                                 IGNORE 1 LINES;''')
               end3 = time.time()
               my_conn.commit()
               my_cursor.close()
               print('result doesnt equal initial push time', end3-start3)
               print('the database has been updated')
               new_boy = 1

               if new_boy == 1:
                  while 1 < 2:
                     my_cursor = my_conn.cursor()

                     print('IN NOT EQUAL LOOP')
                     print('pushing new data')
                     start4 = time.time()
                     my_cursor.execute('INSERT INTO IOST VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end4 = time.time()
                     print('not equal while loop time', end4-start4)
                     my_cursor.close()

                     print('the database has been updated')
                     break

         
         
         if result == last_csv_Date_Time:

               print('================================')

               print('NO NEW ENTRIES, CLOSING CONNECTION')
               print('================================')

               time.sleep(10)
               my_conn.close()
    
   def LINKpush():
      while 1 < 2:
         try:
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/LINK1m.csv')
               print('file exists')

         except FileNotFoundError: 
               print('file not here yet')

               time.sleep(300)
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/LINK1m.csv')
               print('file is here maybe')
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
               #  CREATE TABLE `THETA` (
               #  `pair_1` varchar(20) NOT NULL,
               #  `pair_2` varchar(20) NOT NULL,
               #  `Date_Time` double NOT NULL,
               #  `Open_price` varchar(20) NULL,
               #  `High_price` varchar(20) NULL,
               #  `Low_price` varchar(20) NULL,
               #  `Close_price` varchar(20) NULL,
               #  `Volume` varchar(20) NULL
               #  ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
         my_cursor = my_conn.cursor()
         my_cursor.execute(''' select Date_Time from LINK order by Date_Time desc limit 1; ''')
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
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/LINK1m.csv' INTO TABLE LINK
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
                     my_cursor.execute('INSERT INTO LINK VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end2 = time.time()
                     my_cursor.close()

                     print('the database has been updated')
                     print('result =  none while loop time', end2-start2)
                     break
         #used to append the last value
         if result != None and result != last_csv_Date_Time:
               print('result doesnt equal none, gonna push the data')
               my_cursor = my_conn.cursor()
               my_cursor.execute('DELETE FROM LINK;')
               start3 = time.time()
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/LINK1m.csv' INTO TABLE LINK
                                 FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                                 LINES TERMINATED BY '\r\n'
                                 IGNORE 1 LINES;''')
               end3 = time.time()
               my_conn.commit()
               my_cursor.close()
               print('result doesnt equal initial push time', end3-start3)
               print('the database has been updated')
               new_boy = 1

               if new_boy == 1:
                  while 1 < 2:
                     my_cursor = my_conn.cursor()

                     print('IN NOT EQUAL LOOP')
                     print('pushing new data')
                     start4 = time.time()
                     my_cursor.execute('INSERT INTO LINK VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end4 = time.time()
                     print('not equal while loop time', end4-start4)
                     my_cursor.close()

                     print('the database has been updated')
                     break

         
         
         if result == last_csv_Date_Time:

               print('================================')

               print('NO NEW ENTRIES, CLOSING CONNECTION')
               print('================================')

               time.sleep(10)
               my_conn.close()
   def LTCpush():
      while 1 < 2:
         try:
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/LTC1m.csv')
               print('file exists')

         except FileNotFoundError: 
               print('file not here yet')

               time.sleep(300)
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/LTC1m.csv')
               print('file is here maybe')
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
               #  CREATE TABLE `THETA` (
               #  `pair_1` varchar(20) NOT NULL,
               #  `pair_2` varchar(20) NOT NULL,
               #  `Date_Time` double NOT NULL,
               #  `Open_price` varchar(20) NULL,
               #  `High_price` varchar(20) NULL,
               #  `Low_price` varchar(20) NULL,
               #  `Close_price` varchar(20) NULL,
               #  `Volume` varchar(20) NULL
               #  ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
         my_cursor = my_conn.cursor()
         my_cursor.execute(''' select Date_Time from LTC order by Date_Time desc limit 1; ''')
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
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/LTC1m.csv' INTO TABLE LTC
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
                     my_cursor.execute('INSERT INTO LTC VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end2 = time.time()
                     my_cursor.close()

                     print('the database has been updated')
                     print('result =  none while loop time', end2-start2)
                     break
         #used to append the last value
         if result != None and result != last_csv_Date_Time:
               print('result doesnt equal none, gonna push the data')
               my_cursor = my_conn.cursor()
               my_cursor.execute('DELETE FROM LTC;')
               start3 = time.time()
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/LTC1m.csv' INTO TABLE LTC
                                 FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                                 LINES TERMINATED BY '\r\n'
                                 IGNORE 1 LINES;''')
               end3 = time.time()
               my_conn.commit()
               my_cursor.close()
               print('result doesnt equal initial push time', end3-start3)
               print('the database has been updated')
               new_boy = 1

               if new_boy == 1:
                  while 1 < 2:
                     my_cursor = my_conn.cursor()

                     print('IN NOT EQUAL LOOP')
                     print('pushing new data')
                     start4 = time.time()
                     my_cursor.execute('INSERT INTO LTC VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end4 = time.time()
                     print('not equal while loop time', end4-start4)
                     my_cursor.close()

                     print('the database has been updated')
                     break

         
         
         if result == last_csv_Date_Time:

               print('================================')

               print('NO NEW ENTRIES, CLOSING CONNECTION')
               print('================================')

               time.sleep(10)
               my_conn.close()
   def NEOpush():
      while 1 < 2:
         try:
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/NEO1m.csv')
               print('file exists')

         except FileNotFoundError: 
               print('file not here yet')

               time.sleep(300)
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/NEO1m.csv')
               print('file is here maybe')
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
               #  CREATE TABLE `THETA` (
               #  `pair_1` varchar(20) NOT NULL,
               #  `pair_2` varchar(20) NOT NULL,
               #  `Date_Time` double NOT NULL,
               #  `Open_price` varchar(20) NULL,
               #  `High_price` varchar(20) NULL,
               #  `Low_price` varchar(20) NULL,
               #  `Close_price` varchar(20) NULL,
               #  `Volume` varchar(20) NULL
               #  ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
         my_cursor = my_conn.cursor()
         my_cursor.execute(''' select Date_Time from NEO order by Date_Time desc limit 1; ''')
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
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/NEO1m.csv' INTO TABLE NEO
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
                     my_cursor.execute('INSERT INTO NEO VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end2 = time.time()
                     my_cursor.close()

                     print('the database has been updated')
                     print('result =  none while loop time', end2-start2)
                     break
         #used to append the last value
         if result != None and result != last_csv_Date_Time:
               print('result doesnt equal none, gonna push the data')
               my_cursor = my_conn.cursor()
               my_cursor.execute('DELETE FROM NEO;')
               start3 = time.time()
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/NEO1m.csv' INTO TABLE NEO
                                 FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                                 LINES TERMINATED BY '\r\n'
                                 IGNORE 1 LINES;''')
               end3 = time.time()
               my_conn.commit()
               my_cursor.close()
               print('result doesnt equal initial push time', end3-start3)
               print('the database has been updated')
               new_boy = 1

               if new_boy == 1:
                  while 1 < 2:
                     my_cursor = my_conn.cursor()

                     print('IN NOT EQUAL LOOP')
                     print('pushing new data')
                     start4 = time.time()
                     my_cursor.execute('INSERT INTO NEO VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end4 = time.time()
                     print('not equal while loop time', end4-start4)
                     my_cursor.close()

                     print('the database has been updated')
                     break

         
         
         if result == last_csv_Date_Time:

               print('================================')

               print('NO NEW ENTRIES, CLOSING CONNECTION')
               print('================================')

               time.sleep(10)
               my_conn.close()
     
   def ONTpush():
      while 1 < 2:
         try:
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/ONT1m.csv')
               print('file exists')

         except FileNotFoundError: 
               print('file not here yet')

               time.sleep(300)
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/ONTm.csv')
               print('file is here maybe')
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
               #  CREATE TABLE `THETA` (
               #  `pair_1` varchar(20) NOT NULL,
               #  `pair_2` varchar(20) NOT NULL,
               #  `Date_Time` double NOT NULL,
               #  `Open_price` varchar(20) NULL,
               #  `High_price` varchar(20) NULL,
               #  `Low_price` varchar(20) NULL,
               #  `Close_price` varchar(20) NULL,
               #  `Volume` varchar(20) NULL
               #  ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
         my_cursor = my_conn.cursor()
         my_cursor.execute(''' select Date_Time from ONT order by Date_Time desc limit 1; ''')
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
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/ONT1m.csv' INTO TABLE ONT
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
                     my_cursor.execute('INSERT INTO ONT VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end2 = time.time()
                     my_cursor.close()

                     print('the database has been updated')
                     print('result =  none while loop time', end2-start2)
                     break
         #used to append the last value
         if result != None and result != last_csv_Date_Time:
               print('result doesnt equal none, gonna push the data')
               my_cursor = my_conn.cursor()
               my_cursor.execute('DELETE FROM ONT;')
               start3 = time.time()
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/ONT1m.csv' INTO TABLE ONT
                                 FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                                 LINES TERMINATED BY '\r\n'
                                 IGNORE 1 LINES;''')
               end3 = time.time()
               my_conn.commit()
               my_cursor.close()
               print('result doesnt equal initial push time', end3-start3)
               print('the database has been updated')
               new_boy = 1

               if new_boy == 1:
                  while 1 < 2:
                     my_cursor = my_conn.cursor()

                     print('IN NOT EQUAL LOOP')
                     print('pushing new data')
                     start4 = time.time()
                     my_cursor.execute('INSERT INTO ONT VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end4 = time.time()
                     print('not equal while loop time', end4-start4)
                     my_cursor.close()

                     print('the database has been updated')
                     break

         
         
         if result == last_csv_Date_Time:

                  print('================================')

                  print('NO NEW ENTRIES, CLOSING CONNECTION')
                  print('================================')

                  time.sleep(10)
                  my_conn.close()
      
   def QTUMpush():
      while 1 < 2:
         try:
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/QTUM1m.csv')
               print('file exists')

         except FileNotFoundError: 
               print('file not here yet')

               time.sleep(300)
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/QTUM1m.csv')
               print('file is here maybe')
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
               #  CREATE TABLE `THETA` (
               #  `pair_1` varchar(20) NOT NULL,
               #  `pair_2` varchar(20) NOT NULL,
               #  `Date_Time` double NOT NULL,
               #  `Open_price` varchar(20) NULL,
               #  `High_price` varchar(20) NULL,
               #  `Low_price` varchar(20) NULL,
               #  `Close_price` varchar(20) NULL,
               #  `Volume` varchar(20) NULL
               #  ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
         my_cursor = my_conn.cursor()
         my_cursor.execute(''' select Date_Time from QTUM order by Date_Time desc limit 1; ''')
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
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/QTUM1m.csv' INTO TABLE QTUM
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
                     my_cursor.execute('INSERT INTO QTUM VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end2 = time.time()
                     my_cursor.close()

                     print('the database has been updated')
                     print('result =  none while loop time', end2-start2)
                     break
         #used to append the last value
         if result != None and result != last_csv_Date_Time:
               print('result doesnt equal none, gonna push the data')
               my_cursor = my_conn.cursor()
               my_cursor.execute('DELETE FROM QTUM;')
               start3 = time.time()
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/QTUM1m.csv' INTO TABLE QTUM
                                 FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                                 LINES TERMINATED BY '\r\n'
                                 IGNORE 1 LINES;''')
               end3 = time.time()
               my_conn.commit()
               my_cursor.close()
               print('result doesnt equal initial push time', end3-start3)
               print('the database has been updated')
               new_boy = 1

               if new_boy == 1:
                  while 1 < 2:
                     my_cursor = my_conn.cursor()

                     print('IN NOT EQUAL LOOP')
                     print('pushing new data')
                     start4 = time.time()
                     my_cursor.execute('INSERT INTO QTUM VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end4 = time.time()
                     print('not equal while loop time', end4-start4)
                     my_cursor.close()

                     print('the database has been updated')
                     break

         
         
         if result == last_csv_Date_Time:

                  print('================================')

                  print('NO NEW ENTRIES, CLOSING CONNECTION')
                  print('================================')

                  time.sleep(10)
                  my_conn.close()
         
   def TRXpush():
      while 1 < 2:
         try:
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/TRX1m.csv')
               print('file exists')

         except FileNotFoundError: 
               print('file not here yet')

               time.sleep(300)
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/TRX1m.csv')
               print('file is here maybe')
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
               #  CREATE TABLE `THETA` (
               #  `pair_1` varchar(20) NOT NULL,
               #  `pair_2` varchar(20) NOT NULL,
               #  `Date_Time` double NOT NULL,
               #  `Open_price` varchar(20) NULL,
               #  `High_price` varchar(20) NULL,
               #  `Low_price` varchar(20) NULL,
               #  `Close_price` varchar(20) NULL,
               #  `Volume` varchar(20) NULL
               #  ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
         my_cursor = my_conn.cursor()
         my_cursor.execute(''' select Date_Time from TRX order by Date_Time desc limit 1; ''')
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
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/TRX1m.csv' INTO TABLE TRX
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
                     my_cursor.execute('INSERT INTO TRX VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end2 = time.time()
                     my_cursor.close()

                     print('the database has been updated')
                     print('result =  none while loop time', end2-start2)
                     break
         #used to append the last value
         if result != None and result != last_csv_Date_Time:
               print('result doesnt equal none, gonna push the data')
               my_cursor = my_conn.cursor()
               my_cursor.execute('DELETE FROM TRX;')
               start3 = time.time()
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/TRX1m.csv' INTO TABLE TRX
                                 FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                                 LINES TERMINATED BY '\r\n'
                                 IGNORE 1 LINES;''')
               end3 = time.time()
               my_conn.commit()
               my_cursor.close()
               print('result doesnt equal initial push time', end3-start3)
               print('the database has been updated')
               new_boy = 1

               if new_boy == 1:
                  while 1 < 2:
                     my_cursor = my_conn.cursor()

                     print('IN NOT EQUAL LOOP')
                     print('pushing new data')
                     start4 = time.time()
                     my_cursor.execute('INSERT INTO TRX VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end4 = time.time()
                     print('not equal while loop time', end4-start4)
                     my_cursor.close()

                     print('the database has been updated')
                     break

         
         
         if result == last_csv_Date_Time:

               print('================================')

               print('NO NEW ENTRIES, CLOSING CONNECTION')
               print('================================')

               time.sleep(10)
               my_conn.close()
   def VETpush():
      while 1 < 2:
         try:
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/VET1m.csv')
               print('file exists')

         except FileNotFoundError: 
               print('file not here yet')

               time.sleep(300)
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/VET1m.csv')
               print('file is here maybe')
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
               #  CREATE TABLE `THETA` (
               #  `pair_1` varchar(20) NOT NULL,
               #  `pair_2` varchar(20) NOT NULL,
               #  `Date_Time` double NOT NULL,
               #  `Open_price` varchar(20) NULL,
               #  `High_price` varchar(20) NULL,
               #  `Low_price` varchar(20) NULL,
               #  `Close_price` varchar(20) NULL,
               #  `Volume` varchar(20) NULL
               #  ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
         my_cursor = my_conn.cursor()
         my_cursor.execute(''' select Date_Time from VET order by Date_Time desc limit 1; ''')
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
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/VET1m.csv' INTO TABLE VET
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
                     my_cursor.execute('INSERT INTO VET VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end2 = time.time()
                     my_cursor.close()

                     print('the database has been updated')
                     print('result =  none while loop time', end2-start2)
                     break
         #used to append the last value
         if result != None and result != last_csv_Date_Time:
               print('result doesnt equal none, gonna push the data')
               my_cursor = my_conn.cursor()
               my_cursor.execute('DELETE FROM VET;')
               start3 = time.time()
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/VET1m.csv' INTO TABLE VET
                                 FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                                 LINES TERMINATED BY '\r\n'
                                 IGNORE 1 LINES;''')
               end3 = time.time()
               my_conn.commit()
               my_cursor.close()
               print('result doesnt equal initial push time', end3-start3)
               print('the database has been updated')
               new_boy = 1

               if new_boy == 1:
                  while 1 < 2:
                     my_cursor = my_conn.cursor()

                     print('IN NOT EQUAL LOOP')
                     print('pushing new data')
                     start4 = time.time()
                     my_cursor.execute('INSERT INTO VET VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end4 = time.time()
                     print('not equal while loop time', end4-start4)
                     my_cursor.close()

                     print('the database has been updated')
                     break

         
         
         if result == last_csv_Date_Time:

                  print('================================')

                  print('NO NEW ENTRIES, CLOSING CONNECTION')
                  print('================================')

                  time.sleep(10)
                  my_conn.close()
      
   def XLMpush():
      while 1 < 2:
         try:
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/XLM1m.csv')
               print('file exists')

         except FileNotFoundError: 
               print('file not here yet')

               time.sleep(300)
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/XLM1m.csv')
               print('file is here maybe')
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
               #  CREATE TABLE `THETA` (
               #  `pair_1` varchar(20) NOT NULL,
               #  `pair_2` varchar(20) NOT NULL,
               #  `Date_Time` double NOT NULL,
               #  `Open_price` varchar(20) NULL,
               #  `High_price` varchar(20) NULL,
               #  `Low_price` varchar(20) NULL,
               #  `Close_price` varchar(20) NULL,
               #  `Volume` varchar(20) NULL
               #  ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
         my_cursor = my_conn.cursor()
         my_cursor.execute(''' select Date_Time from XLM order by Date_Time desc limit 1; ''')
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
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/XLM1m.csv' INTO TABLE XLM
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
                     my_cursor.execute('INSERT INTO XLM VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end2 = time.time()
                     my_cursor.close()

                     print('the database has been updated')
                     print('result =  none while loop time', end2-start2)
                     break
         #used to append the last value
         if result != None and result != last_csv_Date_Time:
               print('result doesnt equal none, gonna push the data')
               my_cursor = my_conn.cursor()
               my_cursor.execute('DELETE FROM XLM;')
               start3 = time.time()
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/XLM1m.csv' INTO TABLE XLM
                                 FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                                 LINES TERMINATED BY '\r\n'
                                 IGNORE 1 LINES;''')
               end3 = time.time()
               my_conn.commit()
               my_cursor.close()
               print('result doesnt equal initial push time', end3-start3)
               print('the database has been updated')
               new_boy = 1

               if new_boy == 1:
                  while 1 < 2:
                     my_cursor = my_conn.cursor()

                     print('IN NOT EQUAL LOOP')
                     print('pushing new data')
                     start4 = time.time()
                     my_cursor.execute('INSERT INTO XLM VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end4 = time.time()
                     print('not equal while loop time', end4-start4)
                     my_cursor.close()

                     print('the database has been updated')
                     break

         
         
         if result == last_csv_Date_Time:

                  print('================================')

                  print('NO NEW ENTRIES, CLOSING CONNECTION')
                  print('================================')

                  time.sleep(10)
                  my_conn.close()
      
   def XMRpush():
      while 1 < 2:
         try:
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/XMR1m.csv')
               print('file exists')

         except FileNotFoundError: 
               print('file not here yet')

               time.sleep(300)
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/XMR1m.csv')
               print('file is here maybe')
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
               #  CREATE TABLE `THETA` (
               #  `pair_1` varchar(20) NOT NULL,
               #  `pair_2` varchar(20) NOT NULL,
               #  `Date_Time` double NOT NULL,
               #  `Open_price` varchar(20) NULL,
               #  `High_price` varchar(20) NULL,
               #  `Low_price` varchar(20) NULL,
               #  `Close_price` varchar(20) NULL,
               #  `Volume` varchar(20) NULL
               #  ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
         my_cursor = my_conn.cursor()
         my_cursor.execute(''' select Date_Time from XMR order by Date_Time desc limit 1; ''')
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
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/XMR1m.csv' INTO TABLE XMR
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
                     my_cursor.execute('INSERT INTO XMR VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end2 = time.time()
                     my_cursor.close()

                     print('the database has been updated')
                     print('result =  none while loop time', end2-start2)
                     break
         #used to append the last value
         if result != None and result != last_csv_Date_Time:
               print('result doesnt equal none, gonna push the data')
               my_cursor = my_conn.cursor()
               my_cursor.execute('DELETE FROM XMR;')
               start3 = time.time()
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/XMR1m.csv' INTO TABLE XMR
                                 FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                                 LINES TERMINATED BY '\r\n'
                                 IGNORE 1 LINES;''')
               end3 = time.time()
               my_conn.commit()
               my_cursor.close()
               print('result doesnt equal initial push time', end3-start3)
               print('the database has been updated')
               new_boy = 1

               if new_boy == 1:
                  while 1 < 2:
                     my_cursor = my_conn.cursor()

                     print('IN NOT EQUAL LOOP')
                     print('pushing new data')
                     start4 = time.time()
                     my_cursor.execute('INSERT INTO XMR VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end4 = time.time()
                     print('not equal while loop time', end4-start4)
                     my_cursor.close()

                     print('the database has been updated')
                     break

         
         
         if result == last_csv_Date_Time:

               print('================================')

               print('NO NEW ENTRIES, CLOSING CONNECTION')
               print('================================')

               time.sleep(10)
               my_conn.close()
   def XRPpush():
      while 1 < 2:
         try:
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/XRP1m.csv')
               print('file exists')

         except FileNotFoundError: 
               print('file not here yet')

               time.sleep(600)
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/XRP1m.csv')
               print('file is here maybe')
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
               #  CREATE TABLE `THETA` (
               #  `pair_1` varchar(20) NOT NULL,
               #  `pair_2` varchar(20) NOT NULL,
               #  `Date_Time` double NOT NULL,
               #  `Open_price` varchar(20) NULL,
               #  `High_price` varchar(20) NULL,
               #  `Low_price` varchar(20) NULL,
               #  `Close_price` varchar(20) NULL,
               #  `Volume` varchar(20) NULL
               #  ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
         my_cursor = my_conn.cursor()
         my_cursor.execute(''' select Date_Time from XRP order by Date_Time desc limit 1; ''')
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
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/XRP1m.csv' INTO TABLE XRP
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
                     my_cursor.execute('INSERT INTO XRP VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end2 = time.time()
                     my_cursor.close()

                     print('the database has been updated')
                     print('result =  none while loop time', end2-start2)
                     break
         #used to append the last value
         if result != None and result != last_csv_Date_Time:
               print('result doesnt equal none, gonna push the data')
               my_cursor = my_conn.cursor()
               my_cursor.execute('DELETE FROM XRP;')
               start3 = time.time()
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/XRP1m.csv' INTO TABLE XRP
                                 FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                                 LINES TERMINATED BY '\r\n'
                                 IGNORE 1 LINES;''')
               end3 = time.time()
               my_conn.commit()
               my_cursor.close()
               print('result doesnt equal initial push time', end3-start3)
               print('the database has been updated')
               new_boy = 1

               if new_boy == 1:
                  while 1 < 2:
                     my_cursor = my_conn.cursor()

                     print('IN NOT EQUAL LOOP')
                     print('pushing new data')
                     start4 = time.time()
                     my_cursor.execute('INSERT INTO XRP VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end4 = time.time()
                     print('not equal while loop time', end4-start4)
                     my_cursor.close()

                     print('the database has been updated')
                     break

         
         
         if result == last_csv_Date_Time:

               print('================================')

               print('NO NEW ENTRIES, CLOSING CONNECTION')
               print('================================')

               time.sleep(10)
               my_conn.close()
     
   def XTZpush():
      while 1 < 2:
         try:
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/XTZ1m.csv')
               print('file exists')

         except FileNotFoundError: 
               print('file not here yet')

               time.sleep(300)
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/XTZ1m.csv')
               print('file is here maybe')
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
               #  CREATE TABLE `THETA` (
               #  `pair_1` varchar(20) NOT NULL,
               #  `pair_2` varchar(20) NOT NULL,
               #  `Date_Time` double NOT NULL,
               #  `Open_price` varchar(20) NULL,
               #  `High_price` varchar(20) NULL,
               #  `Low_price` varchar(20) NULL,
               #  `Close_price` varchar(20) NULL,
               #  `Volume` varchar(20) NULL
               #  ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
         my_cursor = my_conn.cursor()
         my_cursor.execute(''' select Date_Time from XTZ order by Date_Time desc limit 1; ''')
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
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/XTZ1m.csv' INTO TABLE XTZ
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
                     my_cursor.execute('INSERT INTO XTZ VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end2 = time.time()
                     my_cursor.close()

                     print('the database has been updated')
                     print('result =  none while loop time', end2-start2)
                     break
         #used to append the last value
         if result != None and result != last_csv_Date_Time:
               print('result doesnt equal none, gonna push the data')
               my_cursor = my_conn.cursor()
               my_cursor.execute('DELETE FROM XTZ;')
               start3 = time.time()
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/XTZ1m.csv' INTO TABLE XTZ
                                 FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                                 LINES TERMINATED BY '\r\n'
                                 IGNORE 1 LINES;''')
               end3 = time.time()
               my_conn.commit()
               my_cursor.close()
               print('result doesnt equal initial push time', end3-start3)
               print('the database has been updated')
               new_boy = 1

               if new_boy == 1:
                  while 1 < 2:
                     my_cursor = my_conn.cursor()

                     print('IN NOT EQUAL LOOP')
                     print('pushing new data')
                     start4 = time.time()
                     my_cursor.execute('INSERT INTO XTZ VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end4 = time.time()
                     print('not equal while loop time', end4-start4)
                     my_cursor.close()

                     print('the database has been updated')
                     break

         
         
         if result == last_csv_Date_Time:

               print('================================')

               print('NO NEW ENTRIES, CLOSING CONNECTION')
               print('================================')

               time.sleep(10)
               my_conn.close()
      
   def ZECpush():
      while 1 < 2:
         try:
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/ZEC1m.csv')
               print('file exists')

         except FileNotFoundError: 
               print('file not here yet')

               time.sleep(300)
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/ZEC1m.csv')
               print('file is here maybe')
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
               #  CREATE TABLE `THETA` (
               #  `pair_1` varchar(20) NOT NULL,
               #  `pair_2` varchar(20) NOT NULL,
               #  `Date_Time` double NOT NULL,
               #  `Open_price` varchar(20) NULL,
               #  `High_price` varchar(20) NULL,
               #  `Low_price` varchar(20) NULL,
               #  `Close_price` varchar(20) NULL,
               #  `Volume` varchar(20) NULL
               #  ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
         my_cursor = my_conn.cursor()
         my_cursor.execute(''' select Date_Time from ZEC order by Date_Time desc limit 1; ''')
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
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/ZEC1m.csv' INTO TABLE ZEC
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
                     my_cursor.execute('INSERT INTO ZEC VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end2 = time.time()
                     my_cursor.close()

                     print('the database has been updated')
                     print('result =  none while loop time', end2-start2)
                     break
         #used to append the last value
         if result != None and result != last_csv_Date_Time:
               print('result doesnt equal none, gonna push the data')
               my_cursor = my_conn.cursor()
               my_cursor.execute('DELETE FROM ZEC;')
               start3 = time.time()
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/ZEC1m.csv' INTO TABLE ZEC
                                 FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                                 LINES TERMINATED BY '\r\n'
                                 IGNORE 1 LINES;''')
               end3 = time.time()
               my_conn.commit()
               my_cursor.close()
               print('result doesnt equal initial push time', end3-start3)
               print('the database has been updated')
               new_boy = 1

               if new_boy == 1:
                  while 1 < 2:
                     my_cursor = my_conn.cursor()

                     print('IN NOT EQUAL LOOP')
                     print('pushing new data')
                     start4 = time.time()
                     my_cursor.execute('INSERT INTO ZEC VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end4 = time.time()
                     print('not equal while loop time', end4-start4)
                     my_cursor.close()

                     print('the database has been updated')
                     break

         
         
         if result == last_csv_Date_Time:

               print('================================')

               print('NO NEW ENTRIES, CLOSING CONNECTION')
               print('================================')

               time.sleep(10)
               my_conn.close()      
   def THETApush():
      while 1 < 2:
         try:
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/THETA1m.csv')
               print('file exists')

         except FileNotFoundError: 
               print('file not here yet')

               time.sleep(300)
               data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/THETA1m.csv')
               print('file is here maybe')
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
               #  CREATE TABLE `THETA` (
               #  `pair_1` varchar(20) NOT NULL,
               #  `pair_2` varchar(20) NOT NULL,
               #  `Date_Time` double NOT NULL,
               #  `Open_price` varchar(20) NULL,
               #  `High_price` varchar(20) NULL,
               #  `Low_price` varchar(20) NULL,
               #  `Close_price` varchar(20) NULL,
               #  `Volume` varchar(20) NULL
               #  ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
         my_cursor = my_conn.cursor()
         my_cursor.execute(''' select Date_Time from THETA order by Date_Time desc limit 1; ''')
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
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/THETA1m.csv' INTO TABLE THETA
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
                     my_cursor.execute('INSERT INTO THETA VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end2 = time.time()
                     my_cursor.close()

                     print('the database has been updated')
                     print('result =  none while loop time', end2-start2)
                     break
         #used to append the last value
         if result != None and result != last_csv_Date_Time:
               print('result doesnt equal none, gonna push the data')
               my_cursor = my_conn.cursor()
               my_cursor.execute('DELETE FROM THETA;')
               start3 = time.time()
               my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/THETA1m.csv' INTO TABLE THETA
                                 FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                                 LINES TERMINATED BY '\r\n'
                                 IGNORE 1 LINES;''')
               end3 = time.time()
               my_conn.commit()
               my_cursor.close()
               print('result doesnt equal initial push time', end3-start3)
               print('the database has been updated')
               new_boy = 1

               if new_boy == 1:
                  while 1 < 2:
                     my_cursor = my_conn.cursor()

                     print('IN NOT EQUAL LOOP')
                     print('pushing new data')
                     start4 = time.time()
                     my_cursor.execute('INSERT INTO THETA VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                     end4 = time.time()
                     print('not equal while loop time', end4-start4)
                     my_cursor.close()

                     print('the database has been updated')
                     break

         
         
         if result == last_csv_Date_Time:

               print('================================')

               print('NO NEW ENTRIES, CLOSING CONNECTION')
               print('================================')

               time.sleep(10)
               my_conn.close()