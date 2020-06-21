from ...AlgoTrader.collectors.collector_base import Collector

class BitmexBTC(Collector):
    _exchange = 'bitmex'
    symbol = 'BTC/USD'


class BitmexETH(Collector):
    _exchange = 'bitmex'
    symbol = 'ETH/USD'


class BinanceBTC(Collector):
    _exchange = 'binance'
    symbol = 'BTC/USDT'
    limit = 1000


class BinanceNano(Collector):
    _exchange = 'binance'
    symbol = 'NANO/USDT'
    limit = 1000


class BinanceEOS(Collector):
    _exchange = 'binance'
    symbol = 'EOS/USDT'
    limit = 1000


if __name__ == "__main__":
    from pathlib import Path
    directory = Path(__file__).parent
    filename = 'pppeeeeee.csv'
    filepath = directory/filename
    collector = BinanceBTC('1m')
    collector.run_loop(filepath, timestamp='2020-05-29T00:00:00Z',  multiplier=1)
