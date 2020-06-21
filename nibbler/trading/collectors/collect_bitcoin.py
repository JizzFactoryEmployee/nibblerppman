from nibbler import trading as td
import time

def livecollectorBTC():


    from pathlib import Path
    directory = Path(__file__).parent
    filename = 'ppman.csv'
    filepath = directory/filename
    collector = td.collectors.BinanceBTC('5m')
    collector.run(filepath, multiplier=1)

livecollectorBTC()
# # def livecollectorETH():


#     from pathlib import Path
#     directory = Path(__file__).parent
#     filename = 'test2.csv'
#     filepath = directory/filename
#     collector = td.collectors.BinanceETH('1h')
#     while 1 < 1000:
#         collector.run(filepath, multiplier=1)

# def livecollectorLINK():


#     from pathlib import Path
#     directory = Path(__file__).parent
#     filename = '11111.csv'
#     filepath = directory/filename
#     collector = td.collectors.BinanceLINK('1m')
#     collector.run_loop(filepath, timestamp='2013-01-01T00:00:00Z',  multiplier=1)


# livecollectorLINK()

# from nibbler.trading.collectors.Binance_Collector_eth import runner

# runner()