import numpy as np

from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rcParams
#from JSAnimation.IPython_display import display_animation
from matplotlib import animation

rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16

fig = pyplot.figure()
ax = fig.gca(projection='3d')

dx = 0.05
dt = 0.005
# Range of X and T
rX = 2
rT = 1
m = int(rX/dx)
n = int(rT/dt)

x = [(-1+i*dx) for i in range(0,m+1)]
yo=[1]
y = [1 for i in range(1,m)]
yo.extend(y)
yo.append(1)
X = np.linspace(-1, 1, m+1)
Y = np.linspace(0, rT, n)
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

def crank_nikolson(c, v):

    U = np.zeros((n, m+1), dtype=np.float32)
    U[:, 0] = 0
    U[:, m] = 0
    U[0,:] = np.cos(np.pi*X/2)
    for k in range(1, n-1):
        A = [v/dx**2 + c/(2*dx) for i in range(1, m)]
        B = [-(2*v)/(dx**2) - 2/dt for i in range(1, m)]
        C = [v/dx**2 - c/(2*dx) for i in range(1, m)]
        D = [U[k-1, j]*((2*v)/(dx**2) - 2/dt) - U[k-1, j-1]*((v)/(dx**2) + c/(2*dx)) - U[k-1, j+1]*((v)/(dx**2) - c/(2*dx)) for j in range(1,m)]
        D[0] = D[0] - U[k, 0]*(v/(dx**2) + c/(2*dx))
        D[m-2] = D[m-2] - U[k,m]*((v/dx**2) - c/(2**dx))
        U[k, 1:m ] = np.array(thomas_algorithm(A, B, C, D))
    return U


fig = pyplot.figure(figsize=(8,5))
# ax = pyplot.axes()
pyplot.axis([-1, 1, 0, 1.5])
line = pyplot.plot([], [], color='#003366', ls='--', lw=3)[0]


def init():
    line.set_data([], [])
    return line,
c = ['r','b','g','c','m','y']



def animate(i):
    u = crank_nikolson(0, 1)
    line.set_data(X, u[i, :])
    pyplot.title('Time='+str(i*0.05))
    return line

u = crank_nikolson(0, 1)
for i in range(1,n):
    ax.plot(x,yo,u[i,:],color='r')

anim = animation.FuncAnimation(fig, animate, 
                               frames=n, interval=100)
print u
ax.set_xlabel('X')
ax.set_ylabel('U', fontsize=10)
ax.set_zlabel('Time', fontsize=10)
ax.set_title('Crank Nicolson Method\ndx=0.05, dt=0.005')
fig.savefig('crank1_dx0.05_dt0.005.png')
#plt.show()
pyplot.xlabel('X')
pyplot.ylabel('U')


pyplot.show()

