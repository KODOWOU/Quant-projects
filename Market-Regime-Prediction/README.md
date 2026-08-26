# Market Regime Prediction — Momentum vs Reversion

Machine learning pipeline to predict, on a daily basis, whether the equity market is more likely to trend (momentum) or mean-revert (reversion) the next day, and to test whether this signal is exploitable in a simple asset allocation strategy.

## Objective

Two opposing market logics are compared: momentum (persistence of recent trends) and reversion (correction of price excesses). The notebook builds a full ML pipeline to classify the next-day regime and evaluates whether this prediction adds value in a SPY/TLT allocation strategy.

## Methodology

- **Data**: SPY, VIX and TLT prices (Yahoo Finance), momentum/reversal style factors (Ken French Data Library). Explicit synthetic fallback if data is unavailable, for full reproducibility.
- **Features**: RSI, normalized ATR, realized volatility, VIX level and change, multi-horizon returns, trend slope, lagged variables. All features use only past information (no look-ahead bias).
- **Validation**: walk-forward with expanding training window, models retrained at each fold, strict respect of chronological order.
- **Models compared**: majority baseline, Logistic Regression, XGBoost, Keras MLP (with dropout and L2 regularization).
- **Interpretability**: XGBoost feature importances and SHAP analysis.
- **Backtest**: signal-based allocation between SPY and TLT, with transaction costs, benchmarked against buy-and-hold SPY and a 60/40 portfolio.

## Results

Model comparison (Accuracy, F1, AUC-ROC) and backtest performance (annualized return, Sharpe, Sortino, max drawdown) are detailed in the notebook.

## Tools

Python, Pandas, NumPy, Scikit-learn, XGBoost, TensorFlow/Keras, SHAP, Matplotlib, yfinance, pandas-datareader.

## Limitations

Regime definition based on a convention, simplified transaction costs, non-stationarity of financial markets. See notebook conclusion for detailed discussion and next steps.

## File

- `market_regime_prediction.ipynb`: full notebook (data loading, feature engineering, modeling, evaluation, SHAP, backtest).
