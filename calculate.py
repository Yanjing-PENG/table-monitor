# -*- encoding: utf-8 -*-

from math import floor
import pandas as pd

def calculate(future_quotes, index_quotes):
    """
    Calculate real basis
    """

    # preprocessing data
    result = future_quotes
    result['index_price'] = 0

    for i in range(len(result)):
        if result.iloc[i, 0][:2] == 'IF':
            result.iloc[i, 2] = index_quotes.loc[index_quotes['code'] == '000300.SH']['index_price'].values[0]
        elif result.iloc[i, 0][:2] == 'IH':
            result.iloc[i, 2] = index_quotes.loc[index_quotes['code'] == '000016.SH']['index_price'].values[0]
        else:
            result.iloc[i, 2] = index_quotes.loc[index_quotes['code'] == '000905.SH']['index_price'].values[0]

    # calculating real basis
    result['real_basis'] = 0
    for i in range(len(result)):
        result.iloc[i, 3] = floor((result.iloc[i, 1] - result.iloc[i, 2]) * 100)/100

    return result

