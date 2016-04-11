
#Ayushi Mrigen
#13MA20053

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


def A(x):
    return 2*x

def B(x):
    return 2
def C(x):
    return 4*x

def ai(x,h):
    return (-A(x)/(2*h) + 1/(h*h) )

def bi(x,h):
    return (B(x) - 2/(h*h))

def ci(x,h):
    return (1/(h*h) + A(x)/(2*h))

def di(x,h):
    return C(x)


xinitial = 0
xfinal = 0.5
yinitial = 1
yfinal = 1.279
h = 0.02

i=xinitial+h
k=1
n = []
xpoints = []
ypoints=[]
while i<xfinal:
    xpoints.append(i)
    n.append(k)
    i = i+h
    k=k+1


dmatrix = []
Amatrix = []
Bmatrix = []
Dmatrix = []
k=1

# Code for Thomas Algorithm

for i in xpoints:
    temp = []
    temp1 = []
    a=ai(i,h)
    b=bi(i,h)
    c=ci(i,h)
    d=di(i,h)
    if(k==1):
        d = d -a*yinitial
       
        Dmatrix.append(d/b)
    else:
       
        if(k==len(n)):
            d=d-c*yfinal
            
     
        Dmatrix.append((d-(a*Dmatrix[k-2]))/(b-(a*Bmatrix[k-2][k-1])))
        
    dmatrix.append(d)
    for j in n:
        if(j==k-1):
            temp.append(a)
            temp1.append(0)
        else:
            if(j==k):
                temp.append(b)
                temp1.append(1)
            else: 
                if(j==k+1):
                    temp.append(c)
                    if(k==1):
                        temp1.append(c/b)
                    else:
                        temp1.append(c/(b-(a*Bmatrix[k-2][k-1])))
                else:
                    temp.append(0)
                    temp1.append(0)
   
    Amatrix.append(temp)
    Bmatrix.append(temp1)
    k=k+1

#print 'A= ',Amatrix
#print 'd = ',dmatrix
#print 'B = ',Bmatrix
#print 'd = ',Dmatrix

ypoints = []

k = len(n)
ypoints = [Dmatrix[k-1]]
k=k-1
i=0

#Finding the final values of y
while(k>=1):
    
    ypoints = [Dmatrix[k-1] - Bmatrix[k-1][k]*ypoints[0]] + ypoints
    k=k-1
    i=i+1



xpoints = [xinitial] + xpoints + [xfinal]
ypoints = [yinitial] + ypoints + [yfinal]

i=0
while(i < len(xpoints)):
    print'x= ',xpoints[i] , ' \t y=' , ypoints[i]
    i=i+1
plt.title('Finite difference method with h = '+str(h))
plt.plot(xpoints,ypoints,color='r',marker='o')
plt.draw()
plt.savefig("Question4_plot.png")

plt.show()
        
