# data_loader.py

import yfinance as yf
import pandas as pd
import time 

def load_data(
        ticker: str,
        start: str = None, # i l’utilisateur ne donne pas de date, la valeur par défaut est None
        end: str = None,
        timeframe: str = '1d', # la valeur par défaut est '1d' pour les données journalières
        max_retries: int = 5,
):
    """
    Load historical stock data from Yahoo Finance.

    Parameters:
    ticker (str): Stock ticker symbol.
    start (str): Start date in 'YYYY-MM-DD' format. Default is None.
    end (str): End date in 'YYYY-MM-DD' format. Default is None.
    timeframe (str): Data interval (e.g., '1d', '1h'). Default is '1d'.
    max_retries (int): Maximum number of retries for data loading. Default is 5.

    Returns:
    pd.DataFrame: Historical stock data.
    """
    #  1 Attempt to load data with retries in case of failure.
    for attempt in range(max_retries):
        try:
            df = yf.download(
                ticker,
                start=start,
                end=end,
                interval=timeframe,
                progress=False  
            )
        except Exception as e:
            print(f"Erreur réseau : {e}")

        # Si on a des données, on arrête les tentatives. 
        if not df.empty:
            break
        print(f"⚠️ Tentative {attempt+1}/{max_retries} échouée. Nouvelle tentative...")
        time.sleep(2)  # Attendre 2 secondes avant la prochaine tentative.

        # Si après toutes les tentatives, on n'a toujours pas de données, on affiche un message d'erreur.
    if df.empty:
        raise ValueError(f"❌ Impossible de télécharger {ticker} après {max_retries} tentatives.")
    
    # 2 Correction MultiIndex 
    if isinstance(df.columns, pd.MultiIndex):
        print("Les données sont  MultiIndex, correction en cours...")
        df.columns = df.columns.get_level_values(0)  # On prend le premier niveau des colonnes.

    # 3 Vérification des colonnes OHLCV
    required_cols = ['Open', 'High', 'Low', 'Close', 'Volume']

    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Colonne manquante : {col} dans les données téléchargées pour {ticker}.")
            df[col] = 0  # Ajouter la colonne manquante avec des valeurs par défaut (0).

    # 4 Nettoyage final des données
    df = df[required_cols].dropna()  # Garder uniquement les colonnes OHLCV et supprimer les lignes avec des valeurs manquantes.
    print(f"✅ Données pour {ticker} chargées avec succès après {attempt+1} tentatives.")

    # 5 Index propre (datetime)
    df.index = pd.to_datetime(df.index)  # S'assurer que l'index est au format datetime.

    return df