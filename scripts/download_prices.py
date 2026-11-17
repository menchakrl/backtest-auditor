"""Download month-end adjusted closes for 10 sector ETFs for the last 15 years into data/prices_monthly.csv """

from pathlib import Path

import pandas as pd
import yfinance as yf

TICKERS = ["XLB", "XLE", "XLF", "XLI", "XLK", "XLP", "XLU", "XLV", "XLY", "IYR"]
START="2005-10-10"
OUT = Path("data/prices_monthly.csv")

#Daily bars, adjusted for dividends and splits.
daily = yf.download(TICKERS, start=START, auto_adjust=True, progress=False, threads=False)["Close"]

print(type(daily))        # pandas DataFrame
print(daily.columns)      # the column names, which is where "Close" appears
print(daily.head())       # the first five rows
print(daily.info())       # column types and missing-value counts

#Last trading day of each month. Drop the final row if the month is incomplete.
monthly = daily.resample("ME").last()
if daily.index[-1] < monthly.index[-1]:
    monthly = monthly.iloc[:-1]

monthly.index.name = "date"
OUT.parent.mkdir(exist_ok=True)
monthly.round(4).to_csv(OUT)
print(monthly.shape, monthly.index[0].date(), monthly.index[-1].date())
print("Missing values per ticker:\n", monthly.isna().sum())