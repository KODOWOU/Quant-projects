# regimes.py

import pandas as pd
import numpy as np

import pandas as pd
import numpy as np

def volatility_regime(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    """
    Détecte les régimes de volatilité et retourne un DataFrame complet :
    - hv : volatilité réalisée annualisée
    - low_threshold : seuil 30%
    - high_threshold : seuil 70%
    - regime : low_vol / normal / high_vol
    """

    close = df["Close"]

    # 1. Returns log
    log_returns = np.log(close / close.shift(1))

    # 2. Volatilité annualisée
    hv = log_returns.rolling(window).std() * np.sqrt(252)

    # 3. Seuils globaux
    low_th = hv.quantile(0.30)
    high_th = hv.quantile(0.70)

    # 4. Classification
    regime = pd.Series("normal", index=df.index)
    regime[hv < low_th] = "low_vol"
    regime[hv > high_th] = "high_vol"

    # 5. Construction du DataFrame final
    out = pd.DataFrame({
        "hv": hv,
        "low_threshold": low_th,
        "high_threshold": high_th,
        "regime": regime
    })

    return out

def trend_regime(df: pd.DataFrame, ma_period: int = 100, slope_window: int = 3) -> pd.DataFrame:
    """
    Détecter les régimes de tendance:
    -uptrend: pente de la MA positive et significative 
    -downtrend: pente négative et singificative
    -neutral  pente faible (range)

    Retourne un DataFrame: 
    -ma: moyenne mobile 
    -slope: pente de la MA
    -slope_threshold: seuil de tendance
    - regime : uptrend / neutral / downtrend
    """
    close = df["Close"]

    # 1. Moyenne mobile
    ma = close.rolling(ma_period).mean()

    # Pente de la MA (variation sur slope_wingdow jours)
    slope = ma.diff(slope_window)

    # Seuil basé sur la volatilité de la pente
    slope_threshold = slope.abs().quantile(0.20)

    # Classification 
    regime = pd.Series("neutral", index = df.index)
    regime[slope > slope_threshold] = "uptrend"
    regime[slope < -slope_threshold] = "downtrend"

    # Dataframe final
    out = pd.DataFrame({
        "ma": ma,
        "slope": slope,
        "slope_treshold" : slope_threshold,
        "regime": regime
    })

    return out


def range_regime(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    """
    Détecte les marchés en range à partir :
    - Bollinger Bandwidth
    - ATR ratio (ATR / Close)

    Retourne un DataFrame :
    - bandwidth
    - atr_ratio
    - bandwidth_threshold
    - atr_threshold
    - regime : range / not_range
    """

    close = df["Close"]
    high = df["High"]
    low = df["Low"]

    # 1. Bollinger Bandwidth
    ma = close.rolling(window).mean()
    std = close.rolling(window).std()
    bandwidth = std / ma

    # 2. ATR
    tr1 = high - low
    tr2 = (high - close.shift(1)).abs()
    tr3 = (low - close.shift(1)).abs()
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    atr = tr.rolling(window).mean()

    atr_ratio = atr / close

    # 3. Seuils
    bandwidth_threshold = bandwidth.quantile(0.30)
    atr_threshold = atr_ratio.quantile(0.30)

    # 4. Classification
    regime = pd.Series("not_range", index=df.index)
    regime[(bandwidth < bandwidth_threshold) & (atr_ratio < atr_threshold)] = "range"

    # 5. DataFrame final
    out = pd.DataFrame({
        "bandwidth": bandwidth,
        "atr_ratio": atr_ratio,
        "bandwidth_threshold": bandwidth_threshold,
        "atr_threshold": atr_threshold,
        "regime": regime
    })

    return out

def impulse_regime(df: pd.DataFrame, roc_period: int = 5, breakout_period: int = 20, volume_window: int = 20) -> pd.DataFrame:
    """
    Détecte les régimes d'impulsion :
    - impulse_up : explosion haussière
    - impulse_down : explosion baissière
    - normal : pas d'impulsion

    Basé sur :
    - ROC (Rate of Change)
    - Breakout de prix
    - Volume spike
    """

    close = df["Close"]
    high = df["High"]
    low = df["Low"]
    volume = df["Volume"]

    # 1. ROC
    roc = close.pct_change(roc_period)

    # 2. Breakouts
    highest = high.rolling(breakout_period).max()
    lowest = low.rolling(breakout_period).min()

    breakout_up = close > highest.shift(1)
    breakout_down = close < lowest.shift(1)

    # 3. Volume spike
    vol_ma = volume.rolling(volume_window).mean()
    volume_ratio = volume / vol_ma

    # 4. Seuil ROC dynamique
    roc_threshold = roc.abs().quantile(0.70)

    # 5. Classification
    regime = pd.Series("normal", index=df.index)

    regime[(roc > roc_threshold) & breakout_up & (volume_ratio > 1.2)] = "impulse_up"
    regime[(roc < -roc_threshold) & breakout_down & (volume_ratio > 1.2)] = "impulse_down"

    # 6. DataFrame final
    out = pd.DataFrame({
        "roc": roc,
        "roc_threshold": roc_threshold,
        "breakout_up": breakout_up,
        "breakout_down": breakout_down,
        "volume_ratio": volume_ratio,
        "regime": regime
    })

    return out
