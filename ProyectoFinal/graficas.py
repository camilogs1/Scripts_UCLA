from mpl_toolkits.mplot3d import axes3d
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#llamado datos
ucla = pd.read_csv("https://raw.githubusercontent.com/camilogs1/Scripts_UCLA/main/ProyectoFinal/ucla.csv", sep=",")

#organizar datos
cantidad = ucla[["grupo","ano"]]
cantidad2 = cantidad.groupby(["grupo"]).count()
cantidad2.ano.astype(float)
cantidad = ucla[["grupo","ano"]]
cantidad3 = cantidad.groupby(["ano"]).count()
cantidad4 = ucla[["grupo", "ano", "vol"]]

#punto 1
plt.stem(cantidad3.index, cantidad3["grupo"])
#punto 2
plt.plot(cantidad3.index, cantidad3["grupo"])
#punto 3
plt.pie(cantidad2.ano, labels=cantidad2.index)
#punto 4
plt.scatter(cantidad3.index, cantidad3["grupo"], c="red")
#punto 5
plt.boxplot(cantidad3["grupo"])
#punto 6
plt.bar(cantidad3.index, cantidad3["grupo"])
#punto 7
plt.barh(cantidad2.index, cantidad2.ano)
#punto 8
plt.step(cantidad3.index, cantidad3["grupo"])
#punto 9
plt.hist(cantidad3["grupo"], edgecolor="red")
#punto 10
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
#punto 11
fig = plt.bar(cantidad3.index, cantidad3["grupo"])
fig = plt.title("Grafica grupos UCLA")
fig = plt.xlabel('año')
fig = plt.ylabel('articulos')
fig = plt.grid(True)
fig = plt.legend(['Articulos por año'])
fig = plt.figure(figsize=(8,6))
#punto 12 con datos aleatorios ya que no poseemos con los datos necesarios para darle forma a la grafica
x=np.random.randint(10, size=60)
y=np.random.randint(10, size=60)
z=np.random.randint(10, size=60)
axes = plt.axes(projection="3d")
axes.scatter3D(x,y,z,color="blue")
axes.set_title("Grafica en 3d")
#punto 13
