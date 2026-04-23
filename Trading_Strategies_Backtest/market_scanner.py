# market_scanner.py

from regimes import volatility_regime, trend_regime, range_regime, impulse_regime

def scan_markets(tickers, loader):
    results = []

    for ticker in tickers:
        df = loader(ticker)

        vol = volatility_regime(df)
        trend = trend_regime(df)
        rng = range_regime(df)
        imp = impulse_regime(df)

        last = df.index[-1]

        result = {
            "ticker": ticker,
            "range": rng.loc[last, "regime"] == "range",
            "trend_up_start": trend.loc[last, "regime"] == "uptrend" and trend.loc[last - 1, "regime"] == "neutral",
            "trend_down_start": trend.loc[last, "regime"] == "downtrend" and trend.loc[last - 1, "regime"] == "neutral",
            "impulse_up": imp.loc[last, "regime"] == "impulse_up",
            "impulse_down": imp.loc[last, "regime"] == "impulse_down",
            "low_vol": vol.loc[last, "regime"] == "low_vol",
            "high_vol": vol.loc[last, "regime"] == "high_vol"
        }

        results.append(result)

    return results


from regimes import volatility_regime, trend_regime, range_regime, impulse_regime

def analyze_single_market(df):

    # 1. Calcul des régimes
    vol = volatility_regime(df)
    trend = trend_regime(df)
    rng = range_regime(df)
    imp = impulse_regime(df)

    last = df.index[-1]
    prev = df.index[-2]

    # 2. États actuels
    vol_state = vol.loc[last, "regime"]
    trend_state = trend.loc[last, "regime"]
    trend_prev = trend.loc[prev, "regime"]
    range_state = rng.loc[last, "regime"]
    impulse_state = imp.loc[last, "regime"]

    # 3. Détections
    is_range = (range_state == "range")
    is_low_vol = (vol_state == "low_vol")
    is_high_vol = (vol_state == "high_vol")

    trend_up_start = (trend_prev == "neutral" and trend_state == "uptrend")
    trend_down_start = (trend_prev == "neutral" and trend_state == "downtrend")

    impulse_up = (impulse_state == "impulse_up")
    impulse_down = (impulse_state == "impulse_down")

    # 4. Résumé intelligent
    if impulse_up:
        summary = "marché explosif haussier"
    elif impulse_down:
        summary = "marché explosif baissier"
    elif trend_up_start:
        summary = "début de tendance haussière"
    elif trend_down_start:
        summary = "début de tendance baissière"
    elif is_range and is_low_vol:
        summary = "marché calme en range"
    elif is_range:
        summary = "marché en range"
    elif trend_state == "uptrend":
        summary = "tendance haussière"
    elif trend_state == "downtrend":
        summary = "tendance baissière"
    else:
        summary = "marché neutre"

    # 5. Retour
    return {
        "volatility": vol_state,
        "trend": trend_state,
        "range": range_state,
        "impulse": impulse_state,
        "trend_up_start": trend_up_start,
        "trend_down_start": trend_down_start,
        "impulse_up": impulse_up,
        "impulse_down": impulse_down,
        "low_vol": is_low_vol,
        "high_vol": is_high_vol,
        "summary": summary
    }
