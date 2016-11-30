import matplotlib.pyplot as plt
from scipy.constants import nano, k
import numpy as np
from math import sqrt

from mpl_toolkits.mplot3d import Axes3D

arquivo = open('dados/saida3.txt')
dados = arquivo.readlines()
r1 = []
r2 = []

titles = ['Z=1', 'Z=-1']

for linha in dados:
    l = linha.split(' ')
    zE = int(l[0])
    r = [float(i) for i in l[2:]]

    if zE == 1:
        r1.append(r)
    elif zE == -1:
        r2.append(r)


arquivo.close()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = [i[0] for i in r1]
y = [i[1] for i in r1]
z = [i[2] for i in r1]
ax.scatter(x, y, z, zdir='z', s=20, c='red', depthshade=True)
x = [i[0] for i in r2]
y = [i[1] for i in r2]
z = [i[2] for i in r2]
ax.scatter(x, y, z, zdir='z', s=20, c='blue', depthshade=True)
plt.show()
