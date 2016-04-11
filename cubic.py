
import matplotlib.pyplot as plt
import numpy as np



def thomas_algorithm(a, b, c, d):
    """
    Solves the Tridiagonal Linear System
          --             -- -- --   -- --
          |b_1 c_1        | |f_1|   |d_1|
          |a_2 b_2 c_2    | | . |   | . |
          |    a_3 . . .  | | . | = | . |
          |               | |   |   |   |
          |               | |   |   |   |
          |       a_n b_n | |f_n|   |d_n|
          --             -- -- --   -- --
    """
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

def cubic_spline(X):
    # Assuming constant spacing
    h = X[1] - X[0]
    N = len(X) - 1
    z_l = np.matrix('0; 0')
    z_r = np.matrix('0; 0')

    a = [np.matrix('0 0; 0 0') for i in range(N-1)]
    b = [np.matrix('0 0; 0 0') for i in range(N-1)]
    c = [np.matrix('0 0; 0 0') for i in range(N-1)]
    d = [np.matrix('0; 0') for i in range(N-1)]
    
    for i in range(N-1):
        a[i] = np.matrix('0 0; -2/h h/3')
        b[i] = np.matrix('(1-2/h) (1-(2*h)/3); (1+2/h) (1+(2*h)/3)')
        c[i] = np.matrix('2/h -h/3; 0 0')
        d[i] = np.matrix('30*h*i; 30*h*i')

    b[0] += ((h/3)/(1-(2*h)/3))*a[0]
    b[N-2] -= ((h/3)/(1+(2*h)/3))*c[N-2]
 

    f = [z_l] + thomas_algorithm(a, b, c, d) + [z_r]
    
    return f

X = np.linspace(0, 1, 11)

soln = cubic_spline(X)
print soln
print len(soln)
z, y = [], []
for ans in soln :
    z.append(ans[0,0])
    y.append(ans[1,0])
    #y = np.array(y)

plt.plot(X,y,color='r')
plt.title('h = 0.1')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('cubic.png')
plt.show()

z = np.array(z)
#plt.plot(X,z)
#plt.title('Z')
#plt.show()


