# src/sensitivity.py

import numpy as np
import pandas as pd


def sensitivity_analysis(returns, base_weights, shock=0.05):
    """
    Analyze sensitivity of portfolio to weight changes
    """

    results = []

    for i in range(len(base_weights)):
        w_up = base_weights.copy()
        w_down = base_weights.copy()

        w_up[i] += shock
        w_down[i] -= shock

        # Normalize
        w_up /= w_up.sum()
        w_down /= w_down.sum()

        ret_up = (returns @ w_up).mean() * 12
        ret_down = (returns @ w_down).mean() * 12

        results.append({
            "Asset": i,
            "Return_up": ret_up,
            "Return_down": ret_down
        })

    return pd.DataFrame(results)
