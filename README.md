# Quantitative Finance Projects Portfolio

## Overview

This repository contains a collection of quantitative finance projects developed to explore and implement key concepts used in systematic trading, portfolio management, and financial modeling.

The goal of this portfolio is to demonstrate practical skills in:

* Quantitative modeling
* Portfolio optimization
* Derivative pricing
* Market simulation
* Systematic trading strategies
* Data analysis and visualization

Each project is designed to be modular, self-contained, and aligned with real-world quantitative finance applications.

---

## Repository Structure

```id="q9k2xv"
Quant-projects/
│
├── Brownian-Motion/                 # Stochastic process simulation (GBM)
├── ETF-Portfolio-optimization/      # Portfolio allocation & optimization
├── Option-Pricing/                  # Black-Scholes + Monte Carlo pricing
├── Trading_Strategies_Backtest/     # Market scanner & strategy framework
└── README.md                        # Global portfolio overview
```

---

## Projects Description

### 1. Geometric Brownian Motion Simulation

This project implements stochastic modeling of asset prices using the Geometric Brownian Motion framework.

**Key Features:**

* Simulation of multiple price paths
* Terminal wealth distribution analysis
* Interactive parameter exploration (drift, volatility, horizon)

**Core Concepts:**

* Stochastic differential equations
* Continuous-time finance models
* Monte Carlo simulation

---

### 2. ETF Portfolio Optimization

A full portfolio construction framework based on ETF assets.

**Key Features:**

* Mean-variance optimization (Markowitz framework)
* Maximum Sharpe ratio portfolio
* Efficient frontier simulation
* Rolling backtesting
* Momentum-based allocation strategy

**Core Concepts:**

* Portfolio theory
* Risk-return optimization
* Factor investing
* Dynamic asset allocation

---

### 3. Option Pricing (Black-Scholes Model)

Implementation of European option pricing using analytical and numerical methods.

**Key Features:**

* Black-Scholes closed-form solution
* Monte Carlo simulation pricing
* Comparison of numerical vs analytical results

**Core Concepts:**

* Derivatives pricing
* Risk-neutral valuation
* Numerical simulation methods

---

### 4. Trading Strategies & Market Regime Framework

A modular system for detecting market regimes and applying adaptive trading strategies.

**Key Features:**

* Market regime detection (trend, volatility, range, impulse)
* Multi-asset market scanner
* Strategy selection based on regime
* Backtesting engine (in progress)
* Streamlit dashboard

**Core Concepts:**

* Systematic trading
* Regime-based allocation
* Momentum and mean reversion strategies
* Algorithmic trading infrastructure

---

## Skills Demonstrated

This portfolio demonstrates proficiency in:

### Programming

* Python (NumPy, Pandas, SciPy, Matplotlib)
* R (portfolio analysis)
* C++ (numerical pricing models)

### Quantitative Finance

* Stochastic processes
* Portfolio optimization
* Derivatives pricing
* Risk management
* Time series analysis

### Systematic Trading

* Backtesting frameworks
* Factor strategies
* Market regime detection
* Signal generation

---

## Economic Intuition

The projects are built around key financial principles:

* Markets are stochastic and can be modeled probabilistically
* No single strategy performs well in all market regimes
* Diversification reduces risk but does not eliminate it
* Risk-return tradeoff is central to portfolio construction
* Adaptive systems outperform static allocations in dynamic environments

---

## Key Takeaways

* Financial markets can be modeled using stochastic processes
* Portfolio performance depends heavily on allocation methodology
* Strategy performance is regime-dependent
* Backtesting is essential to validate systematic approaches
* Robust systems combine multiple models and signals

---

## Limitations

* Simplified assumptions (no transaction costs, no slippage)
* Reliance on Yahoo Finance data
* Some models assume constant volatility
* Backtesting framework still under development in parts
* No real-time execution layer

---

## Future Improvements

* Integration of transaction costs and slippage
* Advanced regime models (HMM, clustering)
* Walk-forward optimization
* Multi-asset portfolio engine
* Live trading integration (paper trading)

---

## Author

Kodjo Anthelme Kodowou
Junior Quantitative Analyst
Based in France

---

## Disclaimer

This repository is intended for educational and research purposes only.
It does not constitute financial advice or investment recommendations.
