import pandas as pd
import numpy as np
from pathlib import Path
import ccxt  # noqa: E402
from datetime import datetime
import time
from ..utils import time_frame_multiplier


class Collector(object):
    max_retries = 10
    symbol = None
    limit = 1000

    formatString = "%Y-%m-%dT%H:%M:%SZ"

    _exchange = None
    exchange_dict = {
        'enableRateLimit': True
    }
    _time_frame_seconds = None
    _time_frame_ms = None
    _time_delta = None
    allowed_timeframes = [
        '1m', '5m', '1h', '1d'
    ]

    def __init__(self, timeframe):
        assert self.symbol is not None
        assert self._exchange is not None
        # assert timeframe in self.allowed_timeframes

        self.timeframe = timeframe

        self.num_retries = 0
        self.scraping = False

    # '2013-07-01T00:00:00Z'
    def run_loop(self, csv_filename, timestamp='2013-07-01T00:00:00Z',
                 multiplier=None):
        while True:
            self.run(
                csv_filename, timestamp=timestamp,
                multiplier=multiplier)
            time.sleep(60)
        
    def run(
            self, csv_filename, timestamp='2013-07-01T00:00:00Z', multiplier=None):

        try:
            df_old = pd.read_csv(csv_filename)
            ts_last = df_old.Date_Time.values[-1]*10**(-3)
            formattedTimestamp = \
                datetime.fromtimestamp(int(ts_last)).strftime(
                    self.formatString)
        except:
            if timestamp.lower() != 'now':
                formattedTimestamp = timestamp
            else:
                formattedTimestamp = datetime.now().strftime(
                    self.formatString)
        self.since = formattedTimestamp
        self.scrape_to_csv(csv_filename)
        newDF = pd.read_csv(csv_filename)
        if multiplier is not None:
            if multiplier > 1:
                newDF = time_frame_mex(newDF, multiplier)
                name = "%s_%d%s.csv" % (
                    csv_filename.stem, multiplier, self.timeframe[1])
                newDF.to_csv(
                    csv_filename.parent/name, index=False, index_label=False)
        newDateTime = int(newDF.iloc[-1]['Date_Time']*10**(-3))
        newDateTime = \
            datetime.fromtimestamp(newDateTime).strftime(
                self.formatString)
        NewTimeStamp = \
            f"""
            Date_Time     :{newDateTime},
            Open_price    :{newDF.iloc[-1]['Open_price']},
            High_price    :{newDF.iloc[-1]['High_price']},
            Low_price     :{newDF.iloc[-1]['Low_price']},
            Close_price   :{newDF.iloc[-1]['Close_price']},
            Volume        :{newDF.iloc[-1]['Volume']}
            """
        print(NewTimeStamp)

    def scrape_to_csv(self, csv_file):
        self.csv_file = Path(csv_file)
        if not self.csv_file.exists():
            df = pd.DataFrame(
                columns=['Date_Time', 'Open_price', 'High_price', 'Low_price', 'Close_price', 'Volume'])
            df.to_csv(csv_file, index=False, index_label=False)
        self.scrape()
        df = self.construct_data_frame()
        symbol = self.symbol.split('/')
        symbol1 = symbol[0]
        symbol2 = symbol[1]
        df['pair_1'] = symbol1
        df['pair_2'] = symbol2
        df = df[[ 'pair_1', 'pair_2','Date_Time', 'Open_price', 'High_price', 'Low_price', 'Close_price', 'Volume']]
        df = df.round(8)
        df.to_csv(self.csv_file, index=False)

    def scrape(self):
        self.earliest_time_stamp_ms = self.exchange.milliseconds()
        self.scraping = True
        self.all_ohlcv = []
        to_break = False
        while True:
            time.sleep(0.7)

            if isinstance(self.since, str):
                self.since = self.exchange.parse8601(self.since)
            self.exchange.load_markets()
            to_break = self.scrape_method()
            if to_break:
                break
        self.scraping = False

    def scrape_method(self):
        fetch_since = self.earliest_time_stamp_ms - self.time_delta
        ohlcv = self.retry_fetch(fetch_since)
        try:
            if ohlcv[0][0] >= self.earliest_time_stamp_ms:
                return True
        except ValueError:
            return True
        self.earliest_time_stamp_ms = ohlcv[0][0]
        self.all_ohlcv.extend(ohlcv)
        print(self.symbol)
        print(
            len(self.all_ohlcv), 'candles in total from',
            self.exchange.iso8601(self.all_ohlcv[0][0]),
            'to', self.exchange.iso8601(self.all_ohlcv[-1][0]))
        if fetch_since < int(self.since):
            return True
        return False


    def retry_fetch(self, since):
        assert self.scraping, "command is run inside the scrape method"

        self.num_retries = 0
        try:
            self.num_retries += 1
            ohlcv = self.exchange.fetch_ohlcv(
                self.symbol, self.timeframe, since, self.limit)
            return ohlcv
        except ValueError:
            if self.num_retries > self.max_retries:
                raise Exception('Failed to fetch', self.timeframe, self.symbol,
                                'OHLCV in', self.max_retries, 'attempts')

    def construct_data_frame(self):
        df = pd.DataFrame(
            columns=['Date_Time', 'Open_price', 'High_price', 'Low_price', 'Close_price', 'Volume', 'pair_1', 'pair_2'])
        df = df.assign(
            **dict(zip(df.keys(), np.array(self.all_ohlcv).T)))
        df = df.sort_values(by='Date_Time', ascending=True)
        if self.csv_file is not None:
            original_csv = pd.read_csv(self.csv_file.as_posix())
            df = original_csv.append(df).drop_duplicates(
                subset='Date_Time', keep='first', inplace=False)
            df = df[['Date_Time', 'Open_price', 'High_price', 'Low_price', 'Close_price', 'Volume', 'pair_1', 'pair_2']]
        return df

    @property
    def exchange(self):
        if isinstance(self._exchange, str):
            self._exchange = getattr(ccxt, self._exchange)(
                self.exchange_dict
            )
        return self._exchange

    @property
    def time_frame_seconds(self):
        if self._time_frame_seconds is None:
            self._time_frame_seconds = self.exchange.parse_timeframe(
                self.timeframe)
        return self._time_frame_seconds

    @property
    def time_frame_ms(self):
        if self._time_frame_ms is None:
            self._time_frame_ms = self.time_frame_seconds * 1000
        return self._time_frame_ms

    @property
    def time_delta(self):
        if self._time_delta is None:
            self._time_delta = self.limit * self.time_frame_ms
        return self._time_delta
