from __future__ import division
import sys
import numpy as np
import matplotlib.pyplot as plt

def thomas_algorithm(a, b, c, d):
    C = [c[0]/b[0]]
    D = [d[0]/b[0]]
   
    for i in range (1,len(xarr) -2):
       
        C.append(c[i]/(b[i] - a[i]*C[i-1]))
        D.append((d[i] - a[i]*D[i-1])/(b[i] - a[i]*C[i-1]))
   
    y = [0] * (len(xarr) - 1)
    n = len(xarr) -1
    i = n-2
    y[len(D)-1]= D[len(D)-1]
    while i>=0 :
      y[i] = D[i] - C[i]*y[i+1]
      i= i -1
    #y.append(0)
    y.insert(0,0)

    return y



def Newton(x,yk,h,k):
    a = []
    b = []
    c = []
    d = []
    for i in range (1,len(xarr)-1):
        a.append(1/(h*h));
        b.append(-2/(h**2) - 3*((1+x[i]+yk[i])**2)/2)
        c.append( 1/(h**2))
        d.append(( ((1+x[i]+yk[i])**3)/2 -(yk[i+1] - 2*yk[i] + yk[i-1])/(h**2)))
    f=thomas_algorithm(a,b,c,d)

    E = 0
    
    print "At k = ",k
    k=k+1
    for i in range (1,len(yk)-1):
        if abs(f[i])>E:
            E = abs(f[i])
        yk[i] = yk[i] + f[i];
        print x[i] ,"\t" ,yk[i]
    if E>0.0000001:
        if(k==1):
            plt.plot(x,yk,linestyle='--',label='Intermediate solutions',color='b' )
        else:
            plt.plot(x,yk,linestyle='--',color='b' )
 
        print "\n\n\n"
        Newton(x,yk,h,k)
        
    else:
       plt.plot(x,yk,color='r',label='Final solution') 
        


h = 0.01
yat0 = 0
yat1 = 0
xarr = []
yk = []
n = int((1-0)/h)
print n
for i in range (n):
   xarr.append(i*h)
   yk.append(0)
xarr.append(1)
yk.append(0)

Newton(xarr,yk,h,0)

plt.title('Newtons linearization technique with h = '+str(h))

plt.draw()
plt.legend()
plt.savefig("newton1_h0.01.png")

plt.show()
        
