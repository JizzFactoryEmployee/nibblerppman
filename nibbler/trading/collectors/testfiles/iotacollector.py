from nibbler import trading as td
from nibbler.trading.collectors.collector_base import Collector



class BinanceIOTA(Collector):
    _exchange = 'binance'
    symbol = 'IOTA/USDT'
    limit = 1000
    
    def IOTAcollector1m():
        from pathlib import Path
        import time
        import os
        directory = Path(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/IOTA/1m')
        timeFrame = '1m'
        filename = 'IOTA%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceIOTA(timeFrame)
        collector.run_loop(filepath, timestamp='2020-02-12T00:00:00Z',  multiplier=1)

BinanceIOTA.IOTAcollector1m()