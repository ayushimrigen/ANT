from __future__ import division
import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt

Ep = 0.0001
fig = plt.figure()
ax = fig.gca(projection='3d')

def f(x,y):
    return x**2 + y**2

def gauss(u,x,y):
    U = u
    h = x[1]-x[0]
    max = 0
    for i in range(1,len(u)-1):
        for j in range(1,len(u[0])-1):
            U[i][j] = ((U[i-1][j] + U[i][j-1] + u[i+1][j] + u[i][j+1]) - (h**2)*f(x[i],y[j]) )/4
            if abs(U[i][j] - u[i][j]) > max :
                max = abs(U[i][j] - u[i][j])
   
    
    #print U
    if max>Ep:
        gauss(U)
    else:
        return u



x = np.linspace(0,1,10)
y = np.linspace(0,1,10)

ui = [[0 for i in range(len(y))] for i in range(len(y))] 

U = gauss(ui,x,y)

#for i in range(len(x)):
 #   print U[i]
np.matrix(U)
#ax.plot(y,x,U)
ax.set_xlabel('X')
ax.set_ylabel('Y', fontsize=10)
ax.set_zlabel('U', fontsize=10)
ax.plot_surface(y, x, U, cstride=1,rstride=1,cmap=cm.jet)
plt.title('Five point method using Gauss-Siedal iterations')

plt.savefig("fivePt.jpg")
plt.show()



