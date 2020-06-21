import pymysql
import time
import pandas as pd
from tqdm import tqdm  
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime, timedelta
class MyHandlerTHETA(FileSystemEventHandler):
    def __init__(self):
        self.last_modified = datetime.now()
    def runner():

        event_handler = MyHandlerTHETA()
        observer = Observer()
        observer.schedule(event_handler, path=r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\coins\THETA\1m', recursive=False)
        observer.start()

        try:
            while 1<2:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

    def on_modified(self, event):
        if datetime.now() - self.last_modified < timedelta(seconds=2):
            event_list = event.src_path.split('\\')
            filename = event_list[-1]
            if 'THETA' in filename:
                print('THETA ACTIVATE GO CORN GO')
                time.sleep(3)
                try:
                    data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/coins/THETA/1m/THETA1m.csv')
                    print('file exists')
                #if the file is being populated it wont be found, thus a timeout is needed while it populates
                except FileNotFoundError:
                    print('still not here, gonna wait longer, waiting five minutes')
                    time.sleep(600)
                    data = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/coins/THETA/1m/THETA1m.csv')
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
                my_cursor.execute(''' select count(*) from THETA; ''')
                result = my_cursor.fetchall()
                a = str(result).strip("(,)")
                try:
                    result = int((a))
                except ValueError:
                    pass
                print('the database length is equal to :',result)
                print('the csv length is equal to:', len(data))

                my_cursor.close()

                if result == 0 or result == None:
                    
                    print('====DATABASE IS EMPTY TIME TO POPULATE=======')


                    my_cursor = my_conn.cursor()
                    start1 = time.time()
                    #pushing data into the database from the CSV file
                    my_cursor.execute(''' LOAD DATA LOCAL INFILE 'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/coins/THETA/1m/THETA1m.csv' IGNORE INTO TABLE THETA
                                        FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                                        LINES TERMINATED BY '\r\n'
                                        IGNORE 1 LINES;''')
                    my_cursor.execute('SHOW WARNINGS')

                    my_conn.commit()
                    end1 = time.time()
                    my_cursor.close()

                    my_cursor = my_conn.cursor()
                    #getting the length of the database file
                    my_cursor.execute(''' select COUNT(*) FROM THETA; ''')
                    Clean_results = my_cursor.fetchall()
                    Clean_results = str(Clean_results).strip("(,)")
                    Clean_results = int(Clean_results)
                    my_cursor.close()
                    print('total values pushed', Clean_results)

                    print('=====PUSHED ENTIRE HISTORY IN:', end1-start1)

                    if Clean_results != len(data):
                        print('ssomething went wrong, probably a datta error')
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
                        Open_price = str(round(to_push[y][3], 3))
                        High_price = str(round(to_push[y][4], 3))
                        Low_price = str(round(to_push[y][5], 3))
                        Close_price = str(round(to_push[y][6], 3))
                        Volume = str(round(to_push[y][7], 3))
                        y = y+1
                        start2 = time.time()
                        my_cursor = my_conn.cursor()
                        my_cursor.execute('INSERT INTO THETA VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (pair_1, pair_2, Date_Time, Open_price, High_price, Low_price, Close_price, Volume))
                        my_conn.commit()
                        end2 = time.time()
                        print('pushed', gap, 'values in:', end2-start2)
                        if y == gap:
                            print('out of the push loop')
                            
                # if listy != newlist:
                #     print('uuuuu')   

                # if gap == 1:
                #     print('no data errors, going to update the last csv value')

                #     pair_1 = data.pair_1.iloc[-1]
                #     pair_2 =  data.pair_2.iloc[-1]
                #     Date_Time = str(round(data.Date_Time.iloc[-1],0))
                #     Open_price = str(round(data.Open_price.iloc[-1],3))
                #     High_price = str(round(data.High_price.iloc[-1],3))
                #     Low_price = str(round(data.Low_price.iloc[-1],3))
                #     Close_price = str(round(data.Close_price.iloc[-1],3))
                #     Volume = str(round(data.Volume.iloc[-1],3))

                #     my_cursor = my_conn.cursor()
                #     ppppp = time.time()
                #     my_cursor.execute('INSERT INTO BTC VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (pair_1, pair_2, Date_Time, Open_price, High_price, Low_price, Close_price, Volume))
                #     my_conn.commit()
                #     ppp = time.time()
                #     my_cursor.close()
                    
                    # my_cursor = my_conn.cursor()
                    # my_cursor.execute(''' select COUNT(*) FROM BTC; ''')
                    # pingu = my_cursor.fetchall()
                    # pingu = str(pingu).strip("(,)")
                    # pingu = int(pingu)
                    # my_cursor.close()
                    # print('total values pushed', pingu)

                    # print('we poooshed in', ppp-ppppp)
                    

                # if gap > 1:
                #     print('something went wrong, just clear it all')
                #     my_cursor = my_conn.cursor()
                #     my_cursor.execute(''' DELETE FROM BTC; ''')
                #     my_conn.commit()
                #     my_cursor.close()
                #     print('data has been wiped, will repopulate next update')
            #if the result doesnt equal the data length then something is wrong
            #deleting the database will fix this and we can repopulate it

                if result > len(data):
                    print('something went wrong, database is somehow longer than the csv, deleting all')
                    my_cursor = my_conn.cursor()
                    my_cursor.execute(''' DELETE FROM THETA; ''')
                    my_conn.commit()
                    my_cursor.close()
                    print('data has been wiped, will repopulate next update')
                if result == len(data):

                    print('SAME LENGTH DO NOTHING')

                print('Done fren')

           
            return
        else:
            self.last_modified = datetime.now()
    
            print(f'Event type: {event.event_type}  path : {event.src_path}')
            print(event.is_directory) # This attribute is also available
