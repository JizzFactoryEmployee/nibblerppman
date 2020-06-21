try:
    from AlgoTrader.indicators import Indicator
except ImportError:
    from .indicator_base import Indicator
import numpy as np
import scipy.signal as sg
from .. import plot


def makeOdd(intval):
    if intval%2 == 0:
        return intval+1
    else:
        return intval


class PartialSavitsky:
    def __init__(self, window_length, polyorder, **kwargs):
        self.window_length = window_length
        self.polyorder = polyorder
        self.kwargs = kwargs

    def __call__(self, x):
        return sg.savgol_filter(
            x, self.window_length, self.polyorder, **self.kwargs
        )


def locate_min(gradients):
    t_0 = gradients[0:-1]
    t_1 = gradients[1:]

    le_0 = np.less_equal(t_0, 0)
    ge_1 = np.greater_equal(t_1, 0)

    mins = np.logical_and(
        ge_1, le_0
    )
    indices = np.argwhere(
        mins
    ).squeeze()
    return indices


def locate_max(gradients):
    t_0 = gradients[0:-1]
    t_1 = gradients[1:]

    ge_0 = np.greater_equal(t_0, 0)
    le_1 = np.less_equal(t_1, 0)

    maxes = np.logical_and(
        ge_0, le_1
    )

    indices = np.argwhere(
        maxes
    ).squeeze()
    return indices


class SavitzkyGradientMethod:
    input_arg_names = [
        'window_length', 'polyorder',
        'grad_window_length', 'grad_polyorder'
    ] 

    def __init__(
        self, window_length, polyorder,
        grad_window_length, grad_polyorder, deriv=0,
        delta=1.0, axis=-1
    ):
        kwargs = dict(
            deriv=deriv, delta=delta,
            axis=axis
        )
        window_length = makeOdd(window_length)
        grad_window_length = makeOdd(grad_window_length)

        assert polyorder < window_length
        assert grad_polyorder < grad_window_length

        self.data_filter = PartialSavitsky(
            window_length, polyorder, mode='interp', **kwargs
        )
        self.gradient_filter = PartialSavitsky(
             grad_window_length, grad_polyorder, **kwargs
        )

    def calculate_gradients(self, data):
        self.data = self.data_filter(data)
        gradients = np.gradient(data)
        gradients = self.gradient_filter(gradients)
        # gradients = self.gradient_filter(gradients)
        return gradients


class FilteredMin(SavitzkyGradientMethod):
    def __call__(self, low, **kwargs):
        gradients = self.calculate_gradients(low)
        return locate_min(gradients)


class FilterdMax(SavitzkyGradientMethod):
    def __call__(self, high, **kwargs):
        gradients = self.calculate_gradients(high)
        return locate_max(gradients)


class Min(Indicator):
    def __init__(self, *args, **kwargs):
        self.function = FilteredMin(
            *args, **kwargs
        )
        super(Min, self).__init__(*args, **kwargs)

    def plot_features(self, *args, **kwargs):
        assert hasattr(self, 'features')
        if 'fig' in kwargs.keys():
            axis = kwargs.pop('fig')
        else:
            axis = self.axis
            
        axis = plot.min(self.features, self.ohlcv, fig=axis, **kwargs)
        axis.line(
            self.ohlcv.datetime, self.function.data, line_width=2, color='green')
        return axis


class Max(Indicator):
    def __init__(self, *args, **kwargs):
        self.function = FilterdMax(
            *args, **kwargs
        )
        super(Max, self).__init__(*args, **kwargs)

    def plot_features(self, *args, **kwargs):
        assert hasattr(self, 'features')
        if 'fig' in kwargs.keys():
            axis = kwargs.pop('fig')
        else:
            axis = self.axis
        
        axis = plot.max(self.features, self.ohlcv, fig=axis, **kwargs)
        axis.line(
            self.ohlcv.datetime, self.function.data, line_width=2, color='red')
        
        return axis

