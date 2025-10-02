# VolatilityBreakoutStrategy.py
import pandas as pd
from Strategy import Strategy

class VolatilityBreakoutStrategy(Strategy):
    def __init__(self, shares_per_ticker=1):
        super().__init__(shares_per_ticker)

    def generate_signals(self, prices: pd.DataFrame):
        sig = self.empty_signals(prices)
        returns = prices.pct_change()
        vol = returns.rolling(20).std()
        cond = returns > vol  # buy if today's return > rolling volatility
        sig[cond] = 1
        return sig
