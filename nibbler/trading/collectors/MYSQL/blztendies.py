import pymysql
import time
import pandas as pd
from tqdm import tqdm

def ppman():

    print('first load, sleeping')
    for i in  tqdm(range(1,10)): 
        time.sleep(2)
    try:
        data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/BTC1m.csv')
        print('file exists')
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
    my_cursor.execute(''' select Date_Time from BTC order by Date_Time desc limit 1; ''')
    result = my_cursor.fetchone()
    a = str(result).strip("(,)")
    try:
        result = int(float(a))
    except ValueError:
        pass
    print(result)

    my_cursor.close()
    # while 1 < 2:
    #     if result != data.Date_Time.iloc[-1]:
    #         print('====INSIDE THE NOT EQUAL LOOP======DATASET IS POPULATED BUT CSV != DF =======')
    #         my_cursor = my_conn.cursor()
    #         my_cursor.execute(''' DELETE FROM BTC; ''')
    #         end1 = time.time()
    #         my_cursor.close()
    #         print('ffff')
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

                
#THE RESULT=NONE LOOP WORKS PROPERLY
    if result == None:
        print('====INSIDE THE NONE LOOP======DATASET IS EMPTY=======')
        print('sleeping for a bit to ensure the database is fully populated')


        my_cursor = my_conn.cursor()
        start1 = time.time()
        my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/BTC1m.csv' IGNORE INTO TABLE BTC
                            FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                            LINES TERMINATED BY '\r\n'
                            IGNORE 1 LINES;''')
        my_cursor.execute('SHOW WARNINGS')

        my_conn.commit()
        end1 = time.time()
        my_cursor.close()

        my_cursor = my_conn.cursor()
        my_cursor.execute(''' select COUNT(*) FROM BTC; ''')
        result = my_cursor.fetchone()
        Clean_results= str(result).strip("(,)")
        result = int(float(Clean_results))
        my_cursor.close()

        print('=====RESULT NONE TIME======', end1-start1)

        if result == len(data):
            #double check by comparing the last x points
            import random
            #make a foreloop that checks 10 random data points
            data_check_amount = list(range(1,100))
            counter = 0
            for i in data_check_amount:
                my_cursor = my_conn.cursor()

                random_points = random.randint(1, len(data))
                my_cursor.execute('''select * from BTC limit %s ,1;''', (random_points))
                check = my_cursor.fetchall()[0]
                
                csv_check = data.iloc[random_points]

                cunt = csv_check[0],csv_check[1], round(csv_check[2],0), round(csv_check[3],3), round(csv_check[4],3), round(csv_check[5],3), round(csv_check[6],3), round(csv_check[7],3)
                # fuck = [[i[0] for i in check],[i[1] for i in check],[i[2] for i in check],[i[3] for i in check],[i[4] for i in check],[i[5] for i in check],[i[6] for i in check],[i[7] for i in check]]
                # fuck = tuple(fuck)

                #strings have to match perfectly to be considered equal
                #turn them to a list
                #splut them (',')
                print(check)
                print(cunt)
                if cunt == check:
                    counter = counter+1
                    print(counter)

                    if counter == len(data_check_amount):
                        print('ERROR PROTECTION COMPLETE, MOVING ON TO DATA PUSHING')
                        break
                else:
                   
                    print('not equal')
                    time.sleep(999999)

                #check whether the random points are within the list

            while 1 < 2:
           
                my_cursor = my_conn.cursor()
                my_cursor.execute('''select * from BTC order by Date_Time desc limit 1;''')
                last_last_database = my_cursor.fetchall()[0]
                my_cursor.close()
                data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/BTC1m.csv')
                time.sleep(10)
                a = data.pair_1.iloc[-1], data.pair_2.iloc[-1], round(data.Date_Time.iloc[-1],0), round(data.Open_price.iloc[-1],3), round(data.High_price.iloc[-1],3), round(data.Low_price.iloc[-1],3), round(data.Close_price.iloc[-1],3), round(data.Volume.iloc[-1],3)
                a_str = str(a)
                last_last_database_str = str(last_last_database)

                while 1 < 2:

                    
                    if a == last_last_database:
                        #the last vals are equal which means we dont need to push, it  should justt exit out of this individual loop
                        print('its the same')
                        time.sleep(1)
                        break

                    if a != last_last_database:
                        '''
                        need to make sure that the csv date time is updated
                        
                        '''
                    
                        if 'nan' in a_str:
                            print('nan in fucker')
                            time.sleep(10000)
                            print('ffff')
                    

                        my_cursor = my_conn.cursor()
                        my_cursor.execute('''select * from BTC order by Date_Time desc limit 1;''')
                        last_last_database = my_cursor.fetchall()[0]
                        my_cursor.close()
                        print('                                   ')
                        print('#####last csv point',    a)
                        print('last database point',    last_last_database)
                        print('                                   ')

                        break                        


    print('pp)')
