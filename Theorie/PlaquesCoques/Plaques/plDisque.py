from sympy import *

r  = Symbol('r')
a  = Symbol('a')
c  = Symbol('c')




E  = 210000.
nu = 0.3
h  = 5.
D  = E*h**3/12./(1.-nu)
p0 = .5
P  = 1000.
a =  200
w = c*((a**2-r**2)**2)


dwdr    = simplify(diff(w,r))
d2wdr2  = simplify(diff(dwdr,r))


print('d2wdr2:',d2wdr2)
print('dwdr:' ,dwdr)

Uloc = pi*D*((d2wdr2+dwdr/r)**2-2.*(1.-nu)/r*(dwdr*d2wdr2))*r

#print simplify(Uloc)
print(Uloc)
U = integrate(Uloc,(r,0.0,a))
print('Integrale:',U)
Wloc = 2.*pi*r*p0*w
print(Wloc)
Wext =  integrate(Wloc,(r,0.0,a))
Wext = c*((a**2)**2)*p0*pi*a**2
Pip= U-Wext

Mini = diff(Pip,c)
# print M
csol = solve(Mini,c)
print('Solution minimum:',csol,' Solution exacte:',p0/64./D)
import numpy as np

#[X,Y] = meshgrid(arange(0,a,2),arange(0,b,2))
r = np.linspace(0,a, 50)
p = np.linspace(0, 2*np.pi, 50)
r_mat,th_mat=np.meshgrid(r,p)
W      = np.array(csol*(a**2-r_mat**2)**2,dtype='d')
print(csol,a)
DWDR   = np.array(-4.*csol[0]*r_mat*(a**2-r_mat**2),dtype='d')
D2WDR2 = np.array(-4.*csol[0]*(a**2-3.*r_mat**2),dtype='d')

MR     = -D*(D2WDR2+nu*DWDR/r_mat)
SR     = MR/h**3*12*h/2.
X = r_mat*np.cos(th_mat)
Y = r_mat*np.sin(th_mat)
import matplotlib.pyplot as plt
from matplotlib import cm
plt.figure('Deplacement')
plt.contourf(X,Y,W)
plt.colorbar()
# print X.dtype, Y.dtype,W.dtype
#from mpl_toolkits.mplot3d import Axes3D
#fig =figure('Deplacement 3D')
# #ax = fig.gca(projection='3d')
#ax=Axes3D(fig)
import matplotlib
print('Matplotlib version:',matplotlib.__version__)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(X, Y, W , rstride=1, cstride=1, cmap=cm.coolwarm,
         linewidth=0, antialiased=False)
plt.figure('Contraintes')
plt.contourf(X,Y,SR)
plt.colorbar()
plt.show()
