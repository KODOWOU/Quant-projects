# ETF Portfolio Allocation & Backtesting Strategy

## Overview

This project implements a quantitative framework for ETF portfolio allocation and backtesting.
It combines portfolio optimization, factor-based strategies, and rolling backtesting to evaluate systematic investment approaches across multiple asset classes.

The objective is to design robust and diversified portfolios using liquid ETFs, while assessing their performance under realistic market conditions.

---

## Key Features

* Multi-asset ETF universe (Equities, Bonds, Commodities, Crypto)
* Data pipeline using Yahoo Finance
* Monthly return computation and time series analysis
* Portfolio optimization (Maximum Sharpe Ratio)
* Efficient Frontier simulation
* Rolling window backtesting
* Momentum-based allocation strategy
* Sensitivity analysis on portfolio weights
* Visualization of performance and risk metrics

---

## Project Structure

```
etf-portfolio-strategy/
│
├── data/                # Stored datasets (optional CSV exports)
├── notebooks/           # Exploratory analysis and testing
├── src/
│   ├── data_loader.py
│   ├── returns.py
│   ├── portfolio.py
│   ├── optimization.py
│   ├── efficient_frontier.py
│   ├── rolling_backtest.py
│   ├── momentum.py
│   ├── sensitivity.py
│   └── visualization.py
│
├── main.py              
├── exploration.ipynb         # Main execution script
└── README.md
```

---

## Methodology

### 1. Data Collection

* Daily adjusted prices are downloaded using `yfinance`
* Data is cleaned, aligned, and forward-filled
* Monthly prices are computed using end-of-period sampling

---

### 2. Return Computation

* Log returns are used for stability and aggregation
* Monthly returns are derived from resampled price series

---

### 3. Portfolio Optimization

The portfolio is optimized using a **Maximum Sharpe Ratio approach**:

* Objective: maximize risk-adjusted return
* Constraints:

  * Fully invested portfolio (weights sum to 1)
  * Long-only (no short selling)

---

### 4. Efficient Frontier

* Random portfolios are generated
* Each portfolio’s return, volatility, and Sharpe ratio are computed
* The efficient frontier is visualized to assess the risk-return tradeoff

---

### 5. Rolling Backtest

A rolling window approach is used to simulate realistic investment conditions:

* Training window: historical data (e.g. 36 months)
* At each step:

  * Optimize portfolio on past data
  * Apply weights to next period returns

This avoids look-ahead bias and reflects real-world implementation.

---

### 6. Momentum Strategy

A cross-sectional momentum strategy is implemented:

* Assets are ranked based on past performance (lookback window)
* Top-performing ETFs are selected
* Equal weights are assigned to selected assets
* Portfolio is rebalanced periodically

---

### 7. Sensitivity Analysis

* Portfolio weights are perturbed (+/- shocks)
* Impact on returns is measured
* Helps identify concentration risk and robustness

---

## Economic Intuition

The project is grounded in well-established financial principles:

### Diversification

Combining multiple asset classes (equities, bonds, commodities, crypto) reduces idiosyncratic risk and improves portfolio stability.

### Risk-Return Tradeoff

The optimization framework seeks efficient portfolios that maximize return per unit of risk (Sharpe ratio).

### Momentum Effect

The momentum strategy exploits the empirical observation that assets with strong past performance tend to continue outperforming in the short-to-medium term.

### Dynamic Allocation

Rolling optimization allows the portfolio to adapt to changing market conditions rather than relying on static allocations.

---

## Results

Typical findings from the framework include:

* Optimized portfolios achieve higher Sharpe ratios compared to equal-weighted portfolios
* Momentum strategies can outperform static allocations in trending markets
* Rolling backtests show more realistic (and often lower) performance than static backtests
* Diversification across asset classes reduces drawdowns during market stress

Visualization outputs include:

* Efficient frontier (risk vs return)
* Cumulative performance curves
* Rolling portfolio performance
* Risk-return scatter plots

---

## Limitations

This project has several important limitations:

### No Transaction Costs

* Rebalancing is assumed to be frictionless
* In reality, transaction costs reduce performance

### Data Constraints

* Relies on Yahoo Finance data (may contain inconsistencies)
* ETF availability varies across regions

### Model Simplifications

* Mean-variance optimization assumes stable correlations
* Momentum strategy ignores market regimes

### No Constraints on Liquidity / AUM

* Real-world ETF selection would include liquidity filters

---

## Possible Improvements

* Incorporate transaction costs and slippage
* Add benchmark comparison (e.g. MSCI World)
* Implement risk parity or minimum variance strategies
* Include regime detection models
* Improve factor models (multi-factor approach)

---

## Technologies Used

* Python (NumPy, Pandas, SciPy)
* yfinance
* Matplotlib
* Object-oriented modular design

---

## Author

Kodjo Anthelme Kodowou
Junior Quantitative Analyst

---

## Disclaimer

This project is for educational purposes only and does not constitute investment advice.
