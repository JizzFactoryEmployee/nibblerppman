from nibbler import trading as td
import time

def livecollector1():


    from pathlib import Path
    directory = Path(__file__).parent
    filename = 'file1.csv'
    filepath = directory/filename
    collector = td.collectors.BinanceETH('1h')
    while 1 < 1000:
        collector.run(filepath, multiplier=1)

