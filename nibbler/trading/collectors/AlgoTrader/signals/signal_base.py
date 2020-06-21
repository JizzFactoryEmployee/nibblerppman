from bokeh.plotting import show
import numpy as np
from pathlib import Path


class Signal:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
    def __call__(self, data):
        return self.condition(data)
    def condition(self, data):
        return data
    def show(self):
        show(self.axis)
    
    @classmethod
    def load(cls, weights):
        if isinstance(
            weights, (str, Path)
        ):
            weights = np.load(
                weights, allow_pickle=True
            ).item()
        return cls(
            *weights['args'], **weights['kwargs']
        ) 

    def save(self, path):
        data = {'args': self.args, 'kwargs': self.kwargs}
        np.save(path, data)
            

        
