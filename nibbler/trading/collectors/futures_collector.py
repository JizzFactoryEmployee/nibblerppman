from nibbler import trading as td
from nibbler.trading.collectors.collector_base import Collector



class BinanceBTC(Collector):
    _exchange = 'binance'
    symbol = 'BTC/USDT'
    limit = 1000
    def BTCcollector1m():
        from pathlib import Path
        import time
        import os
        directory = Path(r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\coins\BTC\1m')
        timeFrame = '1m'
        filename = 'BTC%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceBTC(timeFrame)
        collector.run_loop(filepath, timestamp='2019-06-29T00:00:00Z',  multiplier=1)
    def BTCcollector3m():
        from pathlib import Path
        import time
        directory = Path(r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\coins\BTC\3m')
        timeFrame = '3m'
        filename = 'BTC%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceBTC(timeFrame)
        collector.run_loop(filepath, timestamp='2019-06-29T00:00:00Z',  multiplier=1)   
    def BTCcollector5m():
        from pathlib import Path
        import time
        directory = Path(r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\coins\BTC\5m')
        timeFrame = '5m'
        filename = 'BTC%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceBTC(timeFrame)
        collector.run_loop(filepath, timestamp='2019-06-29T00:00:00Z',  multiplier=1)
    def BTCcollector15m():
        from pathlib import Path
        import time
        directory = Path(r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\coins\BTC\15m')
        timeFrame = '15m'
        filename = 'BTC%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceBTC(timeFrame)
        collector.run_loop(filepath, timestamp='2019-06-29T00:00:00Z',  multiplier=1)  
    def BTCcollector30m():
        from pathlib import Path
        import time
        directory = Path(r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\coins\BTC\30m')
        timeFrame = '30m'
        filename = 'BTC%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceBTC(timeFrame)
        collector.run_loop(filepath, timestamp='2019-06-29T00:00:00Z',  multiplier=1)
    def BTCcollector1h():
        from pathlib import Path
        import time
        directory = Path(r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\coins\BTC\1h')
        timeFrame = '1h'
        filename = 'BTC%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceBTC(timeFrame)
        collector.run_loop(filepath, timestamp='2019-06-29T00:00:00Z',  multiplier=1)  
    def BTCcollector4h():
        from pathlib import Path
        import time
        directory = Path(r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\coins\BTC\4h')
        timeFrame = '4h'
        filename = 'BTC%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceBTC(timeFrame)
        collector.run_loop(filepath, timestamp='2019-06-29T00:00:00Z',  multiplier=1)
class BinanceETH(Collector):
    _exchange = 'binance'
    symbol = 'ETH/USDT'
    limit = 1000
    def ETHcollector():
        from pathlib import Path
        import time
        directory = Path(__file__).parent
        timeFrame= '1m'
        filename = 'ETH%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceETH(timeFrame)
        collector.run_loop(filepath, timestamp='2018-05-29T00:00:00Z',  multiplier=1)
class BinanceBCH(Collector):
    _exchange = 'binance'
    symbol = 'BCH/USDT'
    limit = 1000
    def BCHcollector():
        from pathlib import Path
        import time
        directory = Path(__file__).parent
        timeFrame= '1m'
        filename = 'BCH%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceBCH(timeFrame)
        collector.run_loop(filepath, timestamp='2018-05-29T00:00:00Z',  multiplier=1)
class BinanceXRP(Collector):
    _exchange = 'binance'
    symbol = 'XRP/USDT'
    limit = 1000
    def XRPcollector():
        from pathlib import Path
        import time
        directory = Path(__file__).parent
        timeFrame= '1m'
        filename = 'XRP%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceXRP(timeFrame)
        collector.run_loop(filepath, timestamp='2018-05-29T00:00:00Z',  multiplier=1)
class BinanceEOS(Collector):
    _exchange = 'binance'
    symbol = 'EOS/USDT'
    limit = 1000
    def EOScollector():
        from pathlib import Path
        import time
        directory = Path(__file__).parent
        timeFrame= '1m'
        filename = 'EOS%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceEOS(timeFrame)
        collector.run_loop(filepath, timestamp='2018-05-29T00:00:00Z',  multiplier=1)
class BinanceLTC(Collector):
    _exchange = 'binance'
    symbol = 'LTC/USDT'
    limit = 1000
    def LTCcollector():
        from pathlib import Path
        import time
        directory = Path(__file__).parent
        timeFrame= '1m'
        filename = 'LTC%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceLTC(timeFrame)
        collector.run_loop(filepath, timestamp='2018-05-29T00:00:00Z',  multiplier=1)
class BinanceTRX(Collector):
    _exchange = 'binance'
    symbol = 'TRX/USDT'
    limit = 1000
    def TRXcollector():
        from pathlib import Path
        import time
        directory = Path(__file__).parent
        timeFrame= '1m'
        filename = 'TRX%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceTRX(timeFrame)
        collector.run_loop(filepath, timestamp='2018-05-29T00:00:00Z',  multiplier=1)
class BinanceETC(Collector):
    _exchange = 'binance'
    symbol = 'ETC/USDT'
    limit = 1000
    def ETCcollector():
        from pathlib import Path
        import time
        directory = Path(__file__).parent
        timeFrame= '1m'
        filename = 'ETC%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceETC(timeFrame)
        collector.run_loop(filepath, timestamp='2018-05-29T00:00:00Z',  multiplier=1)
class BinanceLINK(Collector):
    _exchange = 'binance'
    symbol = 'LINK/USDT'
    limit = 1000
    def LINKcollector():
        from pathlib import Path
        import time
        directory = Path(__file__).parent
        timeFrame= '1m'
        filename = 'LINK%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceLINK(timeFrame)
        collector.run_loop(filepath, timestamp='2018-05-29T00:00:00Z',  multiplier=1)
class BinanceXLM(Collector):
    _exchange = 'binance'
    symbol = 'XLM/USDT'
    limit = 1000
    def XLMcollector():
        from pathlib import Path
        import time
        directory = Path(__file__).parent
        timeFrame= '1m'
        filename = 'XLM%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceXLM(timeFrame)
        collector.run_loop(filepath, timestamp='2018-05-29T00:00:00Z',  multiplier=1)
class BinanceADA(Collector):
    _exchange = 'binance'
    symbol = 'ADA/USDT'
    limit = 1000
    def ADAcollector():
        from pathlib import Path
        import time
        directory = Path(__file__).parent
        timeFrame= '1m'
        filename = 'ADA%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceADA(timeFrame)
        collector.run_loop(filepath, timestamp='2018-05-29T00:00:00Z',  multiplier=1)
class BinanceXMR(Collector):
    _exchange = 'binance'
    symbol = 'XMR/USDT'
    limit = 1000
    def XMRcollector():
        from pathlib import Path
        import time
        directory = Path(__file__).parent
        timeFrame= '1m'
        filename = 'XMR%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceXMR(timeFrame)
        collector.run_loop(filepath, timestamp='2018-05-29T00:00:00Z',  multiplier=1)
class BinanceDASH(Collector):
    _exchange = 'binance'
    symbol = 'DASH/USDT'
    limit = 1000
    def DASHcollector():
        from pathlib import Path
        import time
        directory = Path(__file__).parent
        timeFrame= '1m'
        filename = 'DASH%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceDASH(timeFrame)
        collector.run_loop(filepath, timestamp='2018-05-29T00:00:00Z',  multiplier=1)
class BinanceZEC(Collector):
    _exchange = 'binance'
    symbol = 'ZEC/USDT'
    limit = 1000
    def ZECcollector():
        from pathlib import Path
        import time
        directory = Path(__file__).parent
        timeFrame= '1m'
        filename = 'ZEC%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceZEC(timeFrame)
        collector.run_loop(filepath, timestamp='2018-05-29T00:00:00Z',  multiplier=1)
class BinanceXTZ(Collector):
    _exchange = 'binance'
    symbol = 'XTZ/USDT'
    limit = 1000
    def XTZcollector():
        from pathlib import Path
        import time
        directory = Path(__file__).parent
        timeFrame= '1m'
        filename = 'XTZ%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceXTZ(timeFrame)
        collector.run_loop(filepath, timestamp='2018-05-29T00:00:00Z',  multiplier=1)
class BinanceBNB(Collector):
    _exchange = 'binance'
    symbol = 'BNB/USDT'
    limit = 1000
    def BNBcollector():
        from pathlib import Path
        import time
        directory = Path(__file__).parent
        timeFrame= '1m'
        filename = 'BNB%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceBNB(timeFrame)
        collector.run_loop(filepath, timestamp='2018-05-29T00:00:00Z',  multiplier=1)
class BinanceATOM(Collector):
    _exchange = 'binance'
    symbol = 'ATOM/USDT'
    limit = 1000
    def ATOMcollector():
        from pathlib import Path
        import time
        directory = Path(__file__).parent
        timeFrame= '1m'
        filename = 'ATOM%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceATOM(timeFrame)
        collector.run_loop(filepath, timestamp='2018-05-29T00:00:00Z',  multiplier=1)
class BinanceONT(Collector):
    _exchange = 'binance'
    symbol = 'ONT/USDT'
    limit = 1000
    def ONTcollector():
        from pathlib import Path
        import time
        directory = Path(__file__).parent
        timeFrame= '1m'
        filename = 'ONT%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceONT(timeFrame)
        collector.run_loop(filepath, timestamp='2018-05-29T00:00:00Z',  multiplier=1)
class BinanceIOTA(Collector):
    _exchange = 'binance'
    symbol = 'IOTA/USDT'
    limit = 1000
    def IOTAcollector():
        from pathlib import Path
        import time
        directory = Path(__file__).parent
        timeFrame= '1m'
        filename = 'IOTA%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceIOTA(timeFrame)
        collector.run_loop(filepath, timestamp='2018-05-29T00:00:00Z',  multiplier=1)
class BinanceBAT(Collector):
    _exchange = 'binance'
    symbol = 'BAT/USDT'
    limit = 1000
    def BATcollector():
        from pathlib import Path
        import time
        directory = Path(__file__).parent
        timeFrame= '1m'
        filename = 'BAT%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceBAT(timeFrame)
        collector.run_loop(filepath, timestamp='2018-05-29T00:00:00Z',  multiplier=1)
class BinanceVET(Collector):
    _exchange = 'binance'
    symbol = 'VET/USDT'
    limit = 1000
    def VETcollector():
        from pathlib import Path
        import time
        directory = Path(__file__).parent
        timeFrame= '1m'
        filename = 'VET%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceVET(timeFrame)
        collector.run_loop(filepath, timestamp='2018-05-29T00:00:00Z',  multiplier=1)
class BinanceNEO(Collector):
    _exchange = 'binance'
    symbol = 'NEO/USDT'
    limit = 1000
    def NEOcollector():
        from pathlib import Path
        import time
        directory = Path(__file__).parent
        timeFrame= '1m'
        filename = 'NEO%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceNEO(timeFrame)
        collector.run_loop(filepath, timestamp='2018-05-29T00:00:00Z',  multiplier=1)
class BinanceQTUM(Collector):
    _exchange = 'binance'
    symbol = 'ONT/USDT'
    limit = 1000
    def QTUMcollector():
        from pathlib import Path
        import time
        directory = Path(__file__).parent
        timeFrame= '1m'
        filename = 'QTUM%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceQTUM(timeFrame)
        collector.run_loop(filepath, timestamp='2018-05-29T00:00:00Z',  multiplier=1)
class BinanceIOST(Collector):
    _exchange = 'binance'
    symbol = 'IOST/USDT'
    limit = 1000
    def IOSTcollector():
        from pathlib import Path
        import time
        directory = Path(__file__).parent
        timeFrame= '1m'
        filename = 'IOST%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceIOST(timeFrame)
        collector.run_loop(filepath, timestamp='2018-05-29T00:00:00Z',  multiplier=1)
class BinanceTHETA(Collector):
    _exchange = 'binance'
    symbol = 'THETA/USDT'
    limit = 1000
    def THETAcollector1m():
        from pathlib import Path
        import time
        import os
        directory = Path(r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\coins\THETA\1m')
        timeFrame = '1m'
        filename = 'THETA%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceTHETA(timeFrame)
        collector.run_loop(filepath, timestamp='2019-06-29T00:00:00Z',  multiplier=1)
    def THETAcollector3m():
        from pathlib import Path
        import time
        directory = Path(r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\coins\THETA\3m')
        timeFrame = '3m'
        filename = 'BTC%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceTHETA(timeFrame)
        collector.run_loop(filepath, timestamp='2019-06-29T00:00:00Z',  multiplier=1)   
    def THETAcollector5m():
        from pathlib import Path
        import time
        directory = Path(r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\coins\THETA\5m')
        timeFrame = '5m'
        filename = 'BTTHETAC%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceTHETA(timeFrame)
        collector.run_loop(filepath, timestamp='2019-06-29T00:00:00Z',  multiplier=1)
    def THETAcollector15m():
        from pathlib import Path
        import time
        directory = Path(r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\coins\THETA\15m')
        timeFrame = '15m'
        filename = 'THETA%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceTHETA(timeFrame)
        collector.run_loop(filepath, timestamp='2019-06-29T00:00:00Z',  multiplier=1)  
    def THETAcollector30m():
        from pathlib import Path
        import time
        directory = Path(r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\coins\THETA\30m')
        timeFrame = '30m'
        filename = 'THETA%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceTHETA(timeFrame)
        collector.run_loop(filepath, timestamp='2019-06-29T00:00:00Z',  multiplier=1)
    def THETAcollector1h():
        from pathlib import Path
        import time
        directory = Path(r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\coins\THETA\1h')
        timeFrame = '1h'
        filename = 'THETA%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceTHETA(timeFrame)
        collector.run_loop(filepath, timestamp='2019-06-29T00:00:00Z',  multiplier=1)  
    def THETAcollector4h():
        from pathlib import Path
        import time
        directory = Path(r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\coins\THETA\4h')
        timeFrame = '4h'
        filename = 'THETA%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceTHETA(timeFrame)
        collector.run_loop(filepath, timestamp='2019-06-29T00:00:00Z',  multiplier=1)

