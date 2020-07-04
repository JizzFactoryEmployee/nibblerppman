from nibbler import trading as td
from nibbler.trading.collectors.collector_base import Collector



class BinanceXLM(Collector):
    _exchange = 'binance'
    symbol = 'XLM/USDT'
    limit = 1000
    
    def XLMcollector1m():
        from pathlib import Path
        import time
        import os
        directory = Path(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/XLM/1m')
        timeFrame = '1m'
        filename = 'XLM%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceXLM(timeFrame)
        collector.run_loop(filepath, timestamp='2020-01-20T00:00:00Z',  multiplier=1)

BinanceXLM.XLMcollector1m()