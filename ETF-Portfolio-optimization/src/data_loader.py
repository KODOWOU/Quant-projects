# src/data_loader.py

import yfinance as yf
import pandas as pd


def load_data(tickers, start_date="2013-01-01"):
    """
    Download adjusted close prices from Yahoo Finance
    """

    data = yf.download(list(tickers.values()), start=start_date)["Adj Close"]

    # Rename columns with clean names
    data.columns = list(tickers.keys())

    # Drop rows with too many missing values
    data = data.dropna(how="all")

    # Forward fill missing values
    data = data.ffill().bfill()

    return data
