'''o algoritimo foi escrito em python3, o arquivo de
entrada deve estar na mesma pasta que o arquivo legendre.py'''
from math import fabs

# cabeçalho
print('-----------------------------------------------------------')
print('-------------  Aluno: Israel P. Siqueira  -----------------')
print('-----------------Matricula: 14/0144587  -------------------')
print('-----------------------------------------------------------')
print('---------  Tarefa 02 - Polinomios de Legendre  ------------')
print('-----------------------------------------------------------')
print('')

'''Função que recebe dois valores n e x,
 onde n e um inteiro e x deve estar entre -1 e 1
 e calcula o polinomio de legendre'''
def P(n, x):
    pn_ant, pn = 1, x  # pn_ant = pn(n-1) e pn = p(n)
    result = 0  # resultado do somatorio
    if n == 0: return pn_ant  # se n for 0 retorna 1
    if n == 1: return pn  # se n for 1 retorna x
    # loop para calcular o somatório da função
    for i in range(1, n):
        result = ((2 * i + 1) * x * pn - i * pn_ant) / (i + 1)
        pn_ant = pn  # salva o novo valor de p(n-1)
        pn = result  # salva o novo valor de p(n)
    return result

# abre o arquivo de entrada e salva os valores de x em um vetor
arquivo = open('input_02.txt')

for linha in arquivo:  # loop para percorrer as linhas do arquivo de entrada
    x = float(linha)
    print('Pn(%.2f)' % x)
    for i in range(2, 6):  # loop interno para calcular p2-p5 do valor de x lido
        if (fabs(x) > 1):  # verifica se o modulo do valor e entrada é valido
            print('valor de x fora do intervalo de convergencia do Polinomio')
            break
        print('P%d(%.2f) = %.4f' % (i, x, P(i, x)))  # saida formatada
    print('')
arquivo.close()
