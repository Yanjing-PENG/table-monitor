# -*- encoding: utf-8 -*-

import numpy as np
import pandas as pd
from math import floor

def getIndexTick(code_list):
    """
    Acquire the latest prices of corresponding indexes.
    I randomly generate prices for an example, while you could override this
    function by using quotation API in real world.

    """
    index_tick = []
    for code in code_list:
        if code == '000300.SH':
            index_tick.append(floor((5 * np.random.randn(1) + 3000) * 100) / 100)
        elif code == '000016.SH':
            index_tick.append(floor((5 * np.random.randn(1) + 2000) * 100) / 100)
        elif code == '000905.SH':
            index_tick.append(floor((5 * np.random.randn(1) + 5000) * 100) / 100)
        else:
            raise Exception("indexes code error.")

    dataframe_quotes = pd.DataFrame({'code': code_list, 'index_price': index_tick})

    return dataframe_quotes