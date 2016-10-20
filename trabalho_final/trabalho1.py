from random import random
from math import pow, sqrt, exp
from scipy.constants import k, e, epsilon_0, pi, nano, milli
import numpy as np
from numba import jit

@jit
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

@jit #gera um vetor inicial aleatorio [n_ions,3] onde 3 são as coordenadas espaciais x,y,z
def get_vetor_inicial(n_ions):
    return np.random.uniform(0,25*nano,size=[n_ions,3])

@jit #função para gerar um vetor aleatorio com norma <=1 para garantir continuidade da distribuição
def get_random(r,n,step):
    dx = step*np.random.uniform(-1, 1, size=[n,3])
    r_ = r+dx
    if np.linalg.norm(x)<1:
        for ion in range(len(r_)):
            if r_[ion][0]<0:
                r_[ion][0]=-r_[ion][0]

            if r_[ion][0]>25:
                r_[ion][0]=50*nano-r_[ion][0]

            if r_[ion][1]<=0:
                r_[ion][1] +=25*nano

            if r_[ion][1]>=25*nano:
                r_[ion][1]-=25*nano

            if r_[ion][2]<=0:
                r_[ion][2] +=25*nano

            if r_[ion][2]>=25*nano:
                r_[ion][2]-=25*nano
        return r_
    else: get_random(r,n,step)



aceito,boltz,rejeitado = 0,0,0
n_ions = 150
r = get_vetor_inicial(n_ions)
T = 300
N = 1500
step = nano
x=np.zeros((1,3))

'''
print('Inicio Simulated Anealing')
v = V(r) #potencial inicial

for _ in range(50):
    rej = 0
    for _ in range(50):
        r_ = get_random(r,n_ions,step)
        v_ = V(r_)
        delta_v = v_ - v
        if (delta_v) < 0:
            r = r_
            v=v_
        elif (random() < exp(-delta_v / (k * T))):
            r = r_
            v=v_
        else:
            rej+=1
    rej = rej*10/5
    if rej <40:
        step = step*0.9
    if rej >55:
        step = step*0.1

print('Fim simulated Anealing')
print('Step calibrado em: ',step)
'''
print('Iniciando algoritimo...')


r = get_vetor_inicial(n_ions)
v = V(r) #potencial inicial

#algoritimo de metrópolis
for i in range(N):
    r_ = get_random(r,n_ions,step)
    v_ = V(r_)
    delta_v = v_ - v
    if (delta_v) < 0:
        r = r_
        v=v_
        aceito+=1
    elif (random() < exp(-delta_v / (k * T))):
        r = r_
        v=v_
        boltz+=1
    else:
        rejeitado+=1
    x=np.vstack((x,r))

a = x.tolist()

print('%d aceitos; %d aceitos por boltzman; %d rejeitados;'%(aceito,boltz,rejeitado))
rejeitado = rejeitado*100/N
print('taxa de rejeição: %d por cento'%rejeitado)
np.savetxt('dados/saida.txt',a)
