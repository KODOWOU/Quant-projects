# src/efficient_frontier.py

import numpy as np
import pandas as pd


def generate_random_portfolios(returns, n_portfolios=5000):
    results = []

    for _ in range(n_portfolios):
        weights = np.random.random(len(returns.columns))
        weights /= np.sum(weights)

        ret = np.sum(returns.mean() * weights) * 12
        vol = np.sqrt(weights.T @ (returns.cov() * 12) @ weights)
        sharpe = ret / vol

        results.append([ret, vol, sharpe])

    return pd.DataFrame(results, columns=["Return", "Volatility", "Sharpe"])
