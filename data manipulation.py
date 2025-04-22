import pandas as pd
import matplotlib.pyplot as plt
#loading
try:
    df = pd.read_csv("100 Sales Records.csv")
except FileNotFoundError:
    print("The file does not exist")

#printing 5 values
print (df.head())

df.info()

df_cleaned = df.dropna()

print(df.describe(include="all"))

#grouping data by region and finding mean profits for each region

grouping = df.groupby("Region")["Total Profit"].mean()
print(grouping)

#creating a year column to allow me draw a line graph

df["Ship Date"] = pd.to_datetime(df["Ship Date"])
df['Year'] = df["Ship Date"].dt.year
print(df)

#Summing yearly profits

yearly_profits = df.groupby("Year")["Total Profit"].sum()
#line graph

plt.plot(yearly_profits.index, yearly_profits.values, marker="*", color="skyblue")
plt.title("Profits against shipping date")
plt.xlabel("shipping year")
plt.ylabel("Profits")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()

plt.show()

#bar chart

grouping.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Average sales for each region")
plt.xlabel("Region")
plt.ylabel("Profits")

plt.show()

#histogram
plt.hist(df["Total Profit"], bins=5, color="skyblue", edgecolor="black")
plt.title("Profit Distribution")
plt.xlabel("Total Profit")
plt.ylabel("Frequency")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()

plt.show()

#scatterplot
plt.scatter(df["Units Sold"], df["Total Profit"], color="skyblue", edgecolor="black")
plt.title("Profits vs Units Sold")
plt.xlabel("Units")
plt.ylabel("Profits")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

plt.show()