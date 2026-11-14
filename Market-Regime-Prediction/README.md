# Market Regime Prediction — Momentum vs Reversion

Machine learning pipeline to predict, on a daily basis, whether the equity market is more likely to trend (momentum) or mean-revert (reversion) the next day, and to test whether this signal is exploitable in a simple asset allocation strategy.

## Objective

Two opposing market logics are compared: momentum (persistence of recent trends) and reversion (correction of price excesses). The notebook builds a full ML pipeline to classify the next-day regime and evaluates whether this prediction adds value in a SPY/TLT allocation strategy.

## Methodology

- **Data**: SPY, VIX and TLT prices (Yahoo Finance), momentum/reversal style factors (Ken French Data Library). If the factors cannot be loaded, the current notebook falls back to synthetic data (see Known issues).
- **Features**: RSI, normalized ATR, realized volatility, VIX level and change, multi-horizon returns, trend slope, lagged variables. Features are designed to use only past information; see Known issues for the exceptions found in the current notebook.
- **Validation**: walk-forward with expanding training window, models retrained at each fold, strict respect of chronological order.
- **Models compared**: majority baseline, Logistic Regression, XGBoost, Keras MLP (with dropout and L2 regularization).
- **Interpretability**: XGBoost feature importances (SHAP analysis planned, not yet run).
- **Backtest**: signal-based allocation between SPY and TLT, with transaction costs, benchmarked against buy-and-hold SPY and a 60/40 portfolio.

## Results

Model comparison (Accuracy, F1, AUC-ROC) and backtest performance (annualized return, Sharpe, Sortino, max drawdown) are detailed in the notebook.

## Known issues / Rebuild in progress

> This project is being rebuilt as **Regime-Aware Allocation** (link will be added here). **Do not use the metrics of the current notebook.**

- **Synthetic fallback was used.** In the executed notebook the Ken French factors failed to load (`ModuleNotFoundError`) and the code silently switched to synthetic factors. The target (`MOM > ST_REV`) was then built from SPY returns plus noise, while `MOM` and `ST_REV` themselves stayed in the feature set. The classification metrics (accuracy, AUC) are therefore mechanical and say nothing about a market signal.
- **Even with real data**, the code sets `ST_REV = -MOM`, which reduces the regime to `MOM > 0`, and the monthly momentum factor forward-filled on daily dates introduces look-ahead bias.
- **Backtest, as run:** the SPY/TLT allocation returned about −2.4% a year (Sharpe −0.05), versus about +16% a year for buy-and-hold SPY. This run used the synthetic factors.
- Planned fixes: daily Ken French factors, `MOM`/`ST_REV` removed from the features, the code stops with an explicit error if data is missing, full re-run and real figures in this README.

## Tools

Python, Pandas, NumPy, Scikit-learn, XGBoost, TensorFlow/Keras, Matplotlib, yfinance, pandas-datareader.

## Limitations

Regime definition based on a convention, simplified transaction costs, non-stationarity of financial markets. See notebook conclusion for detailed discussion and next steps.

## File

- `market_regime_prediction_improved.ipynb`: full notebook (data loading, feature engineering, modeling, evaluation, backtest).
