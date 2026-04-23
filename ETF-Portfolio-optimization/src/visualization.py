# src/visualization.py

import matplotlib.pyplot as plt


def plot_efficient_frontier(df):
    plt.scatter(df["Volatility"], df["Return"], c=df["Sharpe"])
    plt.xlabel("Volatility")
    plt.ylabel("Return")
    plt.title("Efficient Frontier")
    plt.colorbar(label="Sharpe Ratio")
    plt.show()


def plot_performance(cum_returns, title="Portfolio Performance"):
    cum_returns.plot(figsize=(10, 5), title=title)
    plt.xlabel("Time")
    plt.ylabel("Growth")
    plt.show()
