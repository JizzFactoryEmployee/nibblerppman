import nibbler.trading.collectors.futures_collector as f
import threading
import nibbler.trading.collectors.MYSQL.lastversion as l
BTCcoll = threading.Thread(target=f.BinanceBTC.BTCcollector1m)
BTCpush  = threading.Thread(target= l.MyHandler.runner)
BTCcoll.start()
BTCpush.start()