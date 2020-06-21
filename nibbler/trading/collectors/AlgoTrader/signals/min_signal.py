from ..indicators import Min as min_indicator
from . import Signal


class Min(Signal):
    def __init__(self, *args, time_buffer=20, **kwargs):
        super(Min, self).__init__(
                    *args, time_buffer=time_buffer, **kwargs
                )
        self.min_indicator = min_indicator(
            *args, **kwargs
        )
        self.time_buffer = time_buffer
        self.signalled = []
        
    def condition(self, data):
        len_time = len(data)
        features = self.min_indicator(data)

        try:
            if len(features) == 0:
                return False
        except:
            features = [features, ]

        self.features = \
            features[-1]
                
        if (len_time - self.features)\
            < self.time_buffer: 
            if self.features not in self.signalled:
                self.signalled.append(self.features)
                return True
        return False

    def plot_candles(self, *args, **kwargs):
        self.axis = self.min_indicator.plot_candles(
            *args, **kwargs
        )
        return self.axis

    def plot_features(self, *args, **kwargs):
        old_feats = self.min_indicator.features.copy()
        feats = old_feats[-1]
        self.min_indicator.features = feats
        p = self.min_indicator.plot_features(*args, **kwargs)
        self.min_indicator.features = old_feats
        return p

        


