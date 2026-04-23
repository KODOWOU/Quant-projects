# src/optimization.py

import numpy as np
from scipy.optimize import minimize


def minimize_volatility(weights, returns):
    cov = returns.cov() * 12
    return np.sqrt(weights.T @ cov @ weights)


def optimize_portfolio(returns):
    n = returns.shape[1]

    init_weights = np.ones(n) / n

    bounds = [(0, 1) for _ in range(n)]
    constraints = {"type": "eq", "fun": lambda w: np.sum(w) - 1}

    result = minimize(
        minimize_volatility,
        init_weights,
        args=(returns,),
        method="SLSQP",
        bounds=bounds,
        constraints=constraints,
    )

    return result.x
