# indicator_lib.py

import pandas as pd
import numpy as np
import talib as ta


# ============================================================
#   MOVING AVERAGES
# ============================================================

def sma(series: pd.Series, period: int):
    return ta.SMA(series, timeperiod=period)

def ema(series: pd.Series, period: int):
    return ta.EMA(series, timeperiod=period)

def wma(series: pd.Series, period: int):
    return ta.WMA(series, timeperiod=period)

def hma(series: pd.Series, period: int):
    # Hull MA = WMA(2*WMA(n/2) - WMA(n)), sqrt(n)
    half = int(period / 2)
    sqrt_n = int(np.sqrt(period))
    wma_half = ta.WMA(series, timeperiod=half)
    wma_full = ta.WMA(series, timeperiod=period)
    hull_raw = 2 * wma_half - wma_full
    return ta.WMA(hull_raw, timeperiod=sqrt_n)


# ============================================================
#   MOMENTUM INDICATORS
# ============================================================

def rsi(series: pd.Series, period: int = 14):
    return ta.RSI(series, timeperiod=period)

def macd(series: pd.Series, fast=12, slow=26, signal=9):
    macd_line, signal_line, hist = ta.MACD(series, fastperiod=fast, slowperiod=slow, signalperiod=signal)
    return macd_line, signal_line, hist

def stoch(high, low, close, k=14, d=3):
    k_val, d_val = ta.STOCH(high, low, close, fastk_period=k, slowk_period=d, slowd_period=d)
    return k_val, d_val


# ============================================================
#   VOLATILITY INDICATORS
# ============================================================

def atr(high, low, close, period=14):
    return ta.ATR(high, low, close, timeperiod=period)

def true_range(high, low, close):
    return ta.TRANGE(high, low, close)


# ============================================================
#   TREND INDICATORS
# ============================================================

def adx(high, low, close, period=14):
    return ta.ADX(high, low, close, timeperiod=period)

def cci(high, low, close, period=20):
    return ta.CCI(high, low, close, timeperiod=period)


# ============================================================
#   VOLUME INDICATORS
# ============================================================

def obv(close, volume):
    return ta.OBV(close, volume)

def ad_volume(high, low, close, volume):
    return ta.AD(high, low, close, volume)


# ============================================================
#   PRICE-BASED INDICATORS
# ============================================================

def bollinger_bands(series: pd.Series, period=20, std=2):
    upper, middle, lower = ta.BBANDS(series, timeperiod=period, nbdevup=std, nbdevdn=std)
    return upper, middle, lower

def ichimoku(df, conv=9, base=26, span_b=52):
    high = df["High"]
    low = df["Low"]

    conversion = (high.rolling(conv).max() + low.rolling(conv).min()) / 2
    baseline = (high.rolling(base).max() + low.rolling(base).min()) / 2
    span_a = ((conversion + baseline) / 2).shift(base)
    span_b = ((high.rolling(span_b).max() + low.rolling(span_b).min()) / 2).shift(base)
    lagging = df["Close"].shift(-base)

    return conversion, baseline, span_a, span_b, lagging


# ============================================================
#   VWAP
# ============================================================

def vwap(df):
    typical_price = (df["High"] + df["Low"] + df["Close"]) / 3
    cumulative_vp = (typical_price * df["Volume"]).cumsum()
    cumulative_vol = df["Volume"].cumsum()
    return cumulative_vp / cumulative_vol
