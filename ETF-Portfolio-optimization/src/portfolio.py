# src/portfolio.py

import numpy as np
import pandas as pd

def portfolio_return(weights, returns):
    """
    Compute daily portfolio returns from asset daily returns and weights.
    """
    # Produit matriciel entre les rendements journaliers des actifs et les poids du portefeuille.
    # Cela calcule le rendement journalier total du portefeuille : somme(w_i * r_i(t)).

    return returns @ weights


def max_drawdown(cumulative_returns):
    """
    Compute maximum drawdown from cumulative returns.
    """
    # rolling_max : plus haut niveau historique du portefeuille à chaque date.
    # drawdowns : chute relative par rapport à ce sommet historique.
    # Le max drawdown est la pire chute observée, donc la valeur la plus négative.

    rolling_max = cumulative_returns.cummax()
    drawdowns = (cumulative_returns - rolling_max) / rolling_max
    return drawdowns.min() # Parce que le drawdown est négatif, on prend le minimum pour obtenir la plus grande perte.


def portfolio_metrics(weights, returns, risk_free_rate=0.0):
    """
    Compute all key portfolio metrics using DAILY returns:
    - Annualized return
    - Annualized volatility
    - Sharpe ratio
    - Max drawdown
    - Best year
    - Worst year
    - Value-at-Risk (95%)
    - Expected Shortfall (95%)
    """

    # Daily portfolio returns
    port_ret = portfolio_return(weights, returns)

    # Annualized return (daily → annual)
    ann_return = port_ret.mean() * 252

    # Annualized volatility (daily → annual)
    ann_vol = port_ret.std() * np.sqrt(252)

    # Sharpe ratio
    sharpe = (ann_return - risk_free_rate) / ann_vol if ann_vol != 0 else np.nan

    # Cumulative returns for drawdown
    cumulative = (1 + port_ret).cumprod()
    max_dd = max_drawdown(cumulative)

    # Annual performance (sum of daily returns per year)
    df = port_ret.to_frame("ret")
    df["year"] = df.index.year
    annual_returns = df.groupby("year")["ret"].sum()

    best_year = annual_returns.max()
    worst_year = annual_returns.min()

    # Value-at-Risk (95%)
    var_95 = np.percentile(port_ret, 5)

    # Expected Shortfall (95%)
    es_95 = port_ret[port_ret <= var_95].mean()

    return {
        "annual_return": ann_return,
        "annual_volatility": ann_vol,
        "sharpe_ratio": sharpe,
        "max_drawdown": max_dd,
        "best_year": best_year,
        "worst_year": worst_year,
        "var_95": var_95,
        "expected_shortfall_95": es_95,
        "cumulative_returns": cumulative,
        "annual_returns": annual_returns
    }
