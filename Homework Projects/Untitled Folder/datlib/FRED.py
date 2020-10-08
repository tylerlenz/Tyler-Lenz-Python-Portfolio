#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 19:33:02 2020

@author: Tyler
"""

import pandas as pd
import pandas_datareader.data as web
import datetime

def gather_data(data_codes, start, end = datetime.datetime.today(), freq = "A"):
    i = 0;
    for key, code in data_codes.items():
        if i == 0:
            df = web.DataReader(code, "fred", start, end).resample(freq).mean()
            df.rename(columns = {code:key}, inplace = True)
            
            i = None
        else:
            df[key] = web.DataReader(code, "fred", start, end).resample(freq).mean()
            
        return df