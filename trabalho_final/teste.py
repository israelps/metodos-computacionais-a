from multiprocessing import Pool
import numpy as np
from scipy.constants import e,nano,pi,epsilon_0
from time import time
from numba import jit,vectorize
import os


def V(r):
    potencial = 0
    for i in range(len(r)):  # potencial entre os ions
        for k in range(i + 1, len(r)):
            potencial += pow(e, 2) / (4 * pi * (80 * epsilon_0)
                                      * np.linalg.norm(r[i] - r[k]))
    sigma = 0.0025
    for i in range(len(r)): #somatorio para o potencial da placa
        potencial +=  sigma*e*r[i][0]/(80*epsilon_0)
    return potencial

@jit
def V_novo(r):
    potencial = 0
    sigma = 0.0025
    for i in range(len(r)):  # potencial entre os ions
        potencial +=  sigma*e*r[i][0]/(80*epsilon_0)
        for k in range(i + 1, len(r)):
            potencial += pow(e, 2) / (4 * pi * (80 * epsilon_0)
                                      * np.linalg.norm(r[i] - r[k]))
    return potencial

def get_vetor_inicial(n_ions):
    return np.random.uniform(0,nano*25,size=[n_ions,3])

if __name__ == '__main__':
    r = get_vetor_inicial(1500)
    t = time()
    print(V(r))
    print('V(r) - Normal = %d segundos'%(time()-t))

    t = time()
    print(V_novo(r))
    print('V_novo(r) - Normal = %d segundos'%(time()-t))
