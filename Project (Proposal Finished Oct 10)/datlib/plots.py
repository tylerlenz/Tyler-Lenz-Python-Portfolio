#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 16:19:22 2020

@author: Tyler
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_ts_scatter(df, s = 75, figsize = (40, 20), save_fig = False, pp = None):
    plot_vars = list(df.keys())
    for x in plot_vars:
        for y in plot_vars:
            if x != y:
                fig, ax = plt.subplots(figsize = figsize)
            
                if "Year" not in df.keys():
                    df["Year"] = [int(str(ind)[:4]) for ind in df.index]
                    
                df.plot.scatter(x = x, y = y, s = s, ax = ax, c = "Year", cmap = "plasma")
                    
                ax.tick_params(axis = 'x', rotation =90)
                ax.tick_params('both', length = 0, which = 'both')
                    
                if save_fig:
                    try:
                           os.mkdir("plots")
                    except:
                        pass
                    
                    directory = "plots/" + x[:12] + " " + y[:12] + " c=Year"
                    plt.savefig(directory + ".png")
                    if pp != None: pp.savefig(fig, bbox_inches = "tight")
                
def plot_lines(df, linewidth = 1, figsize = (40,20), 
               legend = True, pp = None):
    fig, ax = plt.subplots(figsize = figsize)
    # If no secondary_y (axis), plot all variables at once
    df.plot.line(linewidth = linewidth, ax = ax, legend = legend)
    # Turn the text on the x-axis so that it reads vertically
    ax.tick_params(axis="x", rotation=90)
    # get rid of tick lines
    ax.tick_params("both", length=0, which = "both")
    
    vals = ax.get_yticks()
    vals = [int(x) for x in vals]
    ax.set_yticklabels(vals)
    
    # format image filename
    remove_chars = "[]:$'\\"
    filename = str(list(df.keys()))
    for char in remove_chars:
        filename = filename.replace(char, "")
    # avoid cutting off text
    plt.savefig(filename[:50] + "line.png",
               bbox_inches = "tight")
    if pp != None: pp.savefig(fig, box_inches = "tight")
    
def plot_stacked_lines(df, plot_vars, linewidth = 1, figsize = (40,20), 
                       pp = None, total_var = False):
    fig, ax = plt.subplots(figsize = figsize)
    df[plot_vars].plot.area(stacked = True, linewidth = linewidth,
                            ax = ax)
    # change y vals from mil to tril
    
    if total_var != False:
        df[total_var].plot.line(linewidth = linewidth, ax = ax, c = "k",
              label = total_var, ls = "--")
    ax.legend(loc=2, ncol = 2)