from nibbler import trading as td
from nibbler.trading.collectors.collector_base import Collector



class BinanceETH(Collector):
    _exchange = 'binance'
    symbol = 'ETH/USDT'
    limit = 1000
    
    def ETHcollector1m():
        from pathlib import Path
        import time
        import os
        directory = Path(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/ETH/1m')
        timeFrame = '1m'
        filename = 'ETH%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceETH(timeFrame)
        collector.run_loop(filepath, timestamp='2019-11-27T00:00:00Z',  multiplier=1)

BinanceETH.ETHcollector1m()