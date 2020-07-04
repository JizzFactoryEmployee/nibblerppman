from nibbler import trading as td
from nibbler.trading.collectors.collector_base import Collector



class BinanceZEC(Collector):
    _exchange = 'binance'
    symbol = 'ZEC/USDT'
    limit = 1000
    
    def ZECcollector1m():
        from pathlib import Path
        import time
        import os
        directory = Path(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/ZEC/1m')
        timeFrame = '1m'
        filename = 'ZEC%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceZEC(timeFrame)
        collector.run_loop(filepath, timestamp='2020-02-05T00:00:00Z',  multiplier=1)

BinanceZEC.ZECcollector1m()