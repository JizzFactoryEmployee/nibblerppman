
            while 1 < 2:
                #if we get to this point then it means that the data isnt fuccked and we can now push the CSV data to the database without worry
                #we need to ensure that we get the last data point
                #we need to ensure that its sequential
                #now that we know the data isnt fucked we can pipe the last data point into the df
                #have a protection mechanism with float
                #ensure that it cant push if the csv data is equal to the database


                ####getting the last data point##############
                # d1 = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/BTC1m.csv')
                # try:
                #     time.sleep(0.1)
                #     last_csv_pair_1 = d1.pair_1.iloc[-1]
                #     time.sleep(0.1)

                #     last_csv_pair_2 = d1.pair_2.iloc[-1]
                #     time.sleep(0.1)

                #     last_csv_Date_Time = int(d1.Date_Time.iloc[-1])
                #     time.sleep(0.1)

                #     last_csv_Open_price = round(float(d1.Open_price.iloc[-1]),3)
                #     time.sleep(0.1)

                #     last_csv_High_price = round(float(d1.High_price.iloc[-1]),3)                    
                #     time.sleep(0.1)

                #     last_csv_Low_price = round(float(d1.Low_price.iloc[-1]),3)                    
                #     time.sleep(0.1)

                #     last_csv_Close_price = round(float(d1.Close_price.iloc[-1]),3)                    
                #     time.sleep(0.1)

                #     last_csv_Volume = round(float(d1.Volume.iloc[-1]),3)                    
                #     time.sleep(0.1)

                #     last_last_csv = last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume

                # except ValueError:
                #     time.sleep(5)
                #     last_csv_pair_1 = d1.pair_1.iloc[-1]
                #     last_csv_pair_2 = d1.pair_2.iloc[-1]
                #     last_csv_Date_Time = int(d1.Date_Time.iloc[-1])
                #     last_csv_Open_price = round(float(d1.Open_price.iloc[-1]),3)
                #     last_csv_High_price = round(float(d1.High_price.iloc[-1]),3)
                #     last_csv_Low_price = round(float(d1.Low_price.iloc[-1]),3)
                #     last_csv_Close_price = round(float(d1.Close_price.iloc[-1]),3)
                #     last_csv_Volume = round(float(d1.Volume.iloc[-1]),3)
                #     last_last_csv = last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume

                my_cursor = my_conn.cursor()
                my_cursor.execute('''select * from BTC order by Date_Time desc limit 1;''')
                last_last_database = my_cursor.fetchall()[0]
                my_cursor.close()

                while 1 < 2:
                    if cunt == last_last_database:
                        #the last vals are equal which means we dont need to push, it  should justt exit out of this individual loop
                        print('its the same')
                        print('do nothing or make it exit out')
                        break

                    if cunt != last_last_database:
                        time.sleep(1)
                        # d2 = pd.read_csv(r'C:/Users/James/Documents/GitHub/Nibbler/nibbler/trading/collectors/BTC1m.csv')
                        
                        
                            # time.sleep(0.1)
                            # last_csv_pair_1 = d1.pair_1.iloc[-1]
                            # time.sleep(0.1)

                            # last_csv_pair_2 = d1.pair_2.iloc[-1]
                            # time.sleep(0.1)

                            # last_csv_Date_Time = int(d1.Date_Time.iloc[-1])
                            # time.sleep(0.1)

                            # last_csv_Open_price = round(float(d1.Open_price.iloc[-1]),3)
                            # time.sleep(0.1)

                            # last_csv_High_price = round(float(d1.High_price.iloc[-1]),3)                    
                            # time.sleep(0.1)

                            # last_csv_Low_price = round(float(d1.Low_price.iloc[-1]),3)                    
                            # time.sleep(0.1)

                            # last_csv_Close_price = round(float(d1.Close_price.iloc[-1]),3)                    
                            # time.sleep(0.1)

                            # last_csv_Volume = round(float(d1.Volume.iloc[-1]),3)                    
                            # time.sleep(0.1)
                            # last_last_csv = last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume

                        # except ValueError:
                        #     time.sleep(10)
                        #     last_csv_pair_1 = d2.pair_1.iloc[-1]
                        #     last_csv_pair_2 = d2.pair_2.iloc[-1]
                        #     last_csv_Date_Time = int(d2.Date_Time.iloc[-1])
                        #     #nan value occurs somewhere here, need a solution for it
                        #     last_csv_Open_price = round(float(d2.Open_price.iloc[-1]),3)
                        #     last_csv_High_price = round(float(d2.High_price.iloc[-1]),3)
                        #     last_csv_Low_price = round(float(d2.Low_price.iloc[-1]),3)
                        #     last_csv_Close_price = round(float(d2.Close_price.iloc[-1]),3)
                        #     last_csv_Volume = round(float(d2.Volume.iloc[-1]),3)
                        #     last_last_csv = last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume
                        #     print('###############################value error colum##########################################################################')

                        my_cursor = my_conn.cursor()
                        my_cursor.execute('''select * from BTC order by Date_Time desc limit 1;''')
                        last_last_database = my_cursor.fetchall()[0]
                        my_cursor.close()
                        print('#####last csv point',    cunt)
                        print('last database point',    last_last_database)
                        print('########DATABASE LENGHT:', )
                        # print('different, lets sleep')
                        # time.sleep(5)
                        # #this  means it doesnt equal and we need to push last_last_csv to the database
                        # print('its different, time to poooosh')
                        # while 1 <2: 
                        #     my_cursor = my_conn.cursor()
                            
                        #     try:
                        #         my_cursor.execute('INSERT INTO BTC VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                        #         penis = 1
                        #     except pymysql.err.InternalError:
                        #         time.sleep(5)
                                
                        #         my_cursor.execute('INSERT INTO BTC VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (last_csv_pair_1, last_csv_pair_2, last_csv_Date_Time, last_csv_Open_price, last_csv_High_price, last_csv_Low_price, last_csv_Close_price, last_csv_Volume))
                        #         penis = 2
                        
                        #     my_conn.commit()

                        #     my_cursor.close()
                        

                        #     print('IT POOOSHED')
                        #     my_cursor = my_conn.cursor()
                        #     my_cursor.execute('SELECT COUNT(*) FROM BTC;')
                        #     DATA_LEN = my_cursor.fetchall()[0]
                        #     print(DATA_LEN)
                        #     my_cursor.close()
                            
               
