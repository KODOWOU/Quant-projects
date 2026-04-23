# src/momentum.py

import pandas as pd
import numpy as np


def momentum_strategy(returns, lookback=12, top_n=3):
    signals = returns.rolling(lookback).mean()

    weights = pd.DataFrame(0, index=returns.index, columns=returns.columns)

    for date in signals.index:
        if signals.loc[date].isna().any():
            continue

        top_assets = signals.loc[date].nlargest(top_n).index
        weights.loc[date, top_assets] = 1 / top_n

    return weights.fillna(0)


def apply_strategy(returns, weights):
    portfolio_returns = (returns * weights.shift(1)).sum(axis=1)
    return portfolio_returns
