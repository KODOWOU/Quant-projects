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

Typical output:

* Black-Scholes Call Price ≈ X
* Monte Carlo Call Price ≈ X (close value)

---

## Economic Intuition

* Option value increases with volatility (higher uncertainty)
* Call option value increases with underlying price
* Discounting reflects time value of money

The Monte Carlo method illustrates how option pricing can be viewed as an expected discounted payoff under the risk-neutral measure.

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
Junior Quantitative Analyst

---

## Disclaimer

This project is for educational purposes only and does not constitute financial advice.
