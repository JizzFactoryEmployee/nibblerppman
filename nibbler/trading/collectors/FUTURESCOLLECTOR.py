import os
import sys
import csv
import pandas as pd
import numpy as np
from pathlib import Path
# -----------------------------------------------------------------------------

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root + '/python')

import ccxt  # noqa: E402

class bigpp_collector():

    def __init__(self):
        pass
    def retry_fetch_ohlcv(exchange, max_retries, symbol, timeframe, since, limit):
        num_retries = 0
        try:
            num_retries += 1
            ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since, limit)
            # print('Fetched', len(ohlcv), symbol, 'candles from', exchange.iso8601 (ohlcv[0][0]), 'to', exchange.iso8601 (ohlcv[-1][0]))
            return ohlcv
        except Exception:
            if num_retries > max_retries:
                raise  # Exception('Failed to fetch', timeframe, symbol, 'OHLCV in', max_retries, 'attempts')
def retry_fetch_ohlcv(exchange, max_retries, symbol, timeframe, since, limit):
    num_retries = 0
    try:
        num_retries += 1
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since, limit)
        # print('Fetched', len(ohlcv), symbol, 'candles from', exchange.iso8601 (ohlcv[0][0]), 'to', exchange.iso8601 (ohlcv[-1][0]))
        return ohlcv
    except Exception:
        if num_retries > max_retries:
            raise  # Exception('Failed to fetch', timeframe, symbol, 'OHLCV in', max_retries, 'attempts')
def scrape_ohlcv(exchange, max_retries, symbol, timeframe, since, limit):
    earliest_timestamp = exchange.milliseconds()
    timeframe_duration_in_seconds = exchange.parse_timeframe(timeframe)
    timeframe_duration_in_ms = timeframe_duration_in_seconds * 1000
    timedelta = limit * timeframe_duration_in_ms
    all_ohlcv = []
    while True:
        fetch_since = earliest_timestamp - timedelta
        ohlcv = retry_fetch_ohlcv(exchange, max_retries, symbol, timeframe, fetch_since, limit)
        # if we have reached the beginning of history
        try:
            if ohlcv[0][0] >= earliest_timestamp:
                break
        except:
            break
        earliest_timestamp = ohlcv[0][0]
        all_ohlcv = ohlcv + all_ohlcv
        print(len(all_ohlcv), 'candles in total from', exchange.iso8601(all_ohlcv[0][0]), 'to', exchange.iso8601(all_ohlcv[-1][0]))
        # if we have reached the checkpoint
        if fetch_since < since:
            break
    return all_ohlcv
def write_to_csv(filename, data):
    with open(filename, mode='w', newline='') as output_file:
        csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerows(data)
def scrape_candles_to_csv(filename, exchange_id, max_retries, symbol, timeframe, since, limit):
    # instantiate the exchange by id
    exchange = getattr(ccxt, exchange_id)({
        'enableRateLimit': True,  # required by the Manual
    })
    # convert since from string to milliseconds integer if needed
    if isinstance(since, str):
        since = exchange.parse8601(since)
    # preload all markets from the exchange
    exchange.load_markets()
    # fetch all candles
    ohlcv = scrape_ohlcv(exchange, max_retries, symbol, timeframe, since, limit)
    
    filename = Path(filename)

    df = pd.DataFrame(columns = ['Date_Time','Open_price','High_price','Low_price','Close_price','Volume'])
    df = df.assign(**dict(zip(df.keys(),np.array(ohlcv).T)))

    if filename.exists():
        original = pd.read_csv(filename)
        df       = original.append(df).drop_duplicates(subset='Date_Time', keep='first', inplace=False)
    # symbol = symbol.split('/')
    # symbol1 = symbol[0]
    # symbol2 = symbol[1]
    # df['pair_1'] = symbol1
    # df['pair_2'] = symbol2
    # df['id'] = ""
    df = df[['Date_Time', 'Open_price', 'High_price', 'Low_price', 'Close_price', 'Volume']]

    df.to_csv(filename,index =False)
if __name__ == "__main__":
    import datetime
    import time
    timeFrame = '1h'
    filename     = r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\BTC%s.csv'%timeFrame
    formatString = "%Y-%m-%dT%H:%M:%SZ"
    while True:
        try:
            oldDF    = pd.read_csv(filename)
            lastDatatimeStamp = oldDF.DateTime.values[-1]*10**(-3)
            dt_object = datetime.datetime.fromtimestamp(int(lastDatatimeStamp))
            formattedTimestamp = datetime.datetime.now().strftime(formatString)
        except:
            formattedTimestamp ='2016-05-25T00:00:00Z'
        scrape_candles_to_csv(filename, 'binance', 10, 'BTC/USDT', timeFrame, formattedTimestamp, 1000)
        newDF = pd.read_csv(filename)
        newDateTime  = int(newDF.iloc[-1]['Date_Time']*10**(-3))
        newDateTime  = datetime.datetime.fromtimestamp(newDateTime).strftime(formatString)
        NewTimeStamp = \
        f"""
        Date_Time:{newDateTime},
        Open_price    :{newDF.iloc[-1]['Open_price']}, 
        High_price    :{newDF.iloc[-1]['High_price']}, 
        Low_price     :{newDF.iloc[-1]['Low_price']}, 
        Close_price   :{newDF.iloc[-1]['Close_price']}, 
        Volume  :{newDF.iloc[-1]['Volume']}
        """
        print(NewTimeStamp)
        time.sleep(5)


