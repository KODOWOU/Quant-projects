# src/rolling_backtest.py

import pandas as pd
from src.optimization import maximize_sharpe


def rolling_backtest(returns, window=36):
    weights_history = []
    portfolio_returns = []

    for i in range(window, len(returns)):
        train = returns.iloc[i-window:i]
        test = returns.iloc[i]

        weights = maximize_sharpe(train)

        weights_history.append(weights)
        portfolio_returns.append((test * weights).sum())

    portfolio_returns = pd.Series(portfolio_returns, index=returns.index[window:])
    cumulative = (1 + portfolio_returns).cumprod()

    return portfolio_returns, cumulative
