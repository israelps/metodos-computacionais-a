# cabeçalho
print('-----------------------------------------------------------')
print('-------------  Aluno: Israel P. Siqueira  -----------------')
print('-----------------Matricula: 14/0144587  -------------------')
print('-----------------------------------------------------------')
print('--------------  Tarefa 07 - Runge Kutta -------------------')
print('-----------------------------------------------------------')
print('')

from math import exp, fabs,cos,sin
import matplotlib.pyplot as plt

# função que calcula a derivada da função usando o método de runge-kutta
# recebe uma função F como parametro, y0, os intervalos de integracao e
# o numero de iteracoes
# metodo de runge-kutta de 2 ordem.
def runge_2kuta(F, y0, a, b, n):
    h = (b - a) / n #calcula tamanho do passo
    x = a
    y = y0
    for i in range(1, n + 1):
        y = y + h * F(x + h / 2, y + h / 2 * F(x, y))
        x = a + i * h
    return y

# função que calcula a derivada da função usando o método de runge-kutta
# recebe uma função F como parametro, y0, os intervalos de integracao e
# o numero de iteracoes
# metodo de runge-kutta de 4 ordem.
def runge_4kuta(F, y0, a, b, n):
    h = (b - a) / n  # calcula o tamanho do passo
    x = a
    y = y0
    for i in range(1, n + 1):
        k1 = h * F(x, y)
        k2 = h * F(x + h / 2, y + k1 / 2)
        k3 = h * F(x + h / 2, y + k2 / 2)
        k4 = h * F(x + h, y + k3)

        y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x = a + i * h
    return y

#Algoritimo de Runge-Kutta-Fehlberg
#Runge-Kutta de 6a ordem com controle de erro (truncamento)
#recebe
def runge_kutta_fehlberg(F, y0, a, b, tol, hmax, hmin):
    x = a
    y = y0
    h = hmax
    FLAG = 1
    print(x, y)
    while FLAG == 1:
        k1 = h * F(x, y)
        k2 = h * F(x + 1 / 4 * h, y + 1 / 4 * k1)
        k3 = h * F(x + 3 / 8 * h, y + 3 / 32 * k1 + 9 / 32 * k2)
        k4 = h * F(x + 12 / 13 * h, y + 1932 / 2197 *
                   k1 - 7200 / 2197 * k2 + 7296 / 2197 * k3)
        k5 = h * F(x + h, y + 439 / 216 * k1 - 8 * k2 +
                   3680 / 513 * k3 - 845 / 4104 * k4)
        k6 = h * F(x + 1 / 2 * h, y - 8 / 27 * k1 + 2 * k2 -
                   3544 / 2565 * k3 + 1859 / 4104 * k4 - 11 / 40 * k5)
        R = 1 / h * fabs((1 / 360 * k1 - 128 / 4275 * k3 - 2197 /
                          75240 * k4 + 1 / 50 * k5 + 2 / 55 * k6))
        delta = 0.84 * (tol / R)**(1 / 4)
        delta = float('%.5f' % delta)
        if R <= tol:
            x = x + h
            y = y + 25 / 216 * k1 + 1408 / 2565 * k3 + 2197 / 4104 * k4 - 1 / 5 * k5
            print('%.8f %.8f %.8f %e %.6f' % (x, y, h, R, delta))
        if delta <= 1:
            h = delta * h
        elif delta >= 4:
            h = 4 * h
        else:
            h = 8 * h
        if h > hmax:
            h = hmax
        if x >= b:
            FLAG = 0
        elif (x + h) > b:
            h = b - x
        elif h < hmin:
            FLAG = 0
            print('h minimo excedido, procedimento sem sucesso')


# função de teste
def f(x, y): return x + y

# derivada analitica da função de testes
def f_(x, y): return exp(x) - x - 1

# loop de teste para verificar o crescimento do erro
print('Calculando o erro relativo para varios valores de N')
n = 10
print('{0:15s} {1:15s} {2:15s}'.format('iteracoes','2 ordem','4 ordem'))

for k in range(10):
    y0 = 0
    a, b = 0, 2

    k2 = runge_2kuta(f, y0, a, b, n)
    err_ = fabs(k2 - f_(b, a))
    k4 = runge_4kuta(f, y0, a, b, n)  # chama o método de runge-kutta
    err = fabs(k4 - f_(b, a))  # calcula o erro
    print('{0:<15d} {1:<15.0e} {2:<15.0e} '.format(n,err_, err))
    n += 10

print('podemos notar que o metodo de 4 ordem é mais eficiente em relacao')
print('ao numero de passos e numero de calculos de função por exemplo:')
print('o Runge-Kutta de 2 ordem com 40 calculos de função (20 iteracoes)')
print('obtem um erro de e^(-2), enquanto o de 4 ordem (10 iteracoes) e^(-4) ')
# função x**3
def g(x, y): return x**3

y0 = 0  # F(0)=0
a, b = 0, 1  # intervalo de integração
n = 10 #numero de intervalos
print()
print('Calcula a equacao diferencial [ dy/dx=x**3 ] no ponto x(0)=0 pelo metodo de Runge-Kutta')
print('dF(x) = x^3')
print('F(0) = %.6f' % runge_4kuta(g, y0, a, b, n))
