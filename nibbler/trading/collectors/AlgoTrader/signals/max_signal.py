from ..indicators import Max as max_indicator
from . import Signal


class Max(Signal):
    def __init__(self, *args, time_buffer=20, **kwargs):

        super(Max, self).__init__(
            *args, time_buffer=time_buffer, **kwargs
        )

        self.max_indicator = max_indicator(
            *args, **kwargs
        )
        self.time_buffer = time_buffer
        self.signalled = []

    def condition(self, data):
        len_time = len(data)
        features = self.max_indicator(data)

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
        self.axis = self.max_indicator.plot_candles(
            *args, **kwargs
        )
        return self.axis

    def plot_features(self, *args, **kwargs):
        old_feats = self.max_indicator.features.copy()
        feats = old_feats[-1]
        self.max_indicator.features = feats
        p = self.max_indicator.plot_features(*args, **kwargs)
        self.max_indicator.features = old_feats
        return p




