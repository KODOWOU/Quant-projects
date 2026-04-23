# Geometric Brownian Motion Simulation

## Overview

This project implements a simulation of asset price dynamics using the **Geometric Brownian Motion (GBM)** model.

It provides a flexible framework to generate multiple stochastic price paths, analyze terminal wealth distributions, and visualize the impact of key financial parameters such as drift and volatility.

An interactive component allows real-time exploration of model behavior.

---

## Model Description

The Geometric Brownian Motion is a standard model for asset price evolution in continuous time.

### Continuous-Time Model

The asset price follows the stochastic differential equation:

dS_t = μ S_t dt + σ S_t dW_t

where:

* μ is the drift (expected return)
* σ is the volatility
* W_t is a Wiener process

---

### Discrete-Time Approximation

The model is discretized as:

S_{t+1} = S_t × exp[(μ − 0.5 σ²)Δt + σ √Δt Z]

where:

* Z ~ N(0,1)

---

### Simplified Implementation

In this project, returns are simulated using a discretized approximation:

* Gaussian shocks are generated
* Returns are computed per time step
* Prices are obtained via cumulative product

---

## Features

* Simulation of multiple GBM price paths
* Configurable parameters:

  * Time horizon
  * Drift (μ)
  * Volatility (σ)
  * Initial price
  * Number of scenarios
* Visualization of simulated price trajectories
* Distribution analysis of terminal wealth
* Interactive exploration using widgets

---

## Implementation Details

### Core Function

The main function generates simulated price paths:

```python
def gbm(n_years=10, n_scenarios=100, mu=0.07, sigma=0.15, steps_per_year=12, s_0=100):
```

Key steps:

* Define time step Δt
* Generate Gaussian random variables
* Compute returns
* Build price paths via cumulative product

---

### Handling Initial Value

Several approaches were tested:

* Direct simulation
* Overwriting first step
* Prepending initial value

The final implementation ensures:

* Correct initialization at S₀
* Consistent expected terminal value

---

### Interactive Visualization

An interactive tool allows dynamic exploration of parameters:

* Drift (μ)
* Volatility (σ)
* Time horizon
* Number of simulations

Outputs:

* Simulated price paths
* Histogram of terminal wealth

---

## Economic Intuition

### Randomness and Uncertainty

Asset prices evolve with uncertainty driven by stochastic shocks.

### Drift (μ)

Represents expected return:

* Higher μ → upward trend

### Volatility (σ)

Measures uncertainty:

* Higher σ → wider dispersion of outcomes

### Compounding Effect

Returns accumulate multiplicatively, leading to exponential growth dynamics.

---

## Results

Typical observations:

* Increasing volatility increases dispersion of terminal wealth
* Higher drift shifts the distribution upward
* Even with positive drift, some scenarios lead to losses
* Long-term outcomes are highly sensitive to volatility

The simulation highlights the asymmetry and uncertainty inherent in financial markets.

---

## Limitations

* Assumes constant drift and volatility
* No jumps or extreme events
* No stochastic volatility
* No market frictions
* Simplified discretization

---

## Possible Improvements

* Exact GBM discretization (log formulation)
* Variance reduction techniques
* Calibration to real market data
* Extension to stochastic volatility models (e.g. Heston)
* Multi-asset simulation

---

## Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* ipywidgets

---

## Author

Kodjo Anthelme Kodowou
Junior Quantitative Analyst

---

## Disclaimer

This project is for educational purposes only and does not constitute financial advice.