def BTCrunner():
    import datetime
    import time
    timeFrame = '1h'
    filename     = r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\BTC%s.csv'%timeFrame
    formatString = "%Y-%m-%dT%H:%M:%SZ"
    while True:
        try:
            oldDF    = pd.read_csv(filename)
            lastDatatimeStamp = oldDF.DateTime.values[-1]*10**(-3)
            dt_object = datetime.datetime.fromtimestamp(int(lastDatatimeStamp))
            formattedTimestamp = datetime.datetime.now().strftime(formatString)
        except:
            formattedTimestamp ='2016-05-25T00:00:00Z'
        scrape_candles_to_csv(filename, 'binance', 10, 'BTC/USDT', timeFrame, formattedTimestamp, 1000)
        newDF = pd.read_csv(filename)
        newDateTime  = int(newDF.iloc[-1]['Date_Time']*10**(-3))
        newDateTime  = datetime.datetime.fromtimestamp(newDateTime).strftime(formatString)
        NewTimeStamp = \
        f"""
        Date_Time:{newDateTime},
        Open_price    :{newDF.iloc[-1]['Open_price']}, 
        High_price    :{newDF.iloc[-1]['High_price']}, 
        Low_price     :{newDF.iloc[-1]['Low_price']}, 
        Close_price   :{newDF.iloc[-1]['Close_price']}, 
        Volume  :{newDF.iloc[-1]['Volume']}
        """
        print(NewTimeStamp)
        time.sleep(10)
def ETHrunner():
    import datetime
    import time
    timeFrame = '1m'
    filename     = r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\ETH%s.csv'%timeFrame
    formatString = "%Y-%m-%dT%H:%M:%SZ"
    while True:
        try:
            oldDF    = pd.read_csv(filename)
            lastDatatimeStamp = oldDF.DateTime.values[-1]*10**(-3)
            dt_object = datetime.datetime.fromtimestamp(int(lastDatatimeStamp))
            formattedTimestamp = datetime.datetime.now().strftime(formatString)
        except:
            formattedTimestamp ='2016-05-25T00:00:00Z'
        scrape_candles_to_csv(filename, 'binance', 10, 'ETH/USDT', timeFrame, formattedTimestamp, 250)
        newDF = pd.read_csv(filename)
        newDateTime  = int(newDF.iloc[-1]['Date_Time']*10**(-3))
        newDateTime  = datetime.datetime.fromtimestamp(newDateTime).strftime(formatString)
        NewTimeStamp = \
        f"""
        Date_Time:{newDateTime},
        Open_price    :{newDF.iloc[-1]['Open_price']}, 
        High_price    :{newDF.iloc[-1]['High_price']}, 
        Low_price     :{newDF.iloc[-1]['Low_price']}, 
        Close_price   :{newDF.iloc[-1]['Close_price']}, 
        Volume  :{newDF.iloc[-1]['Volume']}
        """
        print(NewTimeStamp)
        time.sleep(61)
def BCHrunner():
    import datetime
    import time
    timeFrame = '1m'
    filename     = r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\BCH%s.csv'%timeFrame
    formatString = "%Y-%m-%dT%H:%M:%SZ"
    while True:
        try:
            oldDF    = pd.read_csv(filename)
            lastDatatimeStamp = oldDF.DateTime.values[-1]*10**(-3)
            dt_object = datetime.datetime.fromtimestamp(int(lastDatatimeStamp))
            formattedTimestamp = datetime.datetime.now().strftime(formatString)
        except:
            formattedTimestamp ='2016-05-25T00:00:00Z'
        scrape_candles_to_csv(filename, 'binance', 10, 'BCH/USDT', timeFrame, formattedTimestamp, 100)
        newDF = pd.read_csv(filename)
        newDateTime  = int(newDF.iloc[-1]['Date_Time']*10**(-3))
        newDateTime  = datetime.datetime.fromtimestamp(newDateTime).strftime(formatString)
        NewTimeStamp = \
        f"""
        Date_Time:{newDateTime},
        Open_price    :{newDF.iloc[-1]['Open_price']}, 
        High_price    :{newDF.iloc[-1]['High_price']}, 
        Low_price     :{newDF.iloc[-1]['Low_price']}, 
        Close_price   :{newDF.iloc[-1]['Close_price']}, 
        Volume  :{newDF.iloc[-1]['Volume']}
        """
        print(NewTimeStamp)
        time.sleep(61)
def XRPrunner():
    import datetime
    import time
    timeFrame = '1m'
    filename     = r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\XRP%s.csv'%timeFrame
    formatString = "%Y-%m-%dT%H:%M:%SZ"
    while True:
        try:
            oldDF    = pd.read_csv(filename)
            lastDatatimeStamp = oldDF.DateTime.values[-1]*10**(-3)
            dt_object = datetime.datetime.fromtimestamp(int(lastDatatimeStamp))
            formattedTimestamp = datetime.datetime.now().strftime(formatString)
        except:
            formattedTimestamp ='2016-05-25T00:00:00Z'
        scrape_candles_to_csv(filename, 'binance', 10, 'XRP/USDT', timeFrame, formattedTimestamp, 100)
        newDF = pd.read_csv(filename)
        newDateTime  = int(newDF.iloc[-1]['Date_Time']*10**(-3))
        newDateTime  = datetime.datetime.fromtimestamp(newDateTime).strftime(formatString)
        NewTimeStamp = \
        f"""
        Date_Time:{newDateTime},
        Open_price    :{newDF.iloc[-1]['Open_price']}, 
        High_price    :{newDF.iloc[-1]['High_price']}, 
        Low_price     :{newDF.iloc[-1]['Low_price']}, 
        Close_price   :{newDF.iloc[-1]['Close_price']}, 
        Volume  :{newDF.iloc[-1]['Volume']}
        """
        print(NewTimeStamp)
        time.sleep(61)    
