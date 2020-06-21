import pymysql
import time
import pandas as pd
from tqdm import tqdm

def ppman():
    print('first load, sleeping')
    #setting a sleep timer just in case the datafile isnt created
    for i in  tqdm(range(1,10)): 
        time.sleep(2)
        
    try:
        data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/BTC1m.csv')
        print('file exists')
        print('#################LAST ROW: ', data.iloc[-1])
    #if the file is being populated it wont be found, thus a timeout is needed while it populates
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
    my_cursor = my_conn.cursor()
    #selecting the last date time value from the database
    my_cursor.execute(''' select Date_Time from BTC order by Date_Time desc limit 1; ''')
    result = my_cursor.fetchone()
    a = str(result).strip("(,)")
    try:
        result = int(float(a))
    except ValueError:
        pass
    print(result)

    my_cursor.close()

    #if the result doesnt equal the data length then something is wrong
    #deleting the database will fix this and we can repopulate it
    if result != len(data):
        print('doesnt equal, fuck')
        my_cursor = my_conn.cursor()
        my_cursor.execute(''' DELETE FROM BTC; ''')
        my_cursor.close()
        my_cursor = my_conn.cursor()
        my_cursor.execute(''' select Date_Time from BTC order by Date_Time desc limit 1; ''')
        result = my_cursor.fetchone()  
        a = str(result).strip("(,)")
  
        try:
            result = int(float(a))
        except ValueError:
            pass
        print(result)

#the data base should be empty and we should go into this loop
    if result == None:
        print('====INSIDE THE NONE LOOP======DATASET IS EMPTY=======')
        print('sleeping for a bit to ensure the database is fully populated')


        my_cursor = my_conn.cursor()
        start1 = time.time()
        #pushing data into the database from the CSV file
        my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/BTC1m.csv' IGNORE INTO TABLE BTC
                            FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                            LINES TERMINATED BY '\r\n'
                            IGNORE 1 LINES;''')
        my_cursor.execute('SHOW WARNINGS')

        my_conn.commit()
        end1 = time.time()
        my_cursor.close()

        my_cursor = my_conn.cursor()
        #getting the length of the database file
        my_cursor.execute(''' select COUNT(*) FROM BTC; ''')
        result = my_cursor.fetchone()
        Clean_results= str(result).strip("(,)")
        result = int(float(Clean_results))
        my_cursor.close()

        print('=====RESULT NONE TIME======', end1-start1)

        #if the data equals the length of the data
        #we want to double check to make sure theres no errors and everythings the same
        #we will select x random points from the database and compare them with
        #the csv equivalent.
        #the csv equivalent
        if result == len(data):
            #double check by comparing the last x points
            import random
            #make a foreloop that checks 10 random data points
            data_check_amount = list(range(1,20))
            counter = 0
            for i in data_check_amount:
                my_cursor = my_conn.cursor()

                random_points = random.randint(1, len(data))
                my_cursor.execute('''select * from BTC limit %s ,1;''', (random_points))
                check = my_cursor.fetchall()[0]
                
                csv_check = data.iloc[random_points]

                cunt = csv_check[0],csv_check[1], round(csv_check[2],0), round(csv_check[3],3), round(csv_check[4],3), round(csv_check[5],3), round(csv_check[6],3), round(csv_check[7],3)
                print('#################LAST ROW: ', data.iloc[-1])
                print('#################LAST ROW: ', cunt)


                print(check)
                if cunt == check:
                    counter = counter+1
                    print(counter)

                    if counter == len(data_check_amount):
                        print('ERROR PROTECTION COMPLETE, MOVING ON TO DATA PUSHING')
                        break
                else:
                   #it should never get to this point
                    print('not equal')
                    time.sleep(999999)

            while 1 < 2:
                error_protection = list(range(1,10))
                counter_2 = 0

                for i in error_protection:
                    my_cursor = my_conn.cursor()

                    my_cursor.execute('''select * from BTC order by Date_Time desc limit 1;''')
                    last_last_database = my_cursor.fetchall()[0]

                    last_csv_check = data.pair_1.iloc[-1], data.pair_2.iloc[-1], round(data.Date_Time.iloc[-1],0), round(data.Open_price.iloc[-1],3), round(data.High_price.iloc[-1],3), round(data.Low_price.iloc[-1],3), round(data.Close_price.iloc[-1],3), round(data.Volume.iloc[-1],3)
                    my_cursor.close()
                    print('#################LAST ROW: ', data.iloc[-1])
                    print('#################LAST ROW: ', last_csv_check)

                    print(last_last_database)

                    if last_last_database == last_csv_check:
                        counter_2 = counter_2+1
                        print(counter_2)


                        if counter_2 == len(error_protection):
                            print('ERROR PROTECTION ROUND 2 complete')
                            print('BOTH LAST ITEMS ARE THE SAME')
                            pair_1 = data.pair_1.iloc[-1]
                            pair_2 =  data.pair_2.iloc[-1]
                            Date_Time = str(round(data.Date_Time.iloc[-1],0))
                            Open_price = str(round(data.Open_price.iloc[-1],3))
                            High_price = str(round(data.High_price.iloc[-1],3))
                            Low_price = str(round(data.Low_price.iloc[-1],3))
                            Close_price = str(round(data.Close_price.iloc[-1],3))
                            Volume = str(round(data.Volume.iloc[-1],3))
                            print('broken out of the loop, no errorsyay')

                            print('####TO POOSH VALUES', Date_Time, Open_price, High_price, Low_price, Close_price, Volume)
                            my_cursor = my_conn.cursor()
                            my_cursor.execute('INSERT INTO BTC VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (pair_1, pair_2, Date_Time, Open_price, High_price, Low_price, Close_price, Volume))
                            my_conn.commit()
                            print('we poooshed')
                            time.sleep(10)
                    
                    else:
                        print('not equal')

                    
                        break

'''                 
                        
now we want to make a while loop that updates the data file
we need to have an extra error protection here
The CSV date time should not equal the database date time
-  if it does then we just break
- if it doesnt thhen we need to push that row of the CSV to the database

ORDER
connect and get the last row from the database
get the last row of data from the csv
make a loop that compares them x times, if they're the same after x times then move forward
if they're the same then push the last row from the csv to the database
if they're different then fuck, deal with that when i get to it

'''
