
from math import pow, sqrt, exp
from scipy.constants import k, e, epsilon_0, pi, nano, milli
import numpy as np
from numba import jit, guvectorize
from montecarlo import Metropolis



def V(r,Z):
    potencial = 0
    sigma = 0.0025
    for i in range(len(r)):  # potencial da placa
        potencial += sigma * Z[i]*e * r[i][0] / (80 * epsilon_0)
        for k in range(i + 1, len(r)):# potencial entre os ions
            potencial += Z[i]*Z[k]*pow(e, 2) / (4 * pi * (80 * epsilon_0)
                                      * np.linalg.norm(r[i] - r[k]))
    return potencial


# gera um vetor inicial aleatorio [n_ions,3] onde 3 são as coordenadas
# espaciais x,y,z
@jit
def get_vetor_inicial(n_ions):
    return np.random.uniform(0, 25 * nano, size=[n_ions, 3])

def c_contorno(r):
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

# vetor = [Z,raio,n_ions]
def get_concentracao(vetor):
    n = len(vetor)
    Z = [vetor[i][0]*vetor[i][2] for i in range(n)]
    return Z


print('Iniciando algoritimo...')
if __name__ == '__main__':
    Z = [[1,0,50],[2,0,50]]
    Z = get_concentracao(Z)
    n_ions = len(Z)
    r = get_vetor_inicial(n_ions)
    T = 300
    N = 2000
    step = nano

    m = Metropolis(V,Z,c_contorno,N,r,step,T)

    m.run()
