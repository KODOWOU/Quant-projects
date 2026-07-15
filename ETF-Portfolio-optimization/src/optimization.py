import numpy as np
from scipy.optimize import minimize

def portfolio_performance(weights, returns, risk_free_rate=0.0):
    """
    Compute annualized return and volatility using DAILY returns.
    """
    mean_daily = returns.mean()
    cov_daily = returns.cov()

    ann_return = np.sum(mean_daily * weights) * 252
    ann_vol = np.sqrt(weights.T @ (cov_daily * 252) @ weights)

    sharpe = (ann_return - risk_free_rate) / ann_vol
    return ann_return, ann_vol, sharpe


def negative_sharpe(weights, returns, risk_free_rate=0.0):
    _, _, sharpe = portfolio_performance(weights, returns, risk_free_rate)
    return -sharpe


def maximize_sharpe(returns, risk_free_rate=0.0):
    """
    Maximize Sharpe ratio with constraints:
    - weights >= 0
    - sum(weights) = 1
    """
    n = returns.shape[1]
    init = np.ones(n) / n

    bounds = [(0, 1)] * n
    constraints = {"type": "eq", "fun": lambda w: np.sum(w) - 1}

    result = minimize(
        negative_sharpe,
        init,
        args=(returns, risk_free_rate),
        method="SLSQP",
        bounds=bounds,
        constraints=constraints,
    )

    weights_opt = result.x
    ann_ret, ann_vol, sharpe = portfolio_performance(weights_opt, returns, risk_free_rate)

    return {
        "weights": weights_opt,
        "annual_return": ann_ret,
        "annual_volatility": ann_vol,
        "sharpe_ratio": sharpe
    }
