# strategies.rsi_reversion.py

from indicator_lib import rsi, atr
import pandas as pd

# ============================================================
#   RSI MEAN-REVERSION STRATEGY
# ============================================================

def rsi_reversion_strategy(
    df: pd.DataFrame,
    rsi_period: int = 14,
    oversold: float = 30,
    overbought: float = 70,
    neutral: float = 50,
    atr_period: int = 14,
    atr_multiplier: float = 2.0
) -> pd.Series:

    rsi_values = rsi(df["Close"], rsi_period)
    atr_values = atr(df["High"], df["Low"], df["Close"], atr_period)

    signal = pd.Series(0, index=df.index)

    current_position = 0
    entry_price = None

    for i in range(1, len(df)):

        # SORTIE PAR SIGNAL INVERSE
        # On sort de la position longue si le RSI redescend en dessous du niveau neutre (50) après avoir été en surachat.
        if current_position == 1 and rsi_values.iloc[i] < neutral:
            current_position = 0
            entry_price = None
            # On sort de la position longue si le RSI redescend en dessous du niveau neutre (50) après avoir été en surachat.
        # On sort de la position courte si le RSI remonte au-dessus du niveau neutre (50) après avoir été en survente.
        elif current_position == -1 and rsi_values.iloc[i] > neutral:
            current_position = 0
            entry_price = None

        # STOP-LOSS ATR
        elif current_position == 1 and entry_price is not None:
            if df["Close"].iloc[i] < entry_price - atr_multiplier * atr_values.iloc[i]:
                current_position = 0
                entry_price = None

        elif current_position == -1 and entry_price is not None:
            if df["Close"].iloc[i] > entry_price + atr_multiplier * atr_values.iloc[i]:
                current_position = 0
                entry_price = None

        # ENTRÉE (uniquement si flat)
        if current_position == 0:

            if rsi_values.iloc[i] < oversold:
                current_position = 1
                entry_price = df["Close"].iloc[i]

            elif rsi_values.iloc[i] > overbought:
                current_position = -1
                entry_price = df["Close"].iloc[i]

        signal.iloc[i] = current_position

    return signal.rename("signal")


# ============================================================
#   RSI OVERREACTION STRATEGY (CONTRARIAN)
# ============================================================

def rsi_overreaction_strategy(
    df: pd.DataFrame,
    rsi_period: int = 14,
    oversold: float = 30,
    overbought: float = 70,
    neutral: float = 50,
    atr_period: int = 14,
    atr_multiplier: float = 2.0
) -> pd.Series:
    """
    Stratégie RSI Overreaction (contrarian):
    - Achat quand RSI > overbought (surachat)
    - Vente quand RSI < oversold (survente)
    """

    rsi_values = rsi(df["Close"], rsi_period)
    atr_values = atr(df["High"], df["Low"], df["Close"], atr_period)

    signal = pd.Series(0, index=df.index)

    current_position = 0
    entry_price = None

    for i in range(1, len(df)):

        # SORTIE PAR SIGNAL INVERSE
        # On sort de la position longue si le RSI redescend en dessous du niveau neutre (50) après avoir été en surachat.
        if current_position == 1 and rsi_values.iloc[i] < neutral:
            current_position = 0
            entry_price = None

        # On sort de la position courte si le RSI remonte au-dessus du niveau neutre (50) après avoir été en survente.
        elif current_position == -1 and rsi_values.iloc[i] > neutral:
            current_position = 0
            entry_price = None

        # STOP-LOSS ATR
        elif current_position == 1 and entry_price is not None:
            if df["Close"].iloc[i] < entry_price - atr_multiplier * atr_values.iloc[i]:
                current_position = 0
                entry_price = None

        elif current_position == -1 and entry_price is not None:
            if df["Close"].iloc[i] > entry_price + atr_multiplier * atr_values.iloc[i]:
                current_position = 0
                entry_price = None

        # ENTRÉE (uniquement si flat)
        if current_position == 0:

            if rsi_values.iloc[i] > overbought:
                current_position = 1
                entry_price = df["Close"].iloc[i]

            elif rsi_values.iloc[i] < oversold:
                current_position = -1
                entry_price = df["Close"].iloc[i]

        signal.iloc[i] = current_position

    return signal.rename("signal")