def EOSrunner():
    import datetime
    import time
    timeFrame = '1m'
    filename     = r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\EOS%s.csv'%timeFrame
    formatString = "%Y-%m-%dT%H:%M:%SZ"
    while True:
        try:
            oldDF    = pd.read_csv(filename)
            lastDatatimeStamp = oldDF.DateTime.values[-1]*10**(-3)
            dt_object = datetime.datetime.fromtimestamp(int(lastDatatimeStamp))
            formattedTimestamp = datetime.datetime.now().strftime(formatString)
        except:
            formattedTimestamp ='2016-05-25T00:00:00Z'
        scrape_candles_to_csv(filename, 'binance', 10, 'EOS/USDT', timeFrame, formattedTimestamp, 100)
        newDF = pd.read_csv(filename)
        newDateTime  = int(newDF.iloc[-1]['Date_Time']*10**(-3))
        newDateTime  = datetime.datetime.fromtimestamp(newDateTime).strftime(formatString)
        NewTimeStamp = \
        f"""
        Date_Time:{newDateTime},
        Open_price    :{newDF.iloc[-1]['Open_price']}, 
        High_price    :{newDF.iloc[-1]['High_price']}, 
        Low_price     :{newDF.iloc[-1]['Low_price']}, 
        Close_price   :{newDF.iloc[-1]['Close_price']}, 
        Volume  :{newDF.iloc[-1]['Volume']}
        """
        print(NewTimeStamp)
        time.sleep(61)
def LTCrunner():
    import datetime
    import time
    timeFrame = '1m'
    filename     = r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\LTC%s.csv'%timeFrame
    formatString = "%Y-%m-%dT%H:%M:%SZ"
    while True:
        try:
            oldDF    = pd.read_csv(filename)
            lastDatatimeStamp = oldDF.DateTime.values[-1]*10**(-3)
            dt_object = datetime.datetime.fromtimestamp(int(lastDatatimeStamp))
            formattedTimestamp = datetime.datetime.now().strftime(formatString)
        except:
            formattedTimestamp ='2016-05-25T00:00:00Z'
        scrape_candles_to_csv(filename, 'binance', 10, 'LTC/USDT', timeFrame, formattedTimestamp, 100)
        newDF = pd.read_csv(filename)
        newDateTime  = int(newDF.iloc[-1]['Date_Time']*10**(-3))
        newDateTime  = datetime.datetime.fromtimestamp(newDateTime).strftime(formatString)
        NewTimeStamp = \
        f"""
        Date_Time:{newDateTime},
        Open_price    :{newDF.iloc[-1]['Open_price']}, 
        High_price    :{newDF.iloc[-1]['High_price']}, 
        Low_price     :{newDF.iloc[-1]['Low_price']}, 
        Close_price   :{newDF.iloc[-1]['Close_price']}, 
        Volume  :{newDF.iloc[-1]['Volume']}
        """
        print(NewTimeStamp)
        time.sleep(61)
def TRXrunner():
    import datetime
    import time
    timeFrame = '1m'
    filename     = r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\TRX%s.csv'%timeFrame
    formatString = "%Y-%m-%dT%H:%M:%SZ"
    while True:
        try:
            oldDF    = pd.read_csv(filename)
            lastDatatimeStamp = oldDF.DateTime.values[-1]*10**(-3)
            dt_object = datetime.datetime.fromtimestamp(int(lastDatatimeStamp))
            formattedTimestamp = datetime.datetime.now().strftime(formatString)
        except:
            formattedTimestamp ='2016-05-25T00:00:00Z'
        scrape_candles_to_csv(filename, 'binance', 10, 'TRX/USDT', timeFrame, formattedTimestamp, 100)
        newDF = pd.read_csv(filename)
        newDateTime  = int(newDF.iloc[-1]['Date_Time']*10**(-3))
        newDateTime  = datetime.datetime.fromtimestamp(newDateTime).strftime(formatString)
        NewTimeStamp = \
        f"""
        Date_Time:{newDateTime},
        Open_price    :{newDF.iloc[-1]['Open_price']}, 
        High_price    :{newDF.iloc[-1]['High_price']}, 
        Low_price     :{newDF.iloc[-1]['Low_price']}, 
        Close_price   :{newDF.iloc[-1]['Close_price']}, 
        Volume  :{newDF.iloc[-1]['Volume']}
        """
        print(NewTimeStamp)
        time.sleep(61)
