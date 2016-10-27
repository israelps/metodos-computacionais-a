import numpy as np
from time import time
from random import random
from math import exp
from scipy.constants import k
from numba import jit
import os


class Metropolis:

    def __init__(self, V, Z, c_contorno, n_iter, r, step, T):
        self.V = V
        self.Z = Z
        self.n_iter = n_iter
        self.r = r
        self.step = step
        self.T = T
        self.c_contorno = c_contorno

    @jit
    def get_random(self):
        dx = self.step * np.random.uniform(-1, 1, size=[len(self.r), 3])
        r_ = self.r + dx
        if np.linalg.norm(dx) < 1:
            r_ = self.c_contorno(r_, self.Z)
            return r_

    def run(self):
        t = time()
        aceito, boltz, rejeitado = 0, 0, 0
        v = self.V(self.r, self.Z)  # potencial inicial
        os.remove('dados/saida3.txt')

        f = open('dados/saida3.txt', 'ab')
        for i in range(self.n_iter):

            np.savetxt(f, np.hstack((self.Z, self.r)), fmt='%d %e %e %e %e')

            r_ = self.get_random()
            v_ = self.V(r_, self.Z)

            delta_v = v_ - v

            if (delta_v) < 0:
                self.r = r_
                v = v_
                aceito += 1

            elif (random() < exp(-delta_v / (k * self.T))):
                self.r = r_
                v = v_
                boltz += 1
            else:
                rejeitado += 1

        f.close()
        print('%d aceitos; %d aceitos por boltzman; %d rejeitados;' %
              (aceito, boltz, rejeitado))
        rejeitado = rejeitado * 100 / self.n_iter
        print('taxa de rejeição: %d por cento' % rejeitado)
        print('tempo total de execução: %d s' % (time() - t))
