import polars as pl
import matplotlib.pyplot as plt

def describe_with_polars(filename):
    """Function which returns descriptive stats about input data using Polars."""
    df = pl.read_csv(filename)
    return df.describe()

results = describe_with_polars("nba.csv")

print(results)

nba = pl.read_csv("nba.csv")
plt.figure(figsize=(10, 8))
plt.scatter(nba["Age"], nba["Weight"])
plt.title("NBA player Weight vs Age")
plt.xlabel("Age")
plt.ylabel("Weight")
plt.show(block=True)