def ETCrunner():
    import datetime
    import time
    timeFrame = '1m'
    filename     = r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\ETC%s.csv'%timeFrame
    formatString = "%Y-%m-%dT%H:%M:%SZ"
    while True:
        try:
            oldDF    = pd.read_csv(filename)
            lastDatatimeStamp = oldDF.DateTime.values[-1]*10**(-3)
            dt_object = datetime.datetime.fromtimestamp(int(lastDatatimeStamp))
            formattedTimestamp = datetime.datetime.now().strftime(formatString)
        except:
            formattedTimestamp ='2016-05-25T00:00:00Z'
        scrape_candles_to_csv(filename, 'binance', 10, 'ETC/USDT', timeFrame, formattedTimestamp, 100)
        newDF = pd.read_csv(filename)
        newDateTime  = int(newDF.iloc[-1]['Date_Time']*10**(-3))
        newDateTime  = datetime.datetime.fromtimestamp(newDateTime).strftime(formatString)
        NewTimeStamp = \
        f"""
        Date_Time:{newDateTime},
        Open_price    :{newDF.iloc[-1]['Open_price']}, 
        High_price    :{newDF.iloc[-1]['High_price']}, 
        Low_price     :{newDF.iloc[-1]['Low_price']}, 
        Close_price   :{newDF.iloc[-1]['Close_price']}, 
        Volume  :{newDF.iloc[-1]['Volume']}
        """
        print(NewTimeStamp)
        time.sleep(61)
def LINKrunner():
    import datetime
    import time
    timeFrame = '1m'
    filename     = r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\LINK%s.csv'%timeFrame
    formatString = "%Y-%m-%dT%H:%M:%SZ"
    while True:
        try:
            oldDF    = pd.read_csv(filename)
            lastDatatimeStamp = oldDF.DateTime.values[-1]*10**(-3)
            dt_object = datetime.datetime.fromtimestamp(int(lastDatatimeStamp))
            formattedTimestamp = datetime.datetime.now().strftime(formatString)
        except:
            formattedTimestamp ='2016-05-25T00:00:00Z'
        scrape_candles_to_csv(filename, 'binance', 10, 'LINK/USDT', timeFrame, formattedTimestamp, 100)
        newDF = pd.read_csv(filename)
        newDateTime  = int(newDF.iloc[-1]['Date_Time']*10**(-3))
        newDateTime  = datetime.datetime.fromtimestamp(newDateTime).strftime(formatString)
        NewTimeStamp = \
        f"""
        Date_Time:{newDateTime},
        Open_price    :{newDF.iloc[-1]['Open_price']}, 
        High_price    :{newDF.iloc[-1]['High_price']}, 
        Low_price     :{newDF.iloc[-1]['Low_price']}, 
        Close_price   :{newDF.iloc[-1]['Close_price']}, 
        Volume  :{newDF.iloc[-1]['Volume']}
        """
        print(NewTimeStamp)
        time.sleep(61)
def XLMrunner():
    import datetime
    import time
    timeFrame = '1m'
    filename     = r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\XLM%s.csv'%timeFrame
    formatString = "%Y-%m-%dT%H:%M:%SZ"
    while True:
        try:
            oldDF    = pd.read_csv(filename)
            lastDatatimeStamp = oldDF.DateTime.values[-1]*10**(-3)
            dt_object = datetime.datetime.fromtimestamp(int(lastDatatimeStamp))
            formattedTimestamp = datetime.datetime.now().strftime(formatString)
        except:
            formattedTimestamp ='2016-05-25T00:00:00Z'
        scrape_candles_to_csv(filename, 'binance', 10, 'XLM/USDT', timeFrame, formattedTimestamp, 100)
        newDF = pd.read_csv(filename)
        newDateTime  = int(newDF.iloc[-1]['Date_Time']*10**(-3))
        newDateTime  = datetime.datetime.fromtimestamp(newDateTime).strftime(formatString)
        NewTimeStamp = \
        f"""
        Date_Time:{newDateTime},
        Open_price    :{newDF.iloc[-1]['Open_price']}, 
        High_price    :{newDF.iloc[-1]['High_price']}, 
        Low_price     :{newDF.iloc[-1]['Low_price']}, 
        Close_price   :{newDF.iloc[-1]['Close_price']}, 
        Volume  :{newDF.iloc[-1]['Volume']}
        """
        print(NewTimeStamp)
        time.sleep(61)
def ADArunner():
    import datetime
    import time
    timeFrame = '1m'
    filename     = r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\ADA%s.csv'%timeFrame
    formatString = "%Y-%m-%dT%H:%M:%SZ"
    while True:
        try:
            oldDF    = pd.read_csv(filename)
            lastDatatimeStamp = oldDF.DateTime.values[-1]*10**(-3)
            dt_object = datetime.datetime.fromtimestamp(int(lastDatatimeStamp))
            formattedTimestamp = datetime.datetime.now().strftime(formatString)
        except:
            formattedTimestamp ='2016-05-25T00:00:00Z'
        scrape_candles_to_csv(filename, 'binance', 10, 'ADA/USDT', timeFrame, formattedTimestamp, 100)
        newDF = pd.read_csv(filename)
        newDateTime  = int(newDF.iloc[-1]['Date_Time']*10**(-3))
        newDateTime  = datetime.datetime.fromtimestamp(newDateTime).strftime(formatString)
        NewTimeStamp = \
        f"""
        Date_Time:{newDateTime},
        Open_price    :{newDF.iloc[-1]['Open_price']}, 
        High_price    :{newDF.iloc[-1]['High_price']}, 
        Low_price     :{newDF.iloc[-1]['Low_price']}, 
        Close_price   :{newDF.iloc[-1]['Close_price']}, 
        Volume  :{newDF.iloc[-1]['Volume']}
        """
        print(NewTimeStamp)
        time.sleep(61)
def XMRrunner():
    import datetime
    import time
    timeFrame = '1m'
    filename     = r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\XMR%s.csv'%timeFrame
    formatString = "%Y-%m-%dT%H:%M:%SZ"
    while True:
        try:
            oldDF    = pd.read_csv(filename)
            lastDatatimeStamp = oldDF.DateTime.values[-1]*10**(-3)
            dt_object = datetime.datetime.fromtimestamp(int(lastDatatimeStamp))
            formattedTimestamp = datetime.datetime.now().strftime(formatString)
        except:
            formattedTimestamp ='2016-05-25T00:00:00Z'
        scrape_candles_to_csv(filename, 'binance', 10, 'XMR/USDT', timeFrame, formattedTimestamp, 100)
        newDF = pd.read_csv(filename)
        newDateTime  = int(newDF.iloc[-1]['Date_Time']*10**(-3))
        newDateTime  = datetime.datetime.fromtimestamp(newDateTime).strftime(formatString)
        NewTimeStamp = \
        f"""
        Date_Time:{newDateTime},
        Open_price    :{newDF.iloc[-1]['Open_price']}, 
        High_price    :{newDF.iloc[-1]['High_price']}, 
        Low_price     :{newDF.iloc[-1]['Low_price']}, 
        Close_price   :{newDF.iloc[-1]['Close_price']}, 
        Volume  :{newDF.iloc[-1]['Volume']}
        """
        print(NewTimeStamp)
        time.sleep(61)
def DASHrunner():
    import datetime
    import time
    timeFrame = '1m'
    filename     = r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\DASH%s.csv'%timeFrame
    formatString = "%Y-%m-%dT%H:%M:%SZ"
    while True:
        try:
            oldDF    = pd.read_csv(filename)
            lastDatatimeStamp = oldDF.DateTime.values[-1]*10**(-3)
            dt_object = datetime.datetime.fromtimestamp(int(lastDatatimeStamp))
            formattedTimestamp = datetime.datetime.now().strftime(formatString)
        except:
            formattedTimestamp ='2016-05-25T00:00:00Z'
        scrape_candles_to_csv(filename, 'binance', 10, 'DASH/USDT', timeFrame, formattedTimestamp, 100)
        newDF = pd.read_csv(filename)
        newDateTime  = int(newDF.iloc[-1]['Date_Time']*10**(-3))
        newDateTime  = datetime.datetime.fromtimestamp(newDateTime).strftime(formatString)
        NewTimeStamp = \
        f"""
        Date_Time:{newDateTime},
        Open_price    :{newDF.iloc[-1]['Open_price']}, 
        High_price    :{newDF.iloc[-1]['High_price']}, 
        Low_price     :{newDF.iloc[-1]['Low_price']}, 
        Close_price   :{newDF.iloc[-1]['Close_price']}, 
        Volume  :{newDF.iloc[-1]['Volume']}
        """
        print(NewTimeStamp)
        time.sleep(61)
def ZECrunner():
    import datetime
    import time
    timeFrame = '1m'
    filename     = r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\ZEC%s.csv'%timeFrame
    formatString = "%Y-%m-%dT%H:%M:%SZ"
    while True:
        try:
            oldDF    = pd.read_csv(filename)
            lastDatatimeStamp = oldDF.DateTime.values[-1]*10**(-3)
            dt_object = datetime.datetime.fromtimestamp(int(lastDatatimeStamp))
            formattedTimestamp = datetime.datetime.now().strftime(formatString)
        except:
            formattedTimestamp ='2016-05-25T00:00:00Z'
        scrape_candles_to_csv(filename, 'binance', 10, 'ZEC/USDT', timeFrame, formattedTimestamp, 100)
        newDF = pd.read_csv(filename)
        newDateTime  = int(newDF.iloc[-1]['Date_Time']*10**(-3))
        newDateTime  = datetime.datetime.fromtimestamp(newDateTime).strftime(formatString)
        NewTimeStamp = \
        f"""
        Date_Time:{newDateTime},
        Open_price    :{newDF.iloc[-1]['Open_price']}, 
        High_price    :{newDF.iloc[-1]['High_price']}, 
        Low_price     :{newDF.iloc[-1]['Low_price']}, 
        Close_price   :{newDF.iloc[-1]['Close_price']}, 
        Volume  :{newDF.iloc[-1]['Volume']}
        """
        print(NewTimeStamp)
        time.sleep(61)
def XTZrunner():
    import datetime
    import time
    timeFrame = '1m'
    filename     = r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\XTZ%s.csv'%timeFrame
    formatString = "%Y-%m-%dT%H:%M:%SZ"
    while True:
        try:
            oldDF    = pd.read_csv(filename)
            lastDatatimeStamp = oldDF.DateTime.values[-1]*10**(-3)
            dt_object = datetime.datetime.fromtimestamp(int(lastDatatimeStamp))
            formattedTimestamp = datetime.datetime.now().strftime(formatString)
        except:
            formattedTimestamp ='2016-05-25T00:00:00Z'
        scrape_candles_to_csv(filename, 'binance', 10, 'XTZ/USDT', timeFrame, formattedTimestamp, 100)
        newDF = pd.read_csv(filename)
        newDateTime  = int(newDF.iloc[-1]['Date_Time']*10**(-3))
        newDateTime  = datetime.datetime.fromtimestamp(newDateTime).strftime(formatString)
        NewTimeStamp = \
        f"""
        Date_Time:{newDateTime},
        Open_price    :{newDF.iloc[-1]['Open_price']}, 
        High_price    :{newDF.iloc[-1]['High_price']}, 
        Low_price     :{newDF.iloc[-1]['Low_price']}, 
        Close_price   :{newDF.iloc[-1]['Close_price']}, 
        Volume  :{newDF.iloc[-1]['Volume']}
        """
        print(NewTimeStamp)
        time.sleep(61)
def BNBrunner():
    import datetime
    import time
    timeFrame = '1m'
    filename     = r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\BNB%s.csv'%timeFrame
    formatString = "%Y-%m-%dT%H:%M:%SZ"
    while True:
        try:
            oldDF    = pd.read_csv(filename)
            lastDatatimeStamp = oldDF.DateTime.values[-1]*10**(-3)
            dt_object = datetime.datetime.fromtimestamp(int(lastDatatimeStamp))
            formattedTimestamp = datetime.datetime.now().strftime(formatString)
        except:
            formattedTimestamp ='2016-05-25T00:00:00Z'
        scrape_candles_to_csv(filename, 'binance', 10, 'BNB/USDT', timeFrame, formattedTimestamp, 100)
        newDF = pd.read_csv(filename)
        newDateTime  = int(newDF.iloc[-1]['Date_Time']*10**(-3))
        newDateTime  = datetime.datetime.fromtimestamp(newDateTime).strftime(formatString)
        NewTimeStamp = \
        f"""
        Date_Time:{newDateTime},
        Open_price    :{newDF.iloc[-1]['Open_price']}, 
        High_price    :{newDF.iloc[-1]['High_price']}, 
        Low_price     :{newDF.iloc[-1]['Low_price']}, 
        Close_price   :{newDF.iloc[-1]['Close_price']}, 
        Volume  :{newDF.iloc[-1]['Volume']}
        """
        print(NewTimeStamp)
        time.sleep(61)
def ATOMrunner():
    import datetime
    import time
    timeFrame = '1m'
    filename     = r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\ATOM%s.csv'%timeFrame
    formatString = "%Y-%m-%dT%H:%M:%SZ"
    while True:
        try:
            oldDF    = pd.read_csv(filename)
            lastDatatimeStamp = oldDF.DateTime.values[-1]*10**(-3)
            dt_object = datetime.datetime.fromtimestamp(int(lastDatatimeStamp))
            formattedTimestamp = datetime.datetime.now().strftime(formatString)
        except:
            formattedTimestamp ='2016-05-25T00:00:00Z'
        scrape_candles_to_csv(filename, 'binance', 10, 'ATOM/USDT', timeFrame, formattedTimestamp, 100)
        newDF = pd.read_csv(filename)
        newDateTime  = int(newDF.iloc[-1]['Date_Time']*10**(-3))
        newDateTime  = datetime.datetime.fromtimestamp(newDateTime).strftime(formatString)
        NewTimeStamp = \
        f"""
        Date_Time:{newDateTime},
        Open_price    :{newDF.iloc[-1]['Open_price']}, 
        High_price    :{newDF.iloc[-1]['High_price']}, 
        Low_price     :{newDF.iloc[-1]['Low_price']}, 
        Close_price   :{newDF.iloc[-1]['Close_price']}, 
        Volume  :{newDF.iloc[-1]['Volume']}
        """
        print(NewTimeStamp)
        time.sleep(61)
def ONTrunner():
    import datetime
    import time
    timeFrame = '1m'
    filename     = r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\ONT%s.csv'%timeFrame
    formatString = "%Y-%m-%dT%H:%M:%SZ"
    while True:
        try:
            oldDF    = pd.read_csv(filename)
            lastDatatimeStamp = oldDF.DateTime.values[-1]*10**(-3)
            dt_object = datetime.datetime.fromtimestamp(int(lastDatatimeStamp))
            formattedTimestamp = datetime.datetime.now().strftime(formatString)
        except:
            formattedTimestamp ='2016-05-25T00:00:00Z'
        scrape_candles_to_csv(filename, 'binance', 10, 'ONT/USDT', timeFrame, formattedTimestamp, 100)
        newDF = pd.read_csv(filename)
        newDateTime  = int(newDF.iloc[-1]['Date_Time']*10**(-3))
        newDateTime  = datetime.datetime.fromtimestamp(newDateTime).strftime(formatString)
        NewTimeStamp = \
        f"""
        Date_Time:{newDateTime},
        Open_price    :{newDF.iloc[-1]['Open_price']}, 
        High_price    :{newDF.iloc[-1]['High_price']}, 
        Low_price     :{newDF.iloc[-1]['Low_price']}, 
        Close_price   :{newDF.iloc[-1]['Close_price']}, 
        Volume  :{newDF.iloc[-1]['Volume']}
        """
        print(NewTimeStamp)
        time.sleep(61)
def IOTArunner():
    import datetime
    import time
    timeFrame = '1m'
    filename     = r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\IOTA%s.csv'%timeFrame
    formatString = "%Y-%m-%dT%H:%M:%SZ"
    while True:
        try:
            oldDF    = pd.read_csv(filename)
            lastDatatimeStamp = oldDF.DateTime.values[-1]*10**(-3)
            dt_object = datetime.datetime.fromtimestamp(int(lastDatatimeStamp))
            formattedTimestamp = datetime.datetime.now().strftime(formatString)
        except:
            formattedTimestamp ='2016-05-25T00:00:00Z'
        scrape_candles_to_csv(filename, 'binance', 10, 'IOTA/USDT', timeFrame, formattedTimestamp, 100)
        newDF = pd.read_csv(filename)
        newDateTime  = int(newDF.iloc[-1]['Date_Time']*10**(-3))
        newDateTime  = datetime.datetime.fromtimestamp(newDateTime).strftime(formatString)
        NewTimeStamp = \
        f"""
        Date_Time:{newDateTime},
        Open_price    :{newDF.iloc[-1]['Open_price']}, 
        High_price    :{newDF.iloc[-1]['High_price']}, 
        Low_price     :{newDF.iloc[-1]['Low_price']}, 
        Close_price   :{newDF.iloc[-1]['Close_price']}, 
        Volume  :{newDF.iloc[-1]['Volume']}
        """
        print(NewTimeStamp)
        time.sleep(61)
