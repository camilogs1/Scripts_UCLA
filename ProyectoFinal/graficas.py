from mpl_toolkits.mplot3d import axes3d
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import cv2

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
#punto 12 
z=np.random.randint(10, size=25)
axes = plt.axes(projection="3d")
axes.scatter3D(cantidad3.index, cantidad3["grupo"],z,color="blue")
axes.set_title("Grafica en 3d")
#punto 13
img2=cv2.imread(r'E:\Cg\Programas\Git\Scripts_UCLA\ProyectoFinal\ucla.png')
plt.figure("UCLA")
plt.title("Universidad Católica Luis Amigó")
plt.imshow(img2)

p = cv2.cvtColor(img2,2)
plt.imshow(p)

e = cv2.cvtColor(img2,cv2.COLOR_RGB2LUV)
plt.imshow(e)

w = cv2.cvtColor(img2,cv2.COLOR_RGB2HSV)
plt.imshow(w)

q = cv2.cvtColor(img2,cv2.COLOR_RGB2GRAY)
plt.imshow(q)
#collage
fig, ax= plt.subplots(2,2)
fig.suptitle=('UCLA')
ax[0,0].imshow(p)
ax[0,1].imshow(e)
ax[1,0].imshow(w)
ax[1,1].imshow(q)

