from scipy.optimize import basinhopping,minimize

from math import pow, sqrt, exp
from scipy.constants import k, e, epsilon_0, pi, nano, milli
import numpy as np
from numba import jit, guvectorize
from montecarlo import Metropolis


@jit
def V(r, Z):
    potencial = 0
    sigma = 0.0025
    for i in range(len(r)):  # potencial da placa
        potencial += sigma * Z[i][0] * e * r[i][0] / (80 * epsilon_0)
        for k in range(i + 1, len(r)):  # potencial entre os ions
            potencial += Z[i][0] * Z[k][0] * pow(e, 2) / (
                4 * pi * (80 * epsilon_0) * np.linalg.norm(r[i] - r[k]))
    return potencial


# gera um vetor inicial aleatorio [n_ions,3] onde 3 são as coordenadas
# espaciais x,y,z

def get_vetor_inicial(concentracao):

    Z = []
    for i in concentracao:
        for k in range(i[2]):
            Z.append([i[0], i[1]])
    Z = np.asarray(Z)
    r = np.random.uniform(0, 25 * nano, size=[len(Z), 3])
    return r, Z


@jit
def c_contorno(r, Z):
    norma = np.linalg.norm(r, axis=1)
    for i in range(len(norma)):
        for k in range(i + 1):
            x = np.abs(norma[k] - norma[i])
            if x <= 5.2917721067e-11:
                r[i] = r[i]+nano
                r[k] = r[k]+nano

    for ion in range(len(r)):
        if r[ion][0] < 0:
            r[ion][0] = -r[ion][0]

        if r[ion][0] > 25:
            r[ion][0] = 50 * nano - r[ion][0]

        if r[ion][1] <= 0:
            r[ion][1] += 25 * nano

        if r[ion][1] >= 25 * nano:
            r[ion][1] -= 25 * nano

        if r[ion][2] <= 0:
            r[ion][2] += 25 * nano

        if r[ion][2] >= 25 * nano:
            r[ion][2] -= 25 * nano
    return r


print('Iniciando algoritimo...')
if __name__ == '__main__':
    raio = 5.2917721067e-11

    Z = [[1, raio, 50], [2, raio, 50]]

    r, Z = get_vetor_inicial(Z)
    T = 300
    ret=minimize(V,r)
    print(ret)
