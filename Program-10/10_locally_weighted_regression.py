import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.nonparametric.smoothers_lowess import lowess

data = pd.read_csv("house_price.csv")
X = data["Area"]
Y = data["Price"]

result = lowess(endog=Y, exog=X, frac=0.3)

plt.scatter(X, Y, label="Original Data")
plt.plot(result[:, 0], result[:, 1], linewidth=3, label="Locally Weighted Regression")
plt.title("House Price Prediction using LWR")
plt.xlabel("Area (Square Feet)")
plt.ylabel("Price (Lakhs)")
plt.legend()
plt.grid(True)
plt.show()
