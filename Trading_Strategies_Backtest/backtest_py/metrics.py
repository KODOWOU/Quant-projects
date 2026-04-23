# backtest.metrics.py

import numpy as np
import pandas as pd

# ============================================================
#   DÉTECTION AUTOMATIQUE DE LA FRÉQUENCE
# ============================================================

def detect_frequency(index: pd.DatetimeIndex):
    """
    Déduit automatiquement la fréquence réelle du dataset.
    Retourne le nombre de périodes par an pour annualiser.
    """

    # différence médiane entre deux timestamps
    delta = (index[1:] - index[:-1]).median()

    seconds = delta.total_seconds()

    # --- Intraday ---
    if seconds < 3600:  # moins d'une heure
        return int((252 * 6.5 * 3600) / seconds)   # 252 jours * 6.5h * 3600s

    if seconds < 86400:  # moins d'un jour
        return int((252 * 6.5) / (seconds / 3600))  # 6.5h par jour

    # --- Daily ---
    if seconds < 7 * 86400:
        return 252

    # --- Weekly ---
    if seconds < 30 * 86400:
        return 52

    # --- Monthly ---
    return 12


# ============================================================
#   MÉTRIQUES BASÉES SUR L'EQUITY CURVE
# ============================================================

def compute_equity_metrics(equity: pd.Series):
    """
    Calcule les métriques basées sur l'equity curve.
    Annualisation automatique selon la fréquence détectée.
    Args:
        equity (pd.Series): Série temporelle de l'equity curve du backtest.
    Returns:
        dict: Dictionnaire contenant les métriques calculées.
    """

    returns = equity.pct_change().dropna()

    periods_per_year = detect_frequency(equity.index)

    # --- Rendements ---
    total_return = equity.iloc[-1] / equity.iloc[0] - 1
    annualized_return = (1 + total_return) ** (periods_per_year / len(equity)) - 1

    # --- Volatilité ---
    annualized_vol = returns.std() * np.sqrt(periods_per_year)

    # --- Sharpe ---
    sharpe = annualized_return / annualized_vol if annualized_vol > 0 else np.nan

    # --- Sortino ---
    # Seule la volatilité des rendements négatifs est prise en compte pour le ratio de Sortino.
    downside = returns[returns < 0].std() * np.sqrt(periods_per_year)
    sortino = annualized_return / downside if downside > 0 else np.nan

    # --- Max Drawdown ---
    rolling_max = equity.cummax()
    drawdown = (equity - rolling_max) / rolling_max
    max_drawdown = drawdown.min()

    # --- Calmar ---
    # Mesure le rendement annualisé par rapport au max drawdown.
    calmar = annualized_return / abs(max_drawdown) if max_drawdown != 0 else np.nan

    return {
        "total_return": total_return,
        "annualized_return": annualized_return,
        "annualized_volatility": annualized_vol,
        "sharpe_ratio": sharpe,
        "sortino_ratio": sortino,
        "max_drawdown": max_drawdown,
        "calmar_ratio": calmar
    }


# ============================================================
#   MÉTRIQUES BASÉES SUR LES TRADES
# ============================================================

def compute_trade_metrics(trades: pd.DataFrame):
    """
    Calcule les métriques basées sur les trades.
    """

    if trades.empty:
        return {
            "num_trades": 0,
            "win_rate": np.nan,
            "profit_factor": np.nan,
            "avg_win": np.nan,
            "avg_loss": np.nan,
            "expectancy": np.nan,
            "avg_duration": np.nan
        }

    wins = trades[trades["pnl"] > 0]
    losses = trades[trades["pnl"] < 0]

    num_trades = len(trades)
    win_rate = len(wins) / num_trades if num_trades > 0 else np.nan

    avg_win = wins["pnl"].mean() if len(wins) > 0 else np.nan
    avg_loss = losses["pnl"].mean() if len(losses) > 0 else np.nan

    profit_factor = wins["pnl"].sum() / abs(losses["pnl"].sum()) if len(losses) > 0 else np.nan

    expectancy = trades["pnl"].mean()

    avg_duration = trades["duration"].mean()

    return {
        "num_trades": num_trades,
        "win_rate": win_rate,
        "profit_factor": profit_factor,
        "avg_win": avg_win,
        "avg_loss": avg_loss,
        "expectancy": expectancy,
        "avg_duration": avg_duration
    }


# ============================================================
#   MÉTRIQUES COMBINÉES
# ============================================================

def compute_all_metrics(equity: pd.Series, trades: pd.DataFrame):
    """
    Combine equity metrics + trade metrics dans un seul dictionnaire.
    """

    equity_metrics = compute_equity_metrics(equity)
    trade_metrics = compute_trade_metrics(trades)

    return {
        **equity_metrics,
        **trade_metrics
    }
