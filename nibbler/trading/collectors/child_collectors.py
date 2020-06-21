from . import Collector


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

class BinanceETH(Collector):
    _exchange = 'binance'
    symbol = 'ETH/USDT'
    limit = 500


class BinanceLINK(Collector):
    _exchange = 'binance'
    symbol = 'LINK/USDT'
    limit = 500
