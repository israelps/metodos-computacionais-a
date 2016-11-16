import matplotlib.pyplot as plt
from numpy import genfromtxt
from scipy.constants import nano

arquivo = open('dados/saida3_energia.txt','rb')


x = genfromtxt(arquivo)

plt.plot(x)
plt.show()
'''
plt.title('Concentração de Íons em uma solução aquosa\n sob efeito de um campoelétrico (placa infinita)')
plt.ylabel('Concentração de Íons')
plt.xlabel('Distância da placa')
plt.grid(True)
# plt.axis([0,25*nano,0,10000])
plt.show()
'''
