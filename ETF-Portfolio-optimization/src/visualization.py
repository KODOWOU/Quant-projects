# src/visualization.py

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set_style("whitegrid")


# ============================================================
# Courbe de performance cumulée
# ============================================================

def plot_performance(cum_returns, title="Portfolio Performance"):
    plt.figure(figsize=(12, 6))
    cum_returns.plot(label="Portfolio", linewidth=2)
    plt.xlabel("Time")
    plt.ylabel("Cumulative Growth")
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.show()


# ============================================================
# Drawdown
# ============================================================

def plot_drawdown(cum_returns):
    rolling_max = cum_returns.cummax()
    drawdowns = (cum_returns - rolling_max) / rolling_max

    plt.figure(figsize=(12, 4))
    drawdowns.plot(color="red", linewidth=2)
    plt.title("Portfolio Drawdown")
    plt.xlabel("Time")
    plt.ylabel("Drawdown")
    plt.grid(True)
    plt.show()


# ============================================================
# Distribution des rendements journaliers
# ============================================================

def plot_return_distribution(returns):
    plt.figure(figsize=(10, 5))
    sns.histplot(returns, bins=50, kde=True, color="blue")
    plt.title("Distribution of Daily Returns")
    plt.xlabel("Daily Return")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()


# ============================================================
# Heatmap de corrélation
# ============================================================

def plot_correlation_heatmap(returns):
    corr = returns.corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix (Heatmap)")
    plt.show()


# ============================================================
# Matrice de corrélation simple
# ============================================================

def plot_correlation_matrix(returns):
    corr = returns.corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.show()


# ============================================================
# Répartition des poids
# ============================================================

def plot_weights(weights, labels):
    plt.figure(figsize=(8, 6))
    plt.bar(labels, weights)
    plt.title("Portfolio Weights")
    plt.ylabel("Weight")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()


# ============================================================
# Rendements annuels
# ============================================================

def plot_annual_returns(portfolio_returns):
    df = portfolio_returns.to_frame("ret")
    df["year"] = df.index.year
    annual = df.groupby("year")["ret"].sum()

    plt.figure(figsize=(10, 5))
    annual.plot(kind="bar", color="green")
    plt.title("Annual Returns")
    plt.ylabel("Return")
    plt.grid(True)
    plt.show()


# ============================================================
# Rolling volatility
# ============================================================

def plot_rolling_volatility(returns, window=252):
    rolling_vol = returns.rolling(window).std() * np.sqrt(252)

    plt.figure(figsize=(12, 5))
    rolling_vol.plot(label=f"Rolling Volatility ({window} days)")
    plt.title("Rolling Volatility")
    plt.xlabel("Time")
    plt.ylabel("Volatility")
    plt.grid(True)
    plt.legend()
    plt.show()


# ============================================================
# Rolling Sharpe ratio
# ============================================================

def plot_rolling_sharpe(returns, window=252, risk_free_rate=0.0):
    rolling_ret = returns.rolling(window).mean() * 252
    rolling_vol = returns.rolling(window).std() * np.sqrt(252)
    rolling_sharpe = (rolling_ret - risk_free_rate) / rolling_vol

    plt.figure(figsize=(12, 5))
    rolling_sharpe.plot(label=f"Rolling Sharpe ({window} days)")
    plt.title("Rolling Sharpe Ratio")
    plt.xlabel("Time")
    plt.ylabel("Sharpe Ratio")
    plt.grid(True)
    plt.legend()
    plt.show()


# ============================================================
# Efficient Frontier (si optimisation)
# ============================================================

def plot_efficient_frontier(df):
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Volatility"], df["Return"], c=df["Sharpe"], cmap="viridis")
    plt.colorbar(label="Sharpe Ratio")
    plt.xlabel("Volatility")
    plt.ylabel("Return")
    plt.title("Efficient Frontier")
    plt.grid(True)
    plt.show()
