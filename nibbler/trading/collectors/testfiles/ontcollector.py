from nibbler import trading as td
from nibbler.trading.collectors.collector_base import Collector



class BinanceONT(Collector):
    _exchange = 'binance'
    symbol = 'ONT/USDT'
    limit = 1000
    
    def ONTcollector1m():
        from pathlib import Path
        import time
        import os
        directory = Path(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/ONT/1m')
        timeFrame = '1m'
        filename = 'ONT%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceONT(timeFrame)
        collector.run_loop(filepath, timestamp='2020-02-11T00:00:00Z',  multiplier=1)

BinanceONT.ONTcollector1m()