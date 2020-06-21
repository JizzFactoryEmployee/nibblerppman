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


# -----------------------------------------------------------------------------

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

    df = pd.DataFrame(columns = ['DateTime','Open','High','Low','Close','Volume'])
    df = df.assign(**dict(zip(df.keys(),np.array(ohlcv).T)))

    if filename.exists():
        original = pd.read_csv(filename)
        df       = original.append(df).drop_duplicates(subset='DateTime', keep='first', inplace=False)


    df.to_csv(filename,index =False)

# -----------------------------------------------------------------------------
if __name__ == '__main__':
    import datetime
    import time
    timeFrame = '5m'
    filename     = r'C:\Users\james\Documents\GitHub\bigdikfactory\Collectors\na1o%s.csv'%timeFrame
    formatString = "%Y-%m-%dT%H:%M:%SZ"
    while True:
        try:
            oldDF    = pd.read_csv(filename)
            lastDatatimeStamp = oldDF.DateTime.values[-1]*10**(-3)
            dt_object = datetime.datetime.fromtimestamp(int(lastDatatimeStamp))
            formattedTimestamp = datetime.datetime.now().strftime(formatString)
        except:
            formattedTimestamp ='2017-07-01T00:00:00Z'
        scrape_candles_to_csv(filename, 'binance', 10, 'ONT/USDT', timeFrame, formattedTimestamp, 1000)
        newDF = pd.read_csv(filename)
        newDateTime  = int(newDF.iloc[-1]['DateTime']*10**(-3))
        newDateTime  = datetime.datetime.fromtimestamp(newDateTime).strftime(formatString)
        NewTimeStamp = \
        f"""
        DateTime:{newDateTime},
        Open    :{newDF.iloc[-1]['Open']}, 
        High    :{newDF.iloc[-1]['High']}, 
        Low     :{newDF.iloc[-1]['Low']}, 
        Close   :{newDF.iloc[-1]['Close']}, 
        Volume  :{newDF.iloc[-1]['Volume']}
        """
        print(NewTimeStamp)
        time.sleep(5)
