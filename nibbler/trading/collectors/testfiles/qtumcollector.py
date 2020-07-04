from nibbler import trading as td
from nibbler.trading.collectors.collector_base import Collector



class BinanceQTUM(Collector):
    _exchange = 'binance'
    symbol = 'QTUM/USDT'
    limit = 1000
    
    def QTUMcollector1m():
        from pathlib import Path
        import time
        import os
        directory = Path(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/QTUM/1m')
        timeFrame = '1m'
        filename = 'QTUM%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceQTUM(timeFrame)
        collector.run_loop(filepath, timestamp='2020-02-20T00:00:00Z',  multiplier=1)

BinanceQTUM.QTUMcollector1m()