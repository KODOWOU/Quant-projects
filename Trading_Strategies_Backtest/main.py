# main.py

from data_loader import load_data
from indicator_lib import atr
from strategies.ema_cross import ema_cross_strategy
from strategies.rsi_strategies import rsi_reversion_strategy, rsi_overreaction_strategy
from strategies.ichimoku import ichimoku_strategy
from backtest_py.backtest import execute_trades 
from matplotlib import pyplot as plt
from backtest_py.metrics import compute_equity_metrics, compute_trade_metrics, compute_all_metrics
from regimes import volatility_regime, trend_regime, range_regime, impulse_regime

from market_scanner import analyze_single_market, scan_markets

def main():

    print("\n=== TEST 1 : Scanner un seul marché ===")
    df = load_data("AAPL", start="2015-01-01")  # tu peux mettre end="2020-06-01"
    signal = analyze_single_market(df)

    for k, v in signal.items():
        print(f"{k}: {v}")

    print("\n=== TEST 2 : Scanner plusieurs marchés ===")
    tickers = ["AAPL", "MSFT", "TSLA", "NVDA", "BTC-USD"]

    results = scan_markets(tickers, load_data)

    for r in results:
        print(r)

    print("\n=== TEST 3 : Scan historique (backtest du scanner) ===")
    df = load_data("AAPL", start="2015-01-01")

    test_dates = ["2017-01-01", "2018-06-01", "2020-03-01"]

    for d in test_dates:
        df_cut = df[df.index <= d]
        signal = analyze_single_market(df_cut)
        print(f"\nDate : {d}")
        print(signal)

if __name__ == "__main__":
    main()
