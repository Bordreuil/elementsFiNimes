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
print(csol,p0/64./D)
from pylab import *

#[X,Y] = meshgrid(arange(0,a,2),arange(0,b,2))
r = linspace(0,a, 50)
p = linspace(0, 2*np.pi, 50)
r_mat,th_mat=meshgrid(r,p)
W      = array(csol*(a**2-r_mat**2)**2,dtype='d')
print(csol,a)
DWDR   = array(-4.*csol[0]*r_mat*(a**2-r_mat**2),dtype='d')
D2WDR2 = array(-4.*csol[0]*(a**2-3.*r_mat**2),dtype='d')
MR     = -D*(D2WDR2+nu*DWDR/r_mat)
SR     = MR/h**3*12*h/2.
X = r_mat*cos(th_mat)
Y = r_mat*sin(th_mat)
figure('Deplacement')
contourf(X,Y,W)
colorbar()
# print X.dtype, Y.dtype,W.dtype
from mpl_toolkits.mplot3d import Axes3D
fig =figure('Deplacement 3D')
# #ax = fig.gca(projection='3d')
ax=Axes3D(fig)
surf = ax.plot_surface(X, Y, W , rstride=1, cstride=1, cmap=cm.coolwarm,
         linewidth=0, antialiased=False)
figure('Contraintes')
contourf(X,Y,SR)
colorbar()
show()
