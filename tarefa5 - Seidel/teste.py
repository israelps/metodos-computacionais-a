import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import e, epsilon_0, pi
from scipy.optimize import minimize

k = 1/(4*pi*epsilon_0)

def V(x):
    r = [[-1.4,-1.4,-1.4],[1.4,1.4,-1.4],[1.4,-1.4,1.4],[-1.4,1.4,1.4]]
    r_ = [[1.4,-1.4,-1.4],[-1.4,1.4,-1.4],[-1.4,-1.4,1.4],[1.4,1.4,1.4]]
    pot=0
    for i in r:
        pot -= k*e/(((x[0]-i[0])**2+(x[1]-i[1])**2+(x[2]-i[2])**2)**(1/2))
    for i in r_:
        pot += k*e/(((x[0]-i[0])**2+(x[1]-i[1])**2+(x[2]-i[2])**2)**(1/2))
    return pot
a=0
X,U = [],[]
print('x y z -- V')
for i in range(1,15):
    for k in range(1,i):
        for j in range(0,k):
            x = [i/10,k/10,j/10]
            X.append(np.linalg.norm(x))
            vx = V(x)
            U.append(vx)
            y = [-i/10,-k/10,-j/10]
            vy = V(y)
            X.append(-np.linalg.norm(y))
            U.append(vy)
            a+=1
            print(x,vx,y,vy)
print(a)
plt.plot(X,U,'o')
plt.xlabel('R')
plt.ylabel('V(r)')
plt.show()
