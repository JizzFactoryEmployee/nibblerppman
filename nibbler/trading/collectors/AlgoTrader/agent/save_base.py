import numpy as np
import pandas as pd
from bokeh.plotting import save
from bokeh.models.annotations import Title
from pathlib import Path
import datetime

class Save:

    def __init__(self, buy_signal, sell_signal, save_path='.'):
        self.main_dir = save_path
        self.buy_dir = self.main_dir/'buy_signals'
        self.sell_dir = self.main_dir/'sell_signals'
        for path in [self.buy_dir, self.sell_dir]:
            if not path.exists():
                path.mkdir(parents=True)
        self.buy_signal = buy_signal
        self.sell_signal = sell_signal

    def run(self, data_path, **plot_kwargs):
        if isinstance(data_path, (str, Path)):
            data = pd.read_csv(data_path)
        else:
            data = data_path

        current_date = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
        title = Title()
            
        if self.sell_signal(data):
            self.sell_signal.plot_candles(**plot_kwargs)
            p = self.sell_signal.plot_features()
            title.text = 'sell_signal %s' % current_date
            p.title = title
            return save(
                p, filename=self.sell_dir/('sell-%s.HTML' % current_date)
            )
            
        elif self.buy_signal(data):
            self.buy_signal.plot_candles(**plot_kwargs)
            p = self.buy_signal.plot_features()
            title.text = 'buy_signal %s.HTML' % current_date
            p.title = title
            return save(
                p, filename=self.buy_dir/('buy-%s.HTML' % current_date)
            )

