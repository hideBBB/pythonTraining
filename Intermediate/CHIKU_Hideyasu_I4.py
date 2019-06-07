import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("coalpublic2013.xlsx")

# (a)
sum = df["Production"].sum()
mean = df["Production"].mean()
max = df["Production"].max()
min = df["Production"].min()

print("(a)\nsum = "+str(sum)+"\nmean = "+str(mean)+"\nmax = "+str(max)+"\nmin = "+str(min)+"\n")

# (b)
df_insert = pd.read_excel("coalpublic2013.xlsx")
df_insert.insert(5,"sixth_column",np.nan)
print("(b)")
print(df_insert.columns)

# (c)
df_sub = df[["MSHA ID","Labor_Hours"]].groupby("MSHA ID").sum()
print("\n(c)")
print(df_sub)

# (d)
df_find = df[df["Labor_Hours"] > 20000]
print("\n(d)")
print(df_find)

# (e)
df_sort = df.sort_values(["Production"], ascending=False).head(10)
print("\n(e)")
df_sort.plot(x=df_sort.columns[2],y=df_sort.columns[3],kind = "bar")
plt.show()

# (f)
df_compare = df.head(10)
print("\n(f)")
df_compare.plot(kind="bar",subplots=True, layout=(2, 2),figsize=(15, 10))
plt.show()
