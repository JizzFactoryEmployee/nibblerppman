from nibbler import trading as td
from nibbler.trading.collectors.collector_base import Collector



class BinanceEOS(Collector):
    _exchange = 'binance'
    symbol = 'EOS/USDT'
    limit = 1000
    
    def EOScollector1m():
        from pathlib import Path
        import time
        import os
        directory = Path(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/EOS/1m')
        timeFrame = '1m'
        filename = 'EOS%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceEOS(timeFrame)
        collector.run_loop(filepath, timestamp='2020-01-08T00:00:00Z',  multiplier=1)

BinanceEOS.EOScollector1m()