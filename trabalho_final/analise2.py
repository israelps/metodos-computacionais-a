import matplotlib.pyplot as plt
from numpy import genfromtxt
from scipy.constants import nano

arquivo = open('dados/saida3_energia.txt','rb')


x = genfromtxt(arquivo)

plt.plot(x)
plt.grid()
plt.title('Variação da Energia total do sistema')
plt.ylabel('Energia (eV)')
plt.xlabel('Iterações')
plt.grid(True)
plt.show()
