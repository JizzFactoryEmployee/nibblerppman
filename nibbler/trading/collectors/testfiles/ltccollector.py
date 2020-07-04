from nibbler import trading as td
from nibbler.trading.collectors.collector_base import Collector



class BinanceLTC(Collector):
    _exchange = 'binance'
    symbol = 'LTC/USDT'
    limit = 1000
    
    def LTCcollector1m():
        from pathlib import Path
        import time
        import os
        directory = Path(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/LTC/1m')
        timeFrame = '1m'
        filename = 'LTC%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceLTC(timeFrame)
        collector.run_loop(filepath, timestamp='2020-01-09T00:00:00Z',  multiplier=1)

BinanceLTC.LTCcollector1m()