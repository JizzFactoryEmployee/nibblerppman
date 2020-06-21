# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 20:37:47 2019

@author: chris
"""
import pandas as pd
import numpy as np
from typing import List
from tqdm import tqdm


def time_frame_multiplier(data_frame: pd.DataFrame,
                      time_factor   : int,
                      columns       : List[str] = ['open', 'high', 'low', 'close', 'volume']
                      )->pd.DataFrame:
    """time_frame_multiplier multiply time frame

    multiplies to a higher time frame

    Args:
        data_frame (pd.DataFrame): OHLCV dataframe
        time_factor (int): time frame multiplier
        columns (List[str], optional): required columns. Defaults to ['open', 'high', 'low', 'close', 'volume'].

    Returns:
        pd.DataFrame: OHLCV converted into higher time frame
    """
    df = pd.DataFrame(
            columns = columns,
            index   = np.arange(len(data_frame)//time_factor))
    df.columns = df.columns.str.lower()
    columns    = [col.lower() for col in columns]
    tmp   = [];tmpsetter = tmp.append
    count = 0
    for i in tqdm(np.arange(len(df))):
        # if all([len(tmp)%time_factor == 0,len(tmp) >0]) :
            tmp = data_frame.loc[i*time_factor:(i+1)*time_factor][columns].values
            #now it is time to populate the dataframe
            df.loc[i][columns] = \
                [tmp[0,0],
                 np.max(tmp[:,1]),
                 np.min(tmp[:,2]),
                 tmp[-1,3],
                 np.sum(tmp[:,-1])
                 ]                
           
    return df.dropna()


def time_frame_mex(
    data_frame, time_factor,
    columns=['DateTime', 'Open', 'High', 'Low', 'Close', 'Volume'],
    include_datetime=True
):
    n_entries = len(data_frame)//time_factor
    df = pd.DataFrame(
        columns=columns,
        index=np.arange(n_entries)
    )
    for i in np.arange(n_entries):
        # if all([len(tmp)%time_factor == 0,len(tmp) >0]) :
        tmp = \
            data_frame.loc[i*time_factor:((i+1)*time_factor-1)][columns].values   
        # now it is time to populate the dataframe
        df.loc[i][columns] = \
            [
                tmp[0, 0],
                tmp[0, 1],
                np.max(tmp[:, 1]),
                np.min(tmp[:, 2]),
                tmp[-1, 4],
                np.sum(tmp[:, -1])
            ]
    return df.dropna()