def BATrunner():
    import datetime
    import time
    timeFrame = '1m'
    filename     = r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\BAT%s.csv'%timeFrame
    formatString = "%Y-%m-%dT%H:%M:%SZ"
    while True:
        try:
            oldDF    = pd.read_csv(filename)
            lastDatatimeStamp = oldDF.DateTime.values[-1]*10**(-3)
            dt_object = datetime.datetime.fromtimestamp(int(lastDatatimeStamp))
            formattedTimestamp = datetime.datetime.now().strftime(formatString)
        except:
            formattedTimestamp ='2016-05-25T00:00:00Z'
        scrape_candles_to_csv(filename, 'binance', 10, 'BAT/USDT', timeFrame, formattedTimestamp, 100)
        newDF = pd.read_csv(filename)
        newDateTime  = int(newDF.iloc[-1]['Date_Time']*10**(-3))
        newDateTime  = datetime.datetime.fromtimestamp(newDateTime).strftime(formatString)
        NewTimeStamp = \
        f"""
        Date_Time:{newDateTime},
        Open_price    :{newDF.iloc[-1]['Open_price']}, 
        High_price    :{newDF.iloc[-1]['High_price']}, 
        Low_price     :{newDF.iloc[-1]['Low_price']}, 
        Close_price   :{newDF.iloc[-1]['Close_price']}, 
        Volume  :{newDF.iloc[-1]['Volume']}
        """
        print(NewTimeStamp)
        time.sleep(61)
def VETrunner():
    import datetime
    import time
    timeFrame = '1m'
    filename     = r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\VET%s.csv'%timeFrame
    formatString = "%Y-%m-%dT%H:%M:%SZ"
    while True:
        try:
            oldDF    = pd.read_csv(filename)
            lastDatatimeStamp = oldDF.DateTime.values[-1]*10**(-3)
            dt_object = datetime.datetime.fromtimestamp(int(lastDatatimeStamp))
            formattedTimestamp = datetime.datetime.now().strftime(formatString)
        except:
            formattedTimestamp ='2016-05-25T00:00:00Z'
        scrape_candles_to_csv(filename, 'binance', 10, 'VET/USDT', timeFrame, formattedTimestamp, 100)
        newDF = pd.read_csv(filename)
        newDateTime  = int(newDF.iloc[-1]['Date_Time']*10**(-3))
        newDateTime  = datetime.datetime.fromtimestamp(newDateTime).strftime(formatString)
        NewTimeStamp = \
        f"""
        Date_Time:{newDateTime},
        Open_price    :{newDF.iloc[-1]['Open_price']}, 
        High_price    :{newDF.iloc[-1]['High_price']}, 
        Low_price     :{newDF.iloc[-1]['Low_price']}, 
        Close_price   :{newDF.iloc[-1]['Close_price']}, 
        Volume  :{newDF.iloc[-1]['Volume']}
        """
        print(NewTimeStamp)
        time.sleep(61)
def NEOrunner():
    import datetime
    import time
    timeFrame = '1m'
    filename     = r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\NEO%s.csv'%timeFrame
    formatString = "%Y-%m-%dT%H:%M:%SZ"
    while True:
        try:
            oldDF    = pd.read_csv(filename)
            lastDatatimeStamp = oldDF.DateTime.values[-1]*10**(-3)
            dt_object = datetime.datetime.fromtimestamp(int(lastDatatimeStamp))
            formattedTimestamp = datetime.datetime.now().strftime(formatString)
        except:
            formattedTimestamp ='2016-05-25T00:00:00Z'
        scrape_candles_to_csv(filename, 'binance', 10, 'NEO/USDT', timeFrame, formattedTimestamp, 100)
        newDF = pd.read_csv(filename)
        newDateTime  = int(newDF.iloc[-1]['Date_Time']*10**(-3))
        newDateTime  = datetime.datetime.fromtimestamp(newDateTime).strftime(formatString)
        NewTimeStamp = \
        f"""
        Date_Time:{newDateTime},
        Open_price    :{newDF.iloc[-1]['Open_price']}, 
        High_price    :{newDF.iloc[-1]['High_price']}, 
        Low_price     :{newDF.iloc[-1]['Low_price']}, 
        Close_price   :{newDF.iloc[-1]['Close_price']}, 
        Volume  :{newDF.iloc[-1]['Volume']}
        """
        print(NewTimeStamp)
        time.sleep(61)
