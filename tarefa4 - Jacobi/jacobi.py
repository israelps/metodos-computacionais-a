# cabeçalho
print('-----------------------------------------------------------')
print('-------------  Aluno: Israel P. Siqueira  -----------------')
print('-----------------Matricula: 14/0144587  -------------------')
print('-----------------------------------------------------------')
print('---------  Tarefa 04 - Metodo iterativo de Jacobi ---------')
print('-----------------------------------------------------------')
print('')

from math import sqrt
#função que le o arquivo e monta a matriz de coeficientes e constantes
def le_matriz(caminho):
    arquivo = open(caminho) #abre arquivo
    A,B = [],[] #inicia os vetores
    for linha in arquivo:
        linha = linha.split(' ') #separa as entradas
        linha = [float(i) for i in linha] #converte para float
        B.append(linha[-1]) #salva a ultima coluna(constantes) na matriz B
        A.append(linha[:-1]) #salva a coluna de coeficientes na matriz A
    arquivo.close() #fecha arquivo
    return A,B #retorna a matriz A e B

#função que define o método de jacobi
#recebe como argumento o vetor inicia x, a matriz de coeficientes,
#a matriz de constantes, tolerancia, e numero máximo de iteracoes
def jacobi(x,A,B,tol,maxInt):
    n = len(A) #tamanho da matriz
    for i in range(1,maxInt):
        x_ant = x[:] #copia o vetor x na variavel x_ant
        for linha in range(n): #percorre todas as linhas da matriz
            soma = 0
            for coluna in range(n):#percorre todas as colunas de uma linha
                if linha!=coluna: #requisito do algoritimo
                    soma=soma+A[linha][coluna]*x[coluna]
            x[linha] = (B[linha]-soma)/A[linha][linha]

        #calcula a norma de ||x-x_ant||
        erro = sqrt(sum([(a-b)**2 for a,b in zip(x,x_ant)]))
        n_x = sqrt(sum([a**2 for a in x])) #norma de x

        if erro/n_x<=tol: #se ||x-x_ant|| / ||x|| for menor que a tolerancia
            print('Algoritimo convergiu apos: %d iteracoes.'%i)
            break #para o algoritimo
        else: continue #continua o algoritimo
        #mensagem de erro caso o algoritimo não convirja
        print('Algoritimo não convergiu após: %d iteracoes.'%maxInt)
    return x

A,B = le_matriz('input.txt') #le a matriz do arquivo
x = [abs(1/len(A)) for i in A]#constroi um vetor coluna para o chute inicial da forma abs(1/n)
maxInt = 20 #numero maximo de iteracoes
erro_minimo = pow(10,-6) #erro tolerado

solucao = jacobi(x,A,B,erro_minimo,maxInt)#chama o algoritmo

print('Vetor solucao x(i)')
print(solucao)
print('o chute inicial foi dado na forma 1/n onde n e o tamanho da matriz')
print('com a escolha do erro em 10^-6 o algoritimo convege em 8 iteracoes')
print('a partir disso o algoritimo demora mais para convergir o que nao vale')
print('a pena pois erros de arredondamento comecam a ficar evidentes')
