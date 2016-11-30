import matplotlib.pyplot as plt
from scipy.constants import nano, k
import numpy as np
from math import sqrt

from mpl_toolkits.mplot3d import Axes3D


arquivo = open('dados/saida3.txt')
dados = arquivo.readlines()
arquivo.close()
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


plt.hist([i[0] for i in r1], 50, normed=1, facecolor='green', alpha=0.75)
plt.hist([i[0] for i in r2], 50, normed=1, facecolor='blue', alpha=0.75)


plt.title('Concentração de Ions em uma solução aquosa em contato\n com uma superficie de Ferrita de cobalto (CoFe2O4)')
plt.ylabel('Concentração de Ions')
plt.xlabel('Distância do eixo X')
plt.grid(True)
print(len(dados))
plt.show()
