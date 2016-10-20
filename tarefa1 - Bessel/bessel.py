'''o algoritimo foi escrito em python3, o arquivo de
entrada deve estar na mesma pasta que o arquivo bessel.py
A função 'pow()' foi usada para calcular potencias
para dar maior precisão e mais legibilidade ao código'''

#cabeçalho
print('-----------------------------------------------------------')
print('-------------  Aluno: Israel P. Siqueira  -----------------')
print('-----------------Matricula: 14/0144587  -------------------')
print('-----------------------------------------------------------')
print('---------  Tarefa 01 - Função de Bessel J0(x)  ------------')
print('-----------------------------------------------------------')

# imports de funcoes básicas para deixar o código mais legivel
from math import pow, factorial

# Define a função de bessel no ponto J0(x) = ((-1)^k(x/2)^2k)/(k!)^2
def J0(x, k):
    return pow(-1, k) * pow(x / 2, 2 * k) / pow(factorial(k),2)

'''
Retorna o somatório da função de Bessel recebendo como
parametro x e k, onde k é o expoente máximo da função.
'''
def bessel(x, k):
    result = 0
    for k in range(k):
        result = result + J0(x, k)
    return result

# abre o arquivo de entrada e salva os valores de x em um vetor
arquivo = open('input.txt')
x = []  # vetor para salvar os dados do arquivo de entrada
for linha in arquivo:
    x.append(float(linha))
arquivo.close()


# loop que percorre o vetor x e calcula a funcao de bessel para cada valor de x
# resultado formatado para 6 casas significativas
for i in x:
    print("f(%.1f)" % i, ' -- ', "%.6f" % bessel(i, 10))

print('-----------------------------------------------------------------------------------')
print('O valor de k significativo para uma precisão de 6 casas decimais foi de no máximo 8,')
print('diretamente proporcional ao valor de X')
