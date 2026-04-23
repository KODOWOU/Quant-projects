# strategies.ichimoku.py

from indicator_lib import ichimoku
import pandas as pd

def ichimoku_strategy(df: pd.DataFrame) -> pd.Series:
    """
    Stratégie Ichimoku avec logique d'état persistante :
    - Entrée long : prix > Kumo, Tenkan > Kijun, Chikou > prix
    - Sortie long : Tenkan < Kijun ou prix < Kumo
    - Entrée short : prix < Kumo, Tenkan < Kijun, Chikou < prix
    - Sortie short : Tenkan > Kijun ou prix > Kumo
    """

    tenkan, kijun, senkou_a, senkou_b, chikou = ichimoku(df)
    close = df["Close"]

    signal = pd.Series(0, index=df.index)
    current_position = 0

    for i in range(52, len(df)):  # Ichimoku nécessite un historique long

        price = close.iloc[i]
        span_a = senkou_a.iloc[i]
        span_b = senkou_b.iloc[i]
        chikou_val = chikou.iloc[i]

        # Détermination du Kumo
        kumo_high = max(span_a, span_b)
        kumo_low = min(span_a, span_b)

        # ============================
        # SORTIES (prioritaires)
        # ============================

        # Sortie long
        if current_position == 1:
            if tenkan.iloc[i] < kijun.iloc[i] or price < kumo_low:
                current_position = 0

        # Sortie short
        elif current_position == -1:
            if tenkan.iloc[i] > kijun.iloc[i] or price > kumo_high:
                current_position = 0

        # ============================
        # ENTRÉES (si flat)
        # ============================

        if current_position == 0:

            # Entrée long
            if (
                price > kumo_high and
                tenkan.iloc[i] > kijun.iloc[i] and
                chikou_val > close.iloc[i - 26]
            ):
                current_position = 1

            # Entrée short
            elif (
                price < kumo_low and
                tenkan.iloc[i] < kijun.iloc[i] and
                chikou_val < close.iloc[i - 26]
            ):
                current_position = -1

        signal.iloc[i] = current_position

    return signal.rename("signal")
