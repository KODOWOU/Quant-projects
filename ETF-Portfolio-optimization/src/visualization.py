# src/visualization.py

import matplotlib.pyplot as plt


def plot_prices(prices):
    prices.plot(figsize=(10, 5), title="Asset Prices")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.show()


def plot_cumulative_returns(cum_returns):
    cum_returns.plot(figsize=(10, 5), title="Cumulative Returns")
    plt.xlabel("Time")
    plt.ylabel("Growth")
    plt.show()
