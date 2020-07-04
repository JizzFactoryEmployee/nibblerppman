from nibbler import trading as td
from nibbler.trading.collectors.collector_base import Collector



class BinanceXRP(Collector):
    _exchange = 'binance'
    symbol = 'XRP/USDT'
    limit = 1000
    
    def XRPcollector1m():
        from pathlib import Path
        import time
        import os
        directory = Path(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/XRP/1m')
        timeFrame = '1m'
        filename = 'XRP%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceXRP(timeFrame)
        collector.run_loop(filepath, timestamp='2020-01-08T00:00:00Z',  multiplier=1)

BinanceXRP.XRPcollector1m()