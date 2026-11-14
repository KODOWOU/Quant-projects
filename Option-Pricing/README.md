# Black-Scholes Option Pricing in C++

## Overview

This project implements the Black-Scholes model for pricing European options in C++.
It also includes a Monte Carlo simulation to estimate option prices and compare numerical results with analytical solutions.

The goal is to demonstrate a solid understanding of quantitative finance concepts and efficient numerical implementation in C++.

---

## Features

* Analytical pricing of European Call and Put options
* Monte Carlo simulation for option pricing
* Comparison between analytical and simulated prices
* Clean and minimal C++ implementation

---

## Model Description

The Black-Scholes model assumes:

* Log-normal distribution of asset prices
* Constant volatility
* Constant risk-free rate
* No arbitrage
* Continuous trading

The call option price is computed using:

C = S * N(d1) - K * e^{-rT} * N(d2)

---

## Monte Carlo Simulation

The Monte Carlo approach simulates terminal asset prices:

* Generate random normal variables
* Simulate asset paths at maturity
* Compute discounted payoff

This provides a numerical approximation of the option price.

---

## Parameters

The model uses the following inputs:

* S: Spot price
* K: Strike price
* T: Time to maturity
* r: Risk-free rate
* sigma: Volatility

---

## Results

The analytical and Monte Carlo prices are expected to be close when the number of simulations is sufficiently large.

Actual output (S = K = 100, T = 1, r = 5%, σ = 20%, 100,000 simulations, seed 42), compiled with `g++ -std=c++17 -O2 black_scholes.cpp -o bs`:

```
Black-Scholes Call Price: 10.4506
Black-Scholes Put Price:  5.57353
Monte Carlo Call Price:   10.4741
```

The Monte Carlo estimate is within 0.03 of the analytical price.

---

## Economic Intuition

* Option value increases with volatility (higher uncertainty)
* Call option value increases with underlying price
* Discounting reflects time value of money

The Monte Carlo method illustrates how option pricing can be viewed as an expected discounted payoff under the risk-neutral measure.

---

## Known issues / Rebuild in progress

> This project will be extended into **QuantLibLite**, a C++17 derivatives pricing library (link will be added here). Current limits:

* No Greeks yet (delta, gamma, vega).
* No confidence interval for the Monte Carlo estimate and no variance reduction.
* No build file (CMake) and no automated tests.

---

## Limitations

* Assumes constant volatility (no stochastic volatility)
* No dividends included
* Monte Carlo simulation can be computationally expensive
* No Greeks (sensitivities) implemented

---

## Possible Improvements

* Add Greeks (Delta, Gamma, Vega)
* Implement variance reduction techniques
* Extend to American options
* Introduce stochastic volatility models (e.g. Heston)

---

## Author

Kodjo Anthelme Kodowou
MSc student, Financial Market Engineering (Université de Lorraine)

---

## Disclaimer

This project is for educational purposes only and does not constitute financial advice.
