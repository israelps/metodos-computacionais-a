# cabeçalho
print('-----------------------------------------------------------')
print('-------------  Aluno: Israel P. Siqueira  -----------------')
print('-----------------Matricula: 14/0144587  -------------------')
print('-----------------------------------------------------------')
print('------------  Tarefa 09 - Decomposição LU -----------------')
print('-----------------------------------------------------------')
print('')

from numpy import eye


# função que le o arquivo e monta a matriz de coeficientes e constantes
def le_matriz(caminho):
    arquivo = open(caminho)  # abre arquivo
    A, B = [], []  # inicia os vetores
    for linha in arquivo:
        linha = linha.split(' ')  # separa as entradas
        linha = [float(i) for i in linha]  # converte para float
        B.append(linha[-1])  # salva a ultima coluna(constantes) na matriz B
        A.append(linha[:-1])  # salva a coluna de coeficientes na matriz A
    arquivo.close()  # fecha arquivo
    return A, B  # retorna a matriz A e B


# função que faz a decomposicao LU da matriz
# recebe como argumento  a matriz de coeficientes,
# retorna as matrizes L e U
def LU(A):
    n = len(A) #tamanho da matriz nxn
    L = eye(n) #define L como uma matriz identidade (I) de tamanho NxN
    U = [[0]*n for _ in range(n)] #define a matriz U como uma matriz de zeros, NxN

    for i in range(n): #calcula a primeira linha e primeira coluna da matriz
        U[0][i] = A[0][i] / L[0][0]
        L[i][0] = A[i][0] / U[0][0]

    for i in range(1, n ):# loop para calular a matriz triangular superior
        S = A[i][i] - sum([L[i][k] * U[k][i] for k in range(n - 1)])
        U[i][i] = S / L[i][i]
        L[i][i] = S / U[i][i]
        for j in range(i+1,n): #loop para calcular a matriz triangular inferior
            U[i][j] = 1/L[i][i]*(A[i][j] - sum([L[i][k] * U[k][j] for k in range(n - 1)]))
            L[j][i] = 1/U[i][i]*(A[j][i] - sum([L[j][k] * U[k][i] for k in range(n - 1)]))

    return L, U #retorna a matriz L e a matriz U

#função para resolver o sistema na forma LU=B
def solve_lu(L,U,B):
    n = len(B)
    y = [0 for _ in range(n)] #cria um vetor y de zeros
    x = [0 for _ in range(n)] #cria um vetor x de zeros
    y[0]=B[0]/L[0][0] #calcula o primeiro valor de y
    for i in range(1,n): #loop para calcular todos os valores de y
        y[i]=1/L[i][i]*(B[i]-sum([L[i][j]*y[j] for j in range(n-1)]))

    for i in reversed(range(n)): #loop de traz pra frente pra calcular os valores de x
        x[i]= 1/U[i][i]*(y[i]-sum(U[i][j]*x[j] for j in range(i+1,n)))
    return x #retorna x

A, B = le_matriz('input.txt')#le a matriz do arquivo
L, U = LU(A) #chama função LU para calcular as matrizes
x = solve_lu(L,U,B)


print('Vetor solucao x(i)')
print(x)
