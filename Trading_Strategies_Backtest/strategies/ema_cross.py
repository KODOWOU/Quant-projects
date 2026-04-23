# strategies/ema_cross.py

from indicator_lib import ema, atr
import pandas as pd

def ema_cross_strategy(df: pd.DataFrame, fast: int = 12, slow: int = 26, atr_period: int = 14, atr_multiplier: float = 2.0) -> pd.Series:
    """
    Stratégie EMA crossover avec :
    - signal persistant (on garde la position tant qu'aucun cross opposé ne survient)
    - sortie possible par signal opposé ou stop-loss basé sur ATR
    """

    ema_fast = ema(df["Close"], fast)
    ema_slow = ema(df["Close"], slow)
    atr_values = atr(df["High"], df["Low"], df["Close"], period=atr_period)

    signal = pd.Series(0, index=df.index)

    current_position = 0
    entry_price = None

    for i in range(1, len(df)):
        # --- Cross haussier ---
        # On entre en position longue si la EMA rapide croise au-dessus de la EMA lente.
        if ema_fast[i] > ema_slow[i] and ema_fast[i - 1] <= ema_slow[i - 1]:
            current_position = 1
            entry_price = df["Close"][i]

        # --- Cross baissier ---
        elif ema_fast[i] < ema_slow[i] and ema_fast[i - 1] >= ema_slow[i - 1]:
            current_position = -1
            entry_price = df["Close"][i]

        # --- Stop-loss ATR ---
        elif current_position == 1 and entry_price is not None:
            if df["Close"][i] < entry_price - atr_multiplier * atr_values[i]:
                current_position = 0
                entry_price = None

        elif current_position == -1 and entry_price is not None:
            if df["Close"][i] > entry_price + atr_multiplier * atr_values[i]:
                current_position = 0
                entry_price = None

        signal[i] = current_position

    return signal.rename("signal")

