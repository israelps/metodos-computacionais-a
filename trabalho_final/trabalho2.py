from random import random
from math import pow, sqrt, exp, fmod
from scipy.constants import k, elementary_charge, epsilon_0, pi, nano, milli
import matplotlib.pyplot as plt
import numpy as np


# define o potencial eletroestatico entre as duas cargas
def V(r):
    Q = 10 * elementary_charge
    q = elementary_charge
    return Q * q / (4 * pi * epsilon_0 * np.linalg.norm(r))

# função para gerar um vetor aleatorio com norma <=1 para garantir
# continuidade da distribuição
def get_random():
    x = np.random.uniform(-1, 1, size=3)
    if np.linalg.norm(x) < 1:
        return x
    else:
        return np.random.uniform(-1, 1, size=3)

x, y = [], []


def metropolis(r, T):
    r_ = r + nano * get_random()
    if (np.linalg.norm(r_) >= 2.5 * milli):
        r_ = -r_
        print('colisao')
    v = V(r)
    v_ = V(r_)
    delta_v = v_ - v
    if (delta_v) < 0:
        r = r_
    elif (random() < exp(-delta_v / (k * T))):
        r = r_
    else:
        pass
    x.append(np.linalg.norm(r))
    y.append(v)


# chute inicial para r
r = nano * np.random.uniform(-1, 1, size=3)
# simullated anealling
for i in reversed(range(300, 3000)):
    metropolis(r, i)

for i in range(10000):
    metropolis(r, 300)


plt.plot(x, y, 'ro', linewidth=0.1)
plt.title('Simulação de potencial \n duas cargas em uma caixa de 50mm')
plt.xlabel('Distância (r) m')
plt.ylabel('Potencial Eletrico V(r)')
plt.show()
