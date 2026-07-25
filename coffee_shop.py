import numpy as np
import pandas as pd
coffee = np.array(["Espresso", "Latte", "Cappuccino", "Mocha", "Cold Coffee"])

cups_sold = np.array([120, 95, 150, 80, 110])

price = np.array([120, 180, 160, 200, 150])
df = pd.DataFrame({
    "Coffee": coffee,
    "Cups Sold": cups_sold,
    "Price": price
})
print(df)
df["Revenue"] = df["Cups Sold"] * df["Price"]
print(df)
print("Average Coffee Price: ₹", np.mean(price))
highest_price = df[df["Price"] == df["Price"].max()]

print(highest_price)
best_seller = df[df["Cups Sold"] == df["Cups Sold"].max()]

print(best_seller)
print("Total Revenue: ₹", df["Revenue"].sum())
print("\n========== COFFEE SHOP SALES REPORT ==========")

print(df)

print("\nMost Sold Coffee")
print(best_seller)

print("\nMost Expensive Coffee")
print(highest_price)

print("\nAverage Coffee Price: ₹", np.mean(price))

print("Total Revenue: ₹", df["Revenue"].sum())