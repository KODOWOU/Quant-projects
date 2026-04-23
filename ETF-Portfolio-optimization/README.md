# ETF Portfolio Allocation & Backtesting Strategy

## Overview

This project implements a **quantitative portfolio allocation framework** based on ETFs across multiple asset classes.

It combines:

* Portfolio optimization (Maximum Sharpe Ratio)
* Factor investing (Momentum strategy)
* Rolling backtesting

The objective is to build **robust, diversified portfolios** and evaluate their performance under realistic market conditions.

---

##  How to Use This Project

 The main analysis and results are available in:

**`exploration.ipynb`**

This notebook contains:

* Data exploration
* Portfolio construction
* Backtesting results
* Visualizations

➡️ It is the **entry point of the project** and reflects the full research workflow.

---

## Key Features

* Multi-asset ETF universe:

  * Equities
  * Bonds
  * Commodities
  * Crypto (ETPs)
* Data pipeline using `yfinance`
* Monthly return computation
* Maximum Sharpe Ratio optimization
* Efficient Frontier simulation
* Rolling window backtesting (realistic)
* Momentum-based allocation (factor strategy)
* Sensitivity analysis on portfolio weights
* Full visualization of performance and risk metrics

---

## Project Structure

```text id="etfstruct1"
ETF-Portfolio-optimization/
│
├── data/                    # Optional data storage
├── exploration.ipynb        # Main research notebook (core of the project)
│
├── src/
│   ├── data_loader.py       # Data acquisition & cleaning
│   ├── returns.py           # Return computation
│   ├── portfolio.py         # Portfolio construction logic
│   ├── optimization.py      # Sharpe ratio maximization
│   ├── efficient_frontier.py # Frontier simulation
│   ├── rolling_backtest.py  # Rolling backtesting engine
│   ├── momentum.py          # Momentum factor strategy
│   ├── sensitivity.py       # Sensitivity analysis
│   └── visualization.py     # Plotting & charts
│
├── main.py                  # Optional script entry point
└── README.md
```

---

## Methodology

### 1. Data Collection

* ETF prices are downloaded using `yfinance`
* Data is aligned across assets
* Missing values are forward/backward filled
* Monthly prices are computed using end-of-period sampling

---

### 2. Return Computation

* Log returns are used for numerical stability
* Monthly returns are derived from resampled price series

---

### 3. Portfolio Optimization

The portfolio is optimized using a **Maximum Sharpe Ratio framework**:

* Objective:
  Maximize risk-adjusted return

* Constraints:

  * Fully invested portfolio (Σ weights = 1)
  * Long-only (no short selling)

---

### 4. Efficient Frontier

* Random portfolios are generated
* For each portfolio:

  * Expected return
  * Volatility
  * Sharpe ratio are computed
* The efficient frontier is plotted to visualize the risk-return tradeoff

---

### 5. Rolling Backtest (Key Component)

A rolling window approach is implemented to simulate realistic investment conditions:

* Training window: past data (e.g. 36 months)
* At each step:

  * Optimize portfolio on historical data
  * Apply weights to next period returns

✅ This removes look-ahead bias
✅ This mimics real portfolio management

---

### 6. Momentum Strategy

A cross-sectional momentum strategy is implemented:

* Assets are ranked based on past returns
* Top-performing ETFs are selected
* Equal-weight allocation
* Periodic rebalancing

---

### 7. Sensitivity Analysis

* Portfolio weights are perturbed
* Impact on performance is measured
* Used to assess robustness and concentration risk

---

## Economic Intuition

### Diversification

Combining multiple asset classes reduces idiosyncratic risk and improves stability.

---

### Risk-Return Tradeoff

The Sharpe optimization identifies portfolios that maximize return per unit of risk.

---

### Momentum Effect

Assets with strong past performance tend to continue outperforming (behavioral + structural effect).

---

### Dynamic Allocation

Rolling optimization adapts to market changes, unlike static portfolios.

---

## Results

The framework typically shows:

* Higher Sharpe ratios for optimized portfolios vs naive allocation
* Momentum strategies outperform in trending markets
* Rolling backtests produce more realistic (and lower) performance
* Diversification reduces drawdowns

### Outputs

* Efficient frontier
* Cumulative performance curves
* Rolling performance
* Risk-return scatter plots

---

## Limitations

* No transaction costs or slippage
* Reliance on Yahoo Finance data
* Mean-variance assumes stable correlations
* Momentum strategy does not include regime filtering
* No liquidity constraints

---

## Possible Improvements

* Add transaction costs and slippage
* Benchmark comparison (e.g. MSCI World)
* Risk parity / minimum variance strategies
* Integration with regime detection models
* Multi-factor strategies

---

## Technologies Used

* Python (NumPy, Pandas, SciPy)
* yfinance
* Matplotlib
* Modular architecture

---

## Author

Kodjo Anthelme Kodowou
Junior Quantitative Analyst

---

## Disclaimer

This project is for educational purposes only and does not constitute investment advice.
