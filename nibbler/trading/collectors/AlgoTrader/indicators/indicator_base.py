import inspect
import pandas as pd
import numpy as np
from ..plot import candles, show


class placeholder:
    def __call__(self, *args, **kwargs):
        return None

class Indicator:

    function = placeholder()
    on_chart = True
    
    def __init__(
        self, *args, **kwargs
    ):
        self.axis = None
        self.called = False
        self.kwargs = kwargs
        assert self.function.__class__ is not placeholder,\
            'function must be set'
        argspect = inspect.getfullargspec(self.function)
        all_args = argspect.args
        len_kws = len(argspect.kwonlyargs)
        self.arg_names = all_args[0:len(all_args)-len_kws]
        self.arg_names = [
            arg for arg in self.arg_names if arg !=self
        ]
        self.kwarg_names = all_args[
            (len(all_args) - len_kws):
        ]
        self.kwarg_defaults = argspect.defaults
        if self.kwarg_defaults is not None:
            self.defaults = list(
                zip(
                    self.kwarg_names, self.kwarg_defaults
                )
            )
            self.defaults = dict(self.defaults)
            for key in self.kwarg_names:
                self.kwargs[key] = self.kwargs.get(
                    self.kwargs[key], self.defaults[key]
                )
        
    def __call__(
        self, OHLCV
    ):
        assert OHLCV.__class__ is pd.DataFrame
        OHLCV.columns = OHLCV.columns.str.lower()
        self.ohlcv = OHLCV
        self.called = True
        args = [
            pd.Series(OHLCV[arg]) for arg in self.arg_names if \
                arg not in 'self'
        ]
        features = self.function(*args, **self.kwargs)
        self.features = self.feature_extraction(
            features
        )
        return self.features

    def feature_extraction(self, features):
        return features

    def plot_candles(self, *args, **kwargs):
        assert self.called
        self.axis = candles(
            self.ohlcv, **kwargs
        )
        return self.axis

    def plot_features(self, *args, **kwargs):
        NotImplementedError

    def show(self):
        show(self.axis)




    

__all__ = [
    'Indicator'
]
