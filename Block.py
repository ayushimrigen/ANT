from __future__ import division
import sys
import numpy as np
import matplotlib.pyplot as plt

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


def test_BVP(l, r, h):
    
   

    N = (r - l)/h
    N = int(N)
    z_l = np.matrix('0; 0')
    z_r = np.matrix('0; 0')
    
    a = [np.matrix('0 0; 0 0') for i in range(N-1)]
    b = [np.matrix('0 0; 0 0') for i in range(N-1)]
    c = [np.matrix('0 0; 0 0') for i in range(N-1)]
    d = [np.matrix('0; 0') for i in range(N-1)]

    for i in range(N-1):
        a[i] = np.matrix('-1/(h**2) 0; 0 1/(h**2)')
        b[i] = np.matrix('(2/(h**2) 1; 81 -2/(h**2)')
        c[i] = np.matrix('-1/(h**2) 0; 0 1/(h**2)')
        d[i] = np.matrix('0; 81*((i*h)**2)')
    d[0] -= a[0]*z_l
    d[N-2] -= c[N-2]*z_r

    f = [z_l] + thomas_algorithm(a, b, c, d) + [z_r]
    return f

l = 0
r = 1.
h = 0.01
soln = test_BVP(l, r, h)
for i in soln:
	for j in i:
		print j , '\t',
	print
X = np.linspace(l, r, (r-l)/h+1)
z, y = [], []
for ans in soln :
    z.append(ans[0,0])
    y.append(ans[1,0])
y = np.array(y)
print X.shape, y.shape
plt.xlabel('x')
plt.ylabel('y')
plt.plot(y)
plt.savefig("BlockTrigonalSolution_h0.01.png")
plt.title('Block Trigonal method with h = '+str(h))
plt.show()
