
from math import pow, sqrt, exp
from scipy.constants import k, e, epsilon_0, pi, nano, milli, Avogadro
import numpy as np
from numba import jit, guvectorize
from montecarlo import Metropolis


@jit
def V(r, Z):
    potencial = 0
    sigma = 0.0621
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
    r = np.random.uniform(0, 5 * nano, size=[len(Z), 3])
    return r, Z


@jit
def c_contorno(r, Z):
    l_caixa = 5 * nano
    flag = False
    for i in range(len(r)):
        if r[i][0] < 0:
            r[i][0] = -r[i][0]

        if r[i][0] > l_caixa:
            r[i][0] = 2 * l_caixa - r[i][0]

        if r[i][1] <= 0:
            r[i][1] += l_caixa

        if r[i][1] >= l_caixa:
            r[i][1] -= l_caixa

        if r[i][2] <= 0:
            r[i][2] += l_caixa

        if r[i][2] >= l_caixa:
            r[i][2] -= l_caixa
            
        for k in range(i + 1, len(r)):
            diff_r = r[i] - r[k]
            norm_r = np.linalg.norm(diff_r)
            if norm_r <= (Z[i][1] + Z[k][1]):
                flag = True
                break
    return r, flag


print('Iniciando algoritimo...')
if __name__ == '__main__':

    Z = [[1, 0.095 * nano, 20], [-1, 0.095 * nano, 20]]

    r, Z = get_vetor_inicial(Z)

    T = 280
    N = 5000
    step = 5 * pow(10, -10)

    m = Metropolis(V, Z, c_contorno, N, r, step, T)

    m.run()
