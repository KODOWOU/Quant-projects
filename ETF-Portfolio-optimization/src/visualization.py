# src/visualization.py
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

def plot_efficient_frontier(df):
    """
    Plot the efficient frontier with volatility on x-axis and return on y-axis.
    Color represents the Sharpe ratio.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Volatility"], df["Return"], c=df["Sharpe"], cmap="viridis")
    plt.colorbar(label="Sharpe Ratio")
    plt.xlabel("Volatility")
    plt.ylabel("Return")
    plt.title("Efficient Frontier")
    plt.grid(True)
    plt.show()


def plot_performance(cum_returns, title="Portfolio Performance"):
    """
    Plot cumulative returns of the portfolio.
    """
    plt.figure(figsize=(12, 6))
    cum_returns.plot(label="Portfolio")
    plt.xlabel("Time")
    plt.ylabel("Cumulative Growth")
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.show()


def plot_drawdown(cum_returns):
    """
    Plot drawdowns over time.
    """
    rolling_max = cum_returns.cummax()
    drawdowns = (cum_returns - rolling_max) / rolling_max

    plt.figure(figsize=(12, 4))
    drawdowns.plot(color="red", label="Drawdown")
    plt.title("Portfolio Drawdown")
    plt.xlabel("Time")
    plt.ylabel("Drawdown")
    plt.grid(True)
    plt.legend()
    plt.show()
