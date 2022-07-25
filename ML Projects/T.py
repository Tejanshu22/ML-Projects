import pandas as pd
import math
import numpy as np
from numpy import nan
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv("titanic_data.csv")
df["deck"].fillna("A", limit=14, inplace=True)
df["deck"].fillna("B", limit=15, inplace=True)
df["deck"].fillna("S", inplace=True)
median_age = math.floor(df. age.median())
df["age"].fillna(median_age, inplace=True)
print(df)
y = df.age
x = df[["survived"]]
reg = linear_model.LinearRegression()
reg.fit(x, y)
print(reg.predict([["15"]]))
print(reg.score(x, y))
plt.xlabel('Survived')
plt.ylabel('Age')
plt.scatter(df.age, df.survived, color='red', marker='+')
plt.plot(x, reg.predict(x), color='blue')
plt.show()
