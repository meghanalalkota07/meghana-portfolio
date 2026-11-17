import os

from fredapi import Fred
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# FRED API KEY
# Set this in your shell before running:
#   export FRED_API_KEY='your-key-here'
# Get a free key at https://fred.stlouisfed.org/docs/api/api_key.html
# ==========================================
fred = Fred(api_key=os.environ['FRED_API_KEY'])

# ==========================================
# TREASURY SERIES
# ==========================================
series = {
    "3M": "DTB3",
    "2Y": "DGS2",
    "5Y": "DGS5",
    "10Y": "DGS10",
    "30Y": "DGS30"
}

# ==========================================
# DOWNLOAD DATA
# ==========================================
data = pd.DataFrame()

for maturity, code in series.items():
    data[maturity] = fred.get_series(code)

# ==========================================
# CLEAN DATA
# ==========================================
data = data.dropna()

print(data.tail())

# ==========================================
# PLOT LATEST CURVE
# ==========================================
latest = data.iloc[-1]

maturities = [0.25, 2, 5, 10, 30]
yields = latest.values

plt.figure(figsize=(10,6))
plt.plot(maturities, yields, marker='o')

plt.title("US Treasury Yield Curve")
plt.xlabel("Maturity (Years)")
plt.ylabel("Yield (%)")

plt.grid(True)
plt.show()