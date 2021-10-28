import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ucla = pd.read_csv(r"C:\Users\bryan\Desktop\Universidad\2021-2\Python\Scripts_UCLA\ProyectoFinal\ucla.csv", sep=",")

cantidad = ucla[["grupo","ano"]]
cantidad2 = cantidad.groupby(["grupo"]).count()
cantidad2.ano.astype(float)

cantidad = ucla[["grupo","ano"]]
cantidad3 = cantidad.groupby(["ano"]).count()
#1
plt.stem(cantidad3.index, cantidad3["grupo"])
#2
plt.plot(cantidad3.index, cantidad3["grupo"])
#3
plt.pie(cantidad2.ano, labels=cantidad2.index)
#4
plt.scatter(cantidad3.index, cantidad3["grupo"], c="red")
#5
plt.boxplot(cantidad3["grupo"])
#6
plt.bar(cantidad3.index, cantidad3["grupo"])
#7
plt.barh(cantidad2.index, cantidad2.ano)
#8
plt.step(cantidad3.index, cantidad3["grupo"])
#9
plt.hist(cantidad3["grupo"], edgecolor="red")
#10
fig, ax= plt.subplots(3)
fig.suptitle=('datos UCLA')
ax[0].plot(cantidad3.index, cantidad3["grupo"])
ax[1].barh(cantidad2.index, cantidad2.ano)
ax[2].scatter(cantidad3.index, cantidad3["grupo"], c="red")
plt.figure(figsize=(8,6))
fig, ax= plt.subplots(3)
fig.suptitle=('datos UCLA')
ax[0].plot(cantidad3.index, cantidad3["grupo"])
ax[1].barh(cantidad2.index, cantidad2.ano)
ax[2].scatter(cantidad3.index, cantidad3["grupo"], c="red")
plt.show()
#11
