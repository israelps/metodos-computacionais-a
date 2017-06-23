'''Escrito em python3'''
from math import sqrt,pi,pow,exp

# atualizado via git
# atualizado no servidor
# cabecalho
print('-----------------------------------------------------------')
print('-------------  Aluno: Israel P. Siqueira  -----------------')
print('-----------------Matricula: 14/0144587  -------------------')
print('-----------------------------------------------------------')
print('--------------  Tarefa 03 - Funcao Gamma ------------------')
print('-----------------------------------------------------------')
print('')

#funcao que recebe (x+1) e calcula a funcao gama naquele ponto
def gama(x):
    return sqrt(2*pi*x)*pow(x,x)*exp(-x)*(
        1+1/(12*x)+1/(288*x**2)-139/(51840*x**3))

#arquivo de entrada
f = open('input.txt')

#loop que percorre o arquivo de entrada e calcula a funcao no ponto
for linha in f:
    x = float(linha)
    print('Gamma(%.2f) = %.4f'%(x,gama(x)))
