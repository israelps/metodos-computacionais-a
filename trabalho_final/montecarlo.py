import numpy as np
from time import time
from random import random
from math import exp
from scipy.constants import k,nano
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
            r_, flag = self.c_contorno(r_, self.Z)
            return r_, flag

    def run(self):
        t = time()
        aceito_global, rejeitado_global = 0, 0
        v = self.V(self.r, self.Z)  # potencial inicial
        n_iter = 0
        v_min_anterior = 2000 * v

        f_energia = open('dados/saida3_energia.txt', 'wb')
        condicao = False
        N = 3000
        while True:
            v_min = v
            f = open('dados/saida3.txt', 'wb')
            aceito, rejeitado = 0, 0

            for i in range(N):
                n_iter += 1
                r_, flag = self.get_random()
                if flag:
                    rejeitado += 1
                    rejeitado_global += 1
                    continue
                v_ = self.V(r_, self.Z)

                delta_v = v_ - v

                if(i % 50 == 0):
                    var = aceito / 50
                    aceito = 0
                    rejeitado = 0
                    if(var <= 0.4):
                        self.step *= 0.95
                        print('step alterado para: %e' % (self.step))
                    if(var >= 0.6):
                        print('step alterado para: %e' % (self.step))
                        self.step *= 1.05

                if (delta_v) < 0:
                    self.r = r_
                    v = v_
                    aceito += 1
                    aceito_global += 1

                elif (random() < exp(-delta_v / (k * self.T))):
                    self.r = r_
                    v = v_
                    aceito += 1
                    aceito_global += 1
                else:
                    rejeitado += 1
                    rejeitado_global += 1

                if(v < v_min):
                    v_min = v
                np.savetxt(f_energia, [v])
                np.savetxt(f, np.hstack((self.Z, self.r)),
                           fmt='%d %e %e %e %e')

            f.close()

            if(abs((v_min - v_min_anterior) / v_min) <= 0.05):
                if condicao:
                    break
                condicao = True
                N = int(N * 2)
                print('condicao True')
            else:
                if condicao:
                    N = int(N / 2)
                condicao = False
                v_min_anterior = v_min
                print('condicao False')
        f_energia.close()

        print('%d aceitos; %d rejeitados;' %
              (aceito_global, rejeitado_global))
        rejeitado_global = rejeitado_global * 100 / n_iter
        print('taxa de rejeição: %d por cento' % rejeitado_global)
        print('tempo total de execução: %d s' % (time() - t))
