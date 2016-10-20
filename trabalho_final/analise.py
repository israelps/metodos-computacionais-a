import matplotlib.pyplot as plt
from scipy.constants import nano

arquivo = open('dados/saida2.txt')

x = []

for linha in arquivo:
    l = linha.split(' ')[0]
    x.append(float(l))
arquivo.close()


plt.hist(x,50, normed=1, facecolor='green', alpha=0.75)

plt.title('Concentração de Íons em uma solução aquosa\n sob efeito de um campo elétrico (placa infinita)')
plt.ylabel('Concentração de Íons')
plt.xlabel('Distância da placa')
plt.grid(True)
#plt.axis([0,25*nano,0,10000])
plt.show()
