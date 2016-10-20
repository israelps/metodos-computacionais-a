# cabeçalho
print('-----------------------------------------------------------')
print('-------------  Aluno: Israel P. Siqueira  -----------------')
print('-----------------Matricula: 14/0144587  -------------------')
print('-----------------------------------------------------------')
print('------------  Tarefa 06 - Metodo de Euler -----------------')
print('-----------------------------------------------------------')
print('')

from math import exp, fabs

#função de teste
def f(x, y):
    return x + y

#derivada analitica da função de testes
def f_(x):
    return exp(x) - x - 1

#função x**3
def g(x,y):
    return x**3

#função que calcula a derivada da função usando o étodo de Euler
#recebe uma função F como parametro, x0,y0, os intervalos de integracao e o numero de iteracoes
def euler(F, x0, y0, a, b, n):
    x, y = x0, y0
    h = (b - a) / n #calcula o tamanho do passo
    for i in range(1, n + 1): #faz a integral
        y += F(x, y) * h
        x = a + i * h
    return y


n = 100
#loop de teste para verificar o crescimento do erro
print('Calculando o erro relativo para varios valores de N')
for k in range(6):
    x0, y0 = 0, 0
    x, y = x0, y0
    a, b = 0, 2

    y = euler(f, x0, y0, a, b, n)#chama o método de euler

    err = fabs(y - f_(b)) #calcula o erro
    print('erro relativo: %.2e, Numero de iteracoes: %d' % (err, n))

    n += 200

x0,y0=0,0 # F(0)=0
a,b = 0,1 #intervalo de integração

print()
print('Calcula a equacao diferencial no ponto x(0)=0')
print('dF(x) = x^3')
print('F(0) = %.4f'%euler(g,x0,y0,a,b,n))
print('Podemos ver que a precisao do método depende do numero de "particoes" da funcao')
print('ao plotar o grafico do erro x numero de particoes notou-se que o erro cai de forma exponencial')
print('quanto maior o numero de particoes menor o erro.')
