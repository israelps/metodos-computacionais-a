import matplotlib.pyplot as plt
from scipy.constants import nano

arquivo = open('dados/saida3.txt')

z1 = []
z2 = []
for linha in arquivo:
    l = linha.split(' ')
    if int(l[0])==1:
        z1.append([float(l[2]),float(l[3]),float(l[4])])
    if int(l[0]==2):
        z2.append([float(l[2]),float(l[3]),float(l[4])])

arquivo.close()


plt.hist(z1, 50, normed=1, facecolor='green', alpha=0.75)
plt.hist(z2, 50, normed=1, facecolor='blue', alpha=0.75)

plt.title('Concentração de Íons em uma solução aquosa\n sob efeito de um campo elétrico (placa infinita)')
plt.ylabel('Concentração de Íons')
plt.xlabel('Distância da placa')
plt.grid(True)
# plt.axis([0,25*nano,0,10000])
plt.show()
