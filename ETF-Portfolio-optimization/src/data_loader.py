# src/data_loader.py

import yfinance as yf
import pandas as pd

def load_data(tickers, start_date="2013-01-01"):
    """
    Robust loader for Yahoo Finance data.
    Always extracts 'Close' because 'Adj Close' is not available.
    """

    raw = yf.download(list(tickers.values()), start=start_date)

    if raw.empty:
        raise ValueError("Yahoo Finance returned no data. Check ticker symbols.")

    # MultiIndex case (most common)
    if isinstance(raw.columns, pd.MultiIndex):

        # Use Close prices (Adj Close not available)
        if "Close" in raw.columns.get_level_values(0):
            data = raw["Close"]
        else:
            raise ValueError(f"No 'Close' price found. Columns returned: {raw.columns}")

    # Single index case (rare)
    else:
        if "Close" in raw.columns:
            data = raw["Close"]
        else:
            raise ValueError(f"No 'Close' column found. Columns returned: {raw.columns}")

    # Rename columns using your dictionary keys
    data.columns = list(tickers.keys())

    # Clean missing values
    data = data.dropna(how="all").ffill().bfill()

    return data
