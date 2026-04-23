# main.py

from src.data_loader import load_data
from src.returns import compute_monthly_returns
from src.optimization import maximize_sharpe
from src.efficient_frontier import generate_random_portfolios
from src.rolling_backtest import rolling_backtest
from src.momentum import momentum_strategy, apply_strategy
from src.visualization import plot_efficient_frontier, plot_performance


tickers = {
    "World": "CW8.PA",
    "US_Growth": "VUG",
    "US_Value": "VTV",
    "Bonds": "TLT",
    "Gold": "GLD"
}

# Load data
prices = load_data(tickers)

# Returns
returns = compute_monthly_returns(prices)

# Sharpe optimization
weights = maximize_sharpe(returns)
print("Optimal weights:", weights)

# Efficient frontier
ef = generate_random_portfolios(returns)
plot_efficient_frontier(ef)

# Rolling backtest
ret_rb, cum_rb = rolling_backtest(returns)
plot_performance(cum_rb, "Rolling Backtest")

# Momentum strategy
weights_mom = momentum_strategy(returns)
ret_mom = apply_strategy(returns, weights_mom)
plot_performance((1 + ret_mom).cumprod(), "Momentum Strategy")
