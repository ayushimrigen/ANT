import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
def fy(x,y,z):
    return z

def fz(x,y,z):
    return y

#Fourth Order Runge Kutta Method
def rK3(a, y,z,  hs):
    k0 = fy(a,y, z)*hs
    l0 = fz(a,y, z)*hs
   
    yk = y + k0*0.5
    zk = z + l0*0.5
   
    k1 = fy(a + 0.5*hs,yk, zk)*hs
    l1 = fz(a+0.5*hs,yk, zk)*hs
   
    yk = y + k1*0.5
    zk = z + l1*0.5
    
    k2 = fy(a+0.5*hs,yk, zk)*hs
    l2 = fz(a+0.5*hs,yk, zk)*hs
   
    yk = y + k2
    zk = z + l2
  
    k3 = fy(a+h,yk, zk)*hs
    l3 = fz(a+h,yk, zk)*hs
    
    y = y + (k0 + 2*(k1 + k2) + k3)/6
    z = z + (l0 + 2*(l1 + l2) + l3)/6
  
    return y, z 

x0=0
x1=1
yat0=0
yat1=-1
plt.axis([0,1,-1,0])
plt.xlabel('x')
plt.ylabel('y')
plt.ion()
plt.show()
alpha0=0.3
alpha1=0.4
h=0.05


xgraph=[]
x=0
while(x<=1):
    xgraph.append(x)
    x+=h

#Loop continues till it converges
while (alpha0 - alpha1 >0.000005) or (alpha1 - alpha0 > 0.000005 ):
    x=0
    (y0,z0)=(yat0,alpha0)
    (y1,z1)=(yat0,alpha1)
    ygraph=[]

    
    while(x<=1):
        ygraph.append(y1)
        (y0,z0) = rK3(x,y0,z0,h)
        (y1,z1) = rK3(x,y1,z1,h)
       
        x=x+h
    

    plt.title('Alpha ='+str(alpha1))
    plt.plot(xgraph,ygraph,color='b',marker='o')
    plt.draw()
    time.sleep(0.5)
    alpha2 = alpha0 - (alpha1 - alpha0)*((y0 - yat1)/(y1 - y0))

    alpha0 = alpha1
    alpha1 = alpha2


print '\nAlpha = ' , alpha2
plt.title('Alpha ='+str(alpha2))
i=0
ygraph = ygraph + [yat1]
xgraph = xgraph + [x1]
while i<len(xgraph):
    print 'x= ',xgraph[i],'\ty= ',ygraph[i]
    i=i+1
plt.plot(xgraph,ygraph,color='r',marker='o')
plt.draw()
plt.savefig("Question2_plot.png")
time.sleep(0.5)
plt.show()
time.sleep(1)

plt.close('all')

