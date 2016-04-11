from __future__ import division
import sys
import numpy as np
import matplotlib.pyplot as plt

def thomas_algorithm(a, b, c, d):

    assert len(a) == len(b) == len(c) == len(d)
    N = len(c)
    c_ = [np.matrix('0 0; 0 0') for i in range(N)]
    d_ = [np.matrix('0 ; 0') for i in range(N)]
    b_inv = [np.matrix('0 0; 0 0') for i in range(N)]
    f = [np.matrix('0 ; 0') for i in range(N)]
    b_inv[0] = b[0].getI()
    c_[0] = b_inv[0]*c[0]
    d_[0] = b_inv[0]*d[0]

    for i in range(1, N):
        b_inv[i] = (b[i] - a[i]*c_[i-1]).getI()
        c_[i] = b_inv[i]*c[i]
        d_[i] = b_inv[i]*(d[i] - a[i]*d_[i-1])

    f[N-1] = d_[N-1]
    for i in range(N-2, -1, -1):
        f[i] = d_[i] - c_[i]*f[i+1]

 
    return f



def Newton(x,yk,h,k):
    N = len(x)-1
    a = [np.matrix('0 0; 0 0') for i in range(N-1)]
    b = [np.matrix('0 0; 0 0') for i in range(N-1)]
    c = [np.matrix('0 0; 0 0') for i in range(N-1)]
    d = [np.matrix('0; 0') for i in range(N-1)]
    fk=[]
    Fk=[]
    for ans in yk:
        fk.append(ans[0,0])
        Fk.append(ans[1,0])

    for i in range (1,N):
         a[i-1] =np.matrix([[-1,-h/2],[ 0, 1/(h**2)-fk[i]/(2*h)]])
         b[i-1]= np.matrix([[1,-h/2],[(Fk[i+1]-Fk[i-1])/(2*h),-2/(h**2)-2*Fk[i]]])
         c[i-1] = np.matrix([[0,0],[0,1/(h**2)+fk[i]/(2*h)]])
         d[i-1] =np.matrix([[-(fk[i]-fk[i-1]-h*(Fk[i]+Fk[i-1])/2)],[-((Fk[i+1]-2*Fk[i]+Fk[i-1])/(h**2)+(fk[i]*(Fk[i+1]-Fk[i-1])/(2*h)+1-(Fk[i])**2))]])



    f=thomas_algorithm(a,b,c,d)

    E = 1000
    maxm = 0
    print "At k = ",k
    k=k+1
    for i in range (1,len(yk)-1):
        if (abs(f[i-1][0,0])<E):
            E = abs(f[i-1][0,0])
        if (abs(f[i-1][0,0])>maxm):
            maxm = abs(f[i-1][0,0])
        yk[i] = yk[i] + f[i-1]
        print x[i] ,"\t" ,yk[i][0,0]

    fk=[]
    for ans in yk:
        fk.append(ans[0,0])
      
    #c=input()
    if E>(0.00001):
     
        if(k==1):
            plt.plot(x,fk,linestyle='--',label='Intermediate solutions',color='b' )
        else:
            plt.plot(x,fk,linestyle='--',color='b' )
            
        print "\n\n\n"
        f= Newton(x,yk,h,k)

        
    else:
        plt.plot(x,fk,color='r',label='Final solution') 
        


h = 0.05
yat0 = 0
yat10 = 1

n = int((10-0)/h)


xarr = [(i*h) for i in range (n+1)]

yk= [np.matrix('1.0; 1.0') for i in range(n+1)]

for i in range (n+1):
   
    yk[i][0,0] = (((i*h)**3)*yk[i][0,0])/300
    yk[i][1,0] = (((i*h)**2)*yk[i][1,0])/100



Newton(xarr,yk,h,0)

plt.title('Newtons linearization technique with h = '+str(h))

plt.draw()
plt.legend()
plt.savefig("newton2_h0.05.png")

plt.show()
        
