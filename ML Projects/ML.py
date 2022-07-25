import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv("MAL.csv")
print(df)

reg = linear_model.LinearRegression()
reg.fit(df[['area']], df.price)

print("Predicted price of 3300 sq ft is ")
print(reg.predict([[3300]]))

plt.xlabel('area(sq ft)')
plt.ylabel('price(US$)')
plt.scatter(df.area, df.price, color='red', marker='+')
plt.plot(df.area, reg.predict(df[['area']]), color='blue')
plt.show()
