from nibbler.trading.collectors.collect_bitcoin import livecollectorBTC
from nibbler.trading.collectors.collect_bitcoin import livecollectorETH
from nibbler.trading.collectors.collect_bitcoin import livecollectorLINK

import threading
import time

def CollectNPush():
    t1 = threading.Thread(target=livecollectorBTC, name='t1')
    t2 = threading.Thread(target=livecollectorETH, name='t2')
    t3 = threading.Thread(target=livecollectorLINK, name='t3')

    t1.start()
    t2.start()
    t3.start()

CollectNPush()

