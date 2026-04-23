# src/portfolio.py

import numpy as np


def portfolio_return(weights, returns):
    return returns @ weights


def portfolio_performance(weights, returns):
    port_ret = portfolio_return(weights, returns)
    ann_return = port_ret.mean() * 12
    ann_vol = port_ret.std() * np.sqrt(12)

    return ann_return, ann_vol
