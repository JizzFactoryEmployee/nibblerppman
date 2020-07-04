from nibbler import trading as td
from nibbler.trading.collectors.collector_base import Collector



class BinanceTRX(Collector):
    _exchange = 'binance'
    symbol = 'TRX/USDT'
    limit = 1000
    
    def TRXcollector1m():
        from pathlib import Path
        import time
        import os
        directory = Path(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/TRX/1m')
        timeFrame = '1m'
        filename = 'TRX%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceTRX(timeFrame)
        collector.run_loop(filepath, timestamp='2020-01-15T00:00:00Z',  multiplier=1)

BinanceTRX.TRXcollector1m()