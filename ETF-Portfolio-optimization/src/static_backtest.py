# src/static_backtest.py

import pandas as pd
from src.portfolio import portfolio_return, portfolio_metrics

def static_backtest(returns, weights):
    """
    Backtest simple avec poids fixes définis par l'utilisateur.
    """

    # Daily portfolio returns
    port_ret = portfolio_return(weights, returns)

    # Cumulative returns
    cumulative = (1 + port_ret).cumprod()

    # Metrics
    metrics = portfolio_metrics(weights, returns)

    return {
        "daily_returns": port_ret,
        "cumulative_returns": cumulative,
        "metrics": metrics
    }
