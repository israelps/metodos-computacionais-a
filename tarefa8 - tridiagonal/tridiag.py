# cabeçalho
print('-----------------------------------------------------------')
print('-------------  Aluno: Israel P. Siqueira  -----------------')
print('-----------------Matricula: 14/0144587  -------------------')
print('-----------------------------------------------------------')
print('----------  Tarefa 08 - Matrizes Tridiagonais -------------')
print('-----------------------------------------------------------')
print('')

# função que le o arquivo e monta a matriz de coeficientes e constantes
def le_matriz(caminho):
    print('Matriz de entrada: ')
    arquivo = open(caminho)  # abre arquivo
    A, B = [], []  # inicia os vetores
    for linha in arquivo:
        linha = linha.split(' ')  # separa as entradas
        linha = [float(i) for i in linha]  # converte para float
        print(linha)
        B.append(linha[-1])  # salva a ultima coluna(constantes) na matriz B
        A.append(linha[:-1])  # salva a coluna de coeficientes na matriz A
    arquivo.close()  # fecha arquivo
    return A, B  # retorna a matriz A e B

# funcao que extraí a tridiagonal da matriz lida do arquivo
def get_tridiag_matriz(A):
    n_A = []  # cria uma matriz vazia
    n = len(A)  # tamanho da matriz
    for i in range(n):
        a = A[i][i - 1]  # pega o elemento da diagonal inferior
        b = A[i][i]  # pega o elemento da diagonal
        try:  # try necessário para o caso que i=n, i+1 vai dar arrayOutOfBoundError
            c = A[i][i + 1]  # pega a diagonal superior
            n_A.append([a, b, c])  # adiciona o vetor linha na matriz
        except:
            c = 0  # caso i=n c vai ser sempre 0
            n_A.append([a, b, c])
            continue  # continua para o proximo loop
    return n_A  # retorna a matriz


def tridiag(A, B):
    A = get_tridiag_matriz(A) #extraí a tridiagonal da matriz A
    n = len(B) #n = tamanho da matriz
    x =[0 for i in range(n)] #cria um vetor de zeros do tamanho de n
    delta = [0 for i in range(n)] #cria um vetor de zeros do tamanho de n
    sigma = [0 for i in range(n)] #cria um vetor de zeros do tamanho de n
    delta[0] = A[0][1] #inicia com delta_0
    sigma[0] = B[0] #inicia com sigma_0
    for i in range(1,n):
        a = A[i][0] # elemento da diagonal inferior
        d = A[i][1] #elemento da diagonal
        c = A[i - 1][2] #elemento da diagonal superior (anterior)
        delta_ant = delta[i - 1] #valor de delta anterior
        delta[i]= d - a / delta_ant * c #calcula delta e salva no vetor
        sigma[i]= B[i] - a / delta_ant * sigma[i - 1] #calcula sigma e salva no vetor

    x[-1] = sigma[-1] / delta[-1] #calcula o valor de x_n (a notação -1 significa o ultimo elemento)

    for i in reversed(range(n - 1)): #faz um loop reverso de n - 1 até 0
        x[i] = (sigma[i] - A[i][2] * x[i + 1]) / delta[i] #calcula x e salva no vetor
    return x #retorna o vetor x

A, B = le_matriz('input.txt') #le a matriz de coeficientes A e o vetor solucao B
x = tridiag(A, B) #calcula o vetor solucao da matriz

print('Vetor solução da matriz: ')
for i in range(len(x)):
    print('x%d = %.4f'%(i,x[i]))
