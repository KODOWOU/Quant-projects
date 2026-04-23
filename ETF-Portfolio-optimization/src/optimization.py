# src/optimization.py

import numpy as np
from scipy.optimize import minimize


def portfolio_performance(weights, returns):
    port_return = np.sum(returns.mean() * weights) * 12
    port_vol = np.sqrt(weights.T @ (returns.cov() * 12) @ weights)
    return port_return, port_vol


def negative_sharpe(weights, returns, risk_free_rate=0.0):
    ret, vol = portfolio_performance(weights, returns)
    return -(ret - risk_free_rate) / vol


def maximize_sharpe(returns):
    n = returns.shape[1]
    init = np.ones(n) / n

    bounds = [(0, 1)] * n
    constraints = {"type": "eq", "fun": lambda w: np.sum(w) - 1}

    result = minimize(
        negative_sharpe,
        init,
        args=(returns,),
        method="SLSQP",
        bounds=bounds,
        constraints=constraints,
    )

    return result.x
