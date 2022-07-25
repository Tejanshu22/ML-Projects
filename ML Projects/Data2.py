import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model


df = pd.read_csv("Data2.csv")
median_bedroom = math.floor(df.bedroom.median())
df = df.bedroom.fillna(median_bedroom)
print(df)

reg = linear_model.LinearRegression()
reg.fit(df[['area', 'bedroom', 'age']], df.price)

print(reg.predict([[3000, 3, 40]]))