def QTUMrunner():
    import datetime
    import time
    timeFrame = '1m'
    filename     = r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\QTUM%s.csv'%timeFrame
    formatString = "%Y-%m-%dT%H:%M:%SZ"
    while True:
        try:
            oldDF    = pd.read_csv(filename)
            lastDatatimeStamp = oldDF.DateTime.values[-1]*10**(-3)
            dt_object = datetime.datetime.fromtimestamp(int(lastDatatimeStamp))
            formattedTimestamp = datetime.datetime.now().strftime(formatString)
        except:
            formattedTimestamp ='2016-05-25T00:00:00Z'
        scrape_candles_to_csv(filename, 'binance', 10, 'QTUM/USDT', timeFrame, formattedTimestamp, 100)
        newDF = pd.read_csv(filename)
        newDateTime  = int(newDF.iloc[-1]['Date_Time']*10**(-3))
        newDateTime  = datetime.datetime.fromtimestamp(newDateTime).strftime(formatString)
        NewTimeStamp = \
        f"""
        Date_Time:{newDateTime},
        Open_price    :{newDF.iloc[-1]['Open_price']}, 
        High_price    :{newDF.iloc[-1]['High_price']}, 
        Low_price     :{newDF.iloc[-1]['Low_price']}, 
        Close_price   :{newDF.iloc[-1]['Close_price']}, 
        Volume  :{newDF.iloc[-1]['Volume']}
        """
        print(NewTimeStamp)
        time.sleep(61)
def IOSTrunner():
    import datetime
    import time
    timeFrame = '1m'
    filename     = r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\IOST%s.csv'%timeFrame
    formatString = "%Y-%m-%dT%H:%M:%SZ"
    while True:
        try:
            oldDF    = pd.read_csv(filename)
            lastDatatimeStamp = oldDF.DateTime.values[-1]*10**(-3)
            dt_object = datetime.datetime.fromtimestamp(int(lastDatatimeStamp))
            formattedTimestamp = datetime.datetime.now().strftime(formatString)
        except:
            formattedTimestamp ='2016-05-25T00:00:00Z'
        scrape_candles_to_csv(filename, 'binance', 10, 'IOST/USDT', timeFrame, formattedTimestamp, 100)
        newDF = pd.read_csv(filename)
        newDateTime  = int(newDF.iloc[-1]['Date_Time']*10**(-3))
        newDateTime  = datetime.datetime.fromtimestamp(newDateTime).strftime(formatString)
        NewTimeStamp = \
        f"""
        Date_Time:{newDateTime},
        Open_price    :{newDF.iloc[-1]['Open_price']}, 
        High_price    :{newDF.iloc[-1]['High_price']}, 
        Low_price     :{newDF.iloc[-1]['Low_price']}, 
        Close_price   :{newDF.iloc[-1]['Close_price']}, 
        Volume  :{newDF.iloc[-1]['Volume']}
        """
        print(NewTimeStamp)
        time.sleep(61)
def THETArunner():

    import datetime
    import time
    timeFrame = '1m'
    filename     = r'C:\Users\James\Documents\GitHub\Nibbler\nibbler\trading\collectors\THETA%s.csv'%timeFrame
    formatString = "%Y-%m-%dT%H:%M:%SZ"
    while True:
        try:
            oldDF    = pd.read_csv(filename)
            lastDatatimeStamp = oldDF.DateTime.values[-1]*10**(-3)
            dt_object = datetime.datetime.fromtimestamp(int(lastDatatimeStamp))
            formattedTimestamp = datetime.datetime.now().strftime(formatString)
        except:
            formattedTimestamp ='2019-05-25T00:00:00Z'
        scrape_candles_to_csv(filename, 'binance', 10, 'THETA/USDT', timeFrame, formattedTimestamp, 100)
        newDF = pd.read_csv(filename)
        newDateTime  = int(newDF.iloc[-1]['Date_Time']*10**(-3))
        newDateTime  = datetime.datetime.fromtimestamp(newDateTime).strftime(formatString)
        NewTimeStamp = \
        f"""
        Date_Time:{newDateTime},
        Open_price    :{newDF.iloc[-1]['Open_price']}, 
        High_price    :{newDF.iloc[-1]['High_price']}, 
        Low_price     :{newDF.iloc[-1]['Low_price']}, 
        Close_price   :{newDF.iloc[-1]['Close_price']}, 
        Volume  :{newDF.iloc[-1]['Volume']}
        """
        print(NewTimeStamp)
        time.sleep(61)
THETArunner()
# -----------------------------------------------------------------------------
# if __name__ == '__main__':
#     import datetime
#     import time
#     timeFrame = '1m'
#     filename     = r'C:\Users\james\Documents\GitHub\bigdikfactory\Collectors\eth%s.csv'%timeFrame
#     formatString = "%Y-%m-%dT%H:%M:%SZ"
#     while True:
#         try:
#             oldDF    = pd.read_csv(filename)
#             lastDatatimeStamp = oldDF.DateTime.values[-1]*10**(-3)
#             dt_object = datetime.datetime.fromtimestamp(int(lastDatatimeStamp))
#             formattedTimestamp = datetime.datetime.now().strftime(formatString)
#         except:
#             formattedTimestamp ='2020-05-25T00:00:00Z'
#         scrape_candles_to_csv(filename, 'binance', 10, 'ETH/USDT', timeFrame, formattedTimestamp, 1000)
#         newDF = pd.read_csv(filename)
#         newDateTime  = int(newDF.iloc[-1]['DateTime']*10**(-3))
#         newDateTime  = datetime.datetime.fromtimestamp(newDateTime).strftime(formatString)
#         NewTimeStamp = \
#         f"""
#         DateTime:{newDateTime},
#         Open    :{newDF.iloc[-1]['Open']}, 
#         High    :{newDF.iloc[-1]['High']}, 
#         Low     :{newDF.iloc[-1]['Low']}, 
#         Close   :{newDF.iloc[-1]['Close']}, 
#         Volume  :{newDF.iloc[-1]['Volume']}
#         """
#         print(NewTimeStamp)
#         time.sleep(61)

