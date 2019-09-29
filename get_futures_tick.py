# -*- encoding: utf-8 -*-

import numpy as np
import pandas as pd
from math import floor

def getFuturesTick(code_list):
    """
    Acquire the latest prices of current futures.
    I randomly generate prices for an example, while you could override this
    function by using quotation API in real world.

    """
    futures_tick = []
    for code in code_list:
        if code[:2] == 'IF':
            futures_tick.append(floor((5 * np.random.randn(1) + 3000) * 100) / 100)
        elif code[:2] == 'IH':
            futures_tick.append(floor((5 * np.random.randn(1) + 2000) * 100) / 100)
        elif code[:2] == 'IC':
            futures_tick.append(floor((5 * np.random.randn(1) + 5000) * 100) / 100)
        else:
            raise Exception("futures code error.")

    dataframe_quotes = pd.DataFrame({'code': code_list, 'futures_price': futures_tick})

    return dataframe_quotes