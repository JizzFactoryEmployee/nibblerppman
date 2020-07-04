from nibbler import trading as td
from nibbler.trading.collectors.collector_base import Collector



class BinanceBTC(Collector):
    _exchange = 'binance'
    symbol = 'BTC/USDT'
    limit = 1000
    
    def BTCcollector1m():
        from pathlib import Path
        import time
        import os
        directory = Path(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/BTC/1m')
        timeFrame = '1m'
        filename = 'BTC%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceBTC(timeFrame)
        collector.run_loop(filepath, timestamp='2019-09-08T00:00:00Z',  multiplier=1)

BinanceBTC.BTCcollector1m()