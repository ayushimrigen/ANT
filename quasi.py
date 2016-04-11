import sys
import numpy as np
import matplotlib.pyplot as plt


def eval_y2(y, h):
    return [(y[i+1] + y[i-1] - 2*y[i])/h**2 for i in range(1, len(y)-1)]

def eval_y1(y, h):
    return [(y[i] - y[i-1])/h for i in range(1, len(y)-1)]

def eval_y(y, h):
    return y[1:-1]
    
def evalF(B, D, F, X):
    return [(B[i] - 5*X[i]*D[i] + F[i]**2) for i in range(len(B))]

def eval_part_y2(B, D, F, X) :
    return [1 for i in range(len(B))] 

def eval_part_y1(B, D, F, X) :
    return [-5*X[i] for i in range(len(B))]

def eval_part_y(B, D, F, X) :
    return [2*F[i] for i in range(len(B))]

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
    c_ = [None for i in range(N)]
    d_ = [None for i in range(N)]
    f = [None for i in range(N)]
    c_[0] = c[0]/b[0]
    d_[0] = d[0]/b[0]

    for i in range(1, N):
        c_[i] = c[i]/(b[i] - a[i]*c_[i-1])
        d_[i] = (d[i] - a[i]*d_[i-1])/(b[i] - a[i]*c_[i-1])

    f[N-1] = d_[N-1]
    for i in range(N-2, -1, -1):
        f[i] = d_[i] - c_[i]*f[i+1]

    return f


def Quasi(initial_cond, final_cond, h):
    l, y_l = initial_cond
    r, y_r = final_cond
    N = (r - l)/h
    N = int(N)

    X = np.linspace(l, r, N)
    y_init = [((x-l)*y_r + (r-x)*y_l)/(r-l) for x in X]
    B = eval_y2(y_init,h)
    D = eval_y1(y_init,h)
    F = eval_y(y_init,h)
    A = evalF(B, D, F, X)
    C = eval_part_y2(B, D, F, X)
    E = eval_part_y1(B, D, F, X)
    G = eval_part_y(B, D, F, X)
    
    loop = 0
    while True :
        loop+=1
        
        a = [None for i in X[1:-1]]
        b = [None for i in X[1:-1]]
        c = [None for i in X[1:-1]]
        d = [None for i in X[1:-1]]
        
        for i in range(len(a)):
            a[i] = C[i]/(h**2) - E[i]/h
            b[i] = (-2*C[i]/(h**2) + E[i]/h + G[i])
            c[i] = C[i]/(h**2)
            d[i] = B[i]*C[i] + D[i]*E[i] + F[i]*G[i] - A[i]

        d[0] -= y_l*a[0]
        d[-1] -= y_r*c[-1]

        f = [y_l] + thomas_algorithm(a, b, c, d) + [y_r]
        y_init = f
        B = eval_y2(y_init,h)
        D = eval_y1(y_init,h)
        F = eval_y(y_init,h)
        A = evalF(B, D, F, X)
        C = eval_part_y2(B, D, F, X)
        E = eval_part_y1(B, D, F, X)
        G = eval_part_y(B, D, F, X)

        if( loop > 15) :
            break
        
    return X, f

X, f = Quasi((-1, 4), (1, -4), 0.1)
plt.plot(X,f)
plt.xlabel('x')
plt.ylabel('f')
plt.title('Solution using Quasi linearization \nh=0.1')
plt.savefig('Quasi_h0.1.jpg')
plt.show()
