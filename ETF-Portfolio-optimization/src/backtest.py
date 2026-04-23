# src/backtest.py

import pandas as pd


def backtest_portfolio(returns, weights, rebalance_freq="M"):
    """
    Simple rebalanced portfolio backtest
    """

    portfolio_returns = (returns * weights).sum(axis=1)

    cumulative_returns = (1 + portfolio_returns).cumprod()

    return portfolio_returns, cumulative_returns
