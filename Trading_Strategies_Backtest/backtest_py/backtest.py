# backtest_py.backtest.py

import pandas as pd
import numpy as np

def execute_trades(df: pd.DataFrame, signal: pd.Series, params: dict):
    """
    Execute trades based on the provided signals and parameters.

    Parameters:
    df (pd.DataFrame): Historical stock data.
    signal (pd.Series): Trading signals (1 for buy, -1 for sell, 0 for hold).
    params (dict): Dictionary containing trading parameters such as capital, slippage, and fees.

    Returns:
    pd.Series: Equity curve representing the value of the portfolio over time.
    """
    # Paramètres d'exécution 

    fee = params.get("fee", 0.0001) # Frais de transaction (0.01% par défaut). La syntaxe : params.get("fee", 0.0001) signifie que si la clé "fee" n'est pas présente dans le dictionnaire params, alors la variable fee prendra la valeur par défaut de 0.0001 (soit 0.01% de frais de transaction). Si la clé "fee" est présente, alors fee prendra la valeur associée à cette clé dans le dictionnaire params.
    slipage = params.get("slippage", 0.0002) # Slippage (0.05% par défaut)
    initial_capital = params.get("initial_capital", 10000) # Capital initial (100 000 $ par défaut)
    quantity = params.get("quantity", 1) # Quantité de titres à acheter/vendre par trade (100 par défaut)
    capital = initial_capital
    position = 0  
    entry_price = None 

    equity_curve = []

    for i in range(1, len(df)): # Commence à 1 pour accéder à Open[i]
        today_signal = signal.iloc[i-1] # Le signal généré à  la bougie précédente
        open_price = df["Open"].iloc[i] # Prix d'ouverture de la bougie actuelle

        # Entrée en position
        if position == 0 and today_signal != 0:
            position = today_signal 
            entry_price = open_price * (1 + slipage * position) # Appliquer le slippage à l'entrée
            capital -= abs(capital * fee * quantity) # Appliquer les frais de transaction

        # Sortie de position execute_trades
        elif position != 0 and today_signal == 0:
            exit_price = open_price * (1 - slipage * position) # Appliquerle slippage à la sortie. C'est à dire si on est en position longue (position > 0), on vend à un prix légèrement inférieur (slippage négatif), et si on est en position courte (position < 0), on rachète à un prix légèrement supérieur (slippage positif).
            pnl = (exit_price - entry_price) * position * quantity   # Si la position est longue (position > 0), le PnL est positif si exit_price > entry_price. Si la position est courte (position < 0), le PnL est positif si exit_price < entry_price.
            capital += pnl # Ajouter le pnl au capital
            capital -= abs(capital * fee * quantity) # Appliquer les frais de transaction
            position = 0 # Réinitialiser la position
            entry_price = None # Réinitialiser le prix d'entrée

        # Mise à jour de la courbe d'équité
        if position != 0:
            current_price = df["Close"].iloc[i] # Utiliser le prix de clôture pour évaluer la position ouverte
            unrealized = (current_price - entry_price) * position * quantity # PnL non réalisé de la position ouverte
            equity_curve.append(capital + unrealized) # Ajouter le capital actuel plus le PnL non réalisé à la courbe d'équité

        else:
            equity_curve.append(capital) # Si pas de position ouverte, la courbe d'équité est simplement le capital
        
    return pd.Series(equity_curve, index=df.index[1:]) # Retourner la courbe d'équité en tant que Series pandas avec les mêmes index que les données historiques (en commençant à la deuxième ligne)    


def extract_trades(df: pd.DataFrame, signal: pd.Series, params: dict):
    """ 
    Transformer une série de signaux (1, -1, 0) en une liste de trades.
    Ne gère pas le capital, ni les frais de transaction, ni le slippage.
    Sert uniquement à analyser les trades.
    """
    trades = [] # Liste pour stocker les trades
    position = 0 # Initialiser la position à 0 (pas de position)
    entry_price = None # Initialiser le prix d'entrée à None
    entry_date = None # Initialiser la date d'entrée à None
    fee = params.get("fee", 0.0001) # Frais de transaction (0.01% par défaut)
    slippage = params.get("slippage", 0.0002) # Slippage (0.02% par défaut)
    quantity = params.get("quantity", 1) # Quantité de titres à acheter/vendre par trade (100 par défaut)

    for i in range(1, len(df)):
        prev_signal = signal.iloc[i-1] # Signal de la bougie précédente
        curr_signal = signal.iloc[i] # Signal de la bougie actuelle
        open_price = df["Open"].iloc[i]  # prix d'exécution aujourd'hui


        # Entrée en position 

        if position == 0 and prev_signal != 0:
            position = prev_signal # Prendre la position indiquée par le signal (1 pour long, -1 pour short)
            entry_price = open_price * (1 + slippage * position) # Prix d'entrée à l'ouverture de la bougie actuelle
            entry_date = df.index[i] # Date d'entrée
            entry_fee = abs(entry_price * fee * quantity) # Frais d'entrée

            # Sortie de position
        elif position != 0 and prev_signal == 0: # Si on est en position et que le signal précédent était devenu zero, alors on sort de la position.
            exit_date = df.index[i] # Date de sortie
            exit_price = open_price * (1 - slippage * position) # Prix de sortie à l'ouverture de la bougie actuelle
            exit_fee = abs(exit_price * fee * quantity) # Frais de sortie
            pnl = (exit_price - entry_price) * position * quantity  # Calcul du PnL de la position (sans les frais)
            pnl -= (entry_fee + exit_fee) # Soustraire les frais du PnL

            duration = (exit_date - entry_date) # Durée du trade 
            trades.append({
                "entry_date": entry_date,
                "entry_price": entry_price,
                "exit_date": exit_date,
                "exit_price": exit_price,
                "pnl": pnl,
                "return_trade": pnl / entry_price,
                "duration": duration,
                "direction": "long" if position > 0 else "short"
            }) # Ajouter le trade à la liste des trades

            # Réinitialiser la position et les variables d'entrée
            position = 0
            entry_price = None
            entry_date = None

    return pd.DataFrame(trades) # Retourner les trades sous forme de DataFrame pandas





