# src/returns.py

import numpy as np
import pandas as pd


def compute_log_returns(prices):
    return np.log(prices / prices.shift(1)).dropna()


def compute_monthly_returns(prices):
    monthly_prices = prices.resample("M").last()
    return compute_log_returns(monthly_prices)


def annualized_return(returns):
    return returns.mean() * 12


def annualized_volatility(returns):
    return returns.std() * np.sqrt(12)
