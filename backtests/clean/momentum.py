'''
Signal: at each month-end, rank the ETFs by their return over the past 12 months, skipping the most recent month.
Portfolio: hold the top 3, equally weighted, for the following month.
Output: a series of monthly returns, plus annualized return, volatility, Sharpe ratio, and maximum drawdown, printed as JSON.
The rule that matters: a signal computed with data through month t may only earn the return of month t+1.

Add two or three pytest tests, including one that proves the rule above on a tiny hand-made dataset.
'''

import json
import pandas as pd


# Load the price data
prices = pd.read_csv("data/prices_monthly.csv", index_col="date", parse_dates=True)

# Compute the monthly returns --> month’s price divided by last month’s minus 1
returns = prices.pct_change().dropna()

#Compute the momentum signal
