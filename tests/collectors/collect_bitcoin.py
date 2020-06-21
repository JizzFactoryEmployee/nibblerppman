from nibbler import trading as td

def livecollector():


    from pathlib import Path
    directory = Path(__file__).parent
    filename = 'btcupload1.csv'
    filepath = directory/filename
    collector = td.collectors.BinanceBTC('1d')
    import time
    while 1 < 1000:
        collector.run(filepath, multiplier=1)
        print('going to bed')
        time.sleep(20)

livecollector()