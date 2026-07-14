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

    # Pour chaque ETF, on récupère la première date où des données valides apparaissent.
    # Cela permet d’identifier le moment où l’actif commence réellement à exister dans l’historique.
    first_valid_dates = data.apply(lambda col: col.first_valid_index())

    # On sélectionne la date la plus récente parmi toutes les premières dates valides.
    # Cette date correspond au moment où tous les ETF ont des données disponibles simultanément.
    true_start = max(first_valid_dates)

    # On tronque le DataFrame pour ne conserver que les données à partir de cette date.
    # Cela garantit un backtest propre, sans valeurs manquantes ni périodes où certains ETF n’existaient pas encore.
    data = data[data.index >= true_start]


    return data
