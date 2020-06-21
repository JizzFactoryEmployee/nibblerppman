import pandas as pd
from bokeh.plotting import figure, show, output_file
from math import pi
from .. import utils
import numpy as np

TOOLS = "pan,wheel_zoom,ywheel_zoom,xwheel_zoom,box_zoom,reset,save"
date = 'datetime'


def initialize_dataframe(df):
    df.columns = df.columns.str.lower()

    
    # df[date] = pd.to_datetime(df[date])
    return df


def initialize_figure(p, **kwargs):
    if p is not None:
        return p
    return figure(
        x_axis_type=date,
        tools=TOOLS, **kwargs
    )


def candles(
        df, lims='all', fig=None, w='4h', **kwargs
        
    ):
    if lims is not 'all':
        df = df[lims[0]:lims[1]]
    df = initialize_dataframe(df)

    inc = df.close > df.open
    dec = df.open > df.close
    w = utils.time_frames[w]

    p =  initialize_figure(fig, **kwargs)

    
    p.grid.grid_line_alpha=0.3
    p.segment(df.datetime, df.high, df.datetime, df.low, color="black")
    p.vbar(
        df.datetime[inc], w, df.open[inc], df.close[inc],
        fill_color="#D5E1DD", line_color="black")
    p.vbar(
        df.datetime[dec], w, df.open[dec], df.close[dec],
        fill_color="#F2583E", line_color="black")
    return p


def min(indices, df, fig=None, size=20):
    df = initialize_dataframe(df)
    p = initialize_figure(fig)
    low_values = np.minimum(
        df.low.iloc[indices], df.high.iloc[indices]
    )
    low_values = np.minimum(
        low_values, df.open.iloc[indices]
    )
    low_values = np.minimum(
        low_values, df.close.iloc[indices]
    )
    date_time = df.datetime.iloc[indices]

    p.triangle(
        date_time, low_values - 0.002*low_values,
        size=size, color="green", alpha=0.5
    )
    return p


def max(indices, df, fig=None, size=20):
    df = initialize_dataframe(df)
    p = initialize_figure(fig)
    max_values = np.maximum(
        df.low.iloc[indices], df.high.iloc[indices]
    )
    max_values = np.maximum(
        max_values, df.open.iloc[indices]
    )
    max_values = np.maximum(
        max_values, df.close.iloc[indices]
    )
    date_time = df.datetime.iloc[indices]

    p.inverted_triangle(
        date_time, max_values + 0.002*max_values,
        size=size, color="red", alpha=0.5
    )
    return p


__all__ = [
    'TOOLS', 'initialize_dataframe', 'date', 'initialize_dataframe',
    'initialize_figure', 'plot_candles', 'plot_min'
]







