#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 16:50:30 2020

@author: Tyler
"""

#format.py
#format.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#pd.set_option('display.width', 300)

df = pd.read_csv("MusicData.csv", index_col=[0,1,2]).fillna(0)
df.to_csv("reformattedMusicData.csv")


for key in df:
    # replace "," with blank so that string can be transformed to value
    # instead of being read as a null value
    df[key] = pd.to_numeric(df[key].str.replace(",",""), errors = "coerce")
df = df[~df.index.duplicated()]
metrics = sorted(list(set(df.index.get_level_values("Metric"))))

first = True
for metric in metrics[-1::-1]:
    print(df[df.index.get_level_values("Metric") == metric])
    if first == True:
        reformat_df = df[df.index.get_level_values("Metric") == metric]
        reformat_df.rename(columns = {"Value":metric}, inplace = True)
        reformat_df.reset_index(inplace = True)
        reformat_df.set_index(["Format", "Year"], inplace = True)
        first = False
    else:
        df_slice = df[df.index.get_level_values("Metric") == metric]
        df_slice.reset_index(inplace = True)
        df_slice.set_index(["Format", "Year"], inplace = True)
        # reformat_df = pd.concat([reformat_df, df_slice["Value"]], 
        #                         axis=1)
        # duplicate value in index of Units columns
        reformat_df[metric] = df_slice["Value"]

reformat_df["Implied Price"] = reformat_df["Value"].div(reformat_df["Units"])#.mul(10**9)
reformat_df["Implied Real Price"] = reformat_df["Value (Adjusted)"].div(reformat_df["Units"])
print(reformat_df)


# select only a subset of the index for multindex
#df[df.index.get_level_values(index_name) == desired_value]
# after getting subset, you may need to reset index
#df.reset_index(inplace=True).set_index(desired_index_column)
