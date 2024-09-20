from sympy import * #  Import du module de calcul symbolique

x  = Symbol('x') # Definition de la variable x
y  = Symbol('y')
a  = Symbol('a')
b  = Symbol('b')
c  = Symbol('c')
D  = Symbol('D')
nu = Symbol('nu')

a =  200.
b =  200.

E  = 210000.
nu = 0.3
h  = 10.
D  = E*h**3/12./(1-nu**2)
p0 = 1

w = c*sin(pi/a*x)*sin(pi/b*y)
# Encastrement
#w = c*(x**4/a**4-2*x**3/a**3+x**2/a**2)*(y**4/b**4-2.*y**3/b**3.+y**2/b**2)
dwdx    = diff(w,x)
d2wdx2  = simplify(diff(dwdx,x))    # derivee seconde de w par rapport a x
d2wdxdy = simplify(diff(dwdx,y))
dwdy    = diff(w,y)
d2wdy2  = simplify(diff(dwdy,y))    # idem par rapport à y

print('d2wdx2:',d2wdx2)
print('d2wdy2:',d2wdy2)
print('d2wdxdy:',d2wdxdy)

Uloc = 0.5*D*((d2wdx2+d2wdy2)**2-2.*(1.-nu)*(d2wdx2*d2wdy2-d2wdxdy**2))       # energie de deformation sur un petit element de surface dx dy
print('integral terme1',integrate(integrate(d2wdx2**2+d2wdy2**2,(y)),(x)))
#print simplify(Uloc)

U = integrate(integrate(Uloc,(y,0,b)),(x,0,a))                                # energie elastique en flexion sur toute la plaque
print(U)
Wloc = p0*sin(pi/a*x)*sin(pi/b*y)*w
#Wloc = p0*w   
# travail des forces exterieures sur un element de dx dy
# Wloc = p0*w                                                                 # decommenter pour traiter le cas d'une plaque appuye appuye soumis  a une pression constante

Wext =  integrate(integrate(Wloc,(y,0,b)),(x,0,a))                            # sur toute la plaque

Pip= U-Wext                                                                   # Calcul de l energie potentielle

Mini = diff(Pip,c)                                                            # differentiation de l energie potentielle

csol   = solve(Mini,c)                                                        # Recherche de la valeur de c qui rend la derivee nulle
cexact = p0/D/(3.14116**4*(1./a**2+1./b**2)**2)                                 
print('Csol:',csol,'cexact:',cexact)

from numpy import *


[X,Y] = meshgrid(arange(0,a,2),arange(0,b,2))
W =array(csol*sin(pi/a*X)*sin(pi/b*Y),dtype='d')
D2WDX2 = -W*(pi/a)**2
D2WDY2 = -W*(pi/b)**2
#Encastrement
#W = array(csol*(X**4/a**4-2*X**3/a**3+X**2/a**2)*(Y**4/b**4-2.*Y**3/b**3.+Y**2/b**2),dtype='d')

#print 'max w:', max(W.all())
#from pylab import *
#  On va tracer sur un graphe 

import matplotlib.pyplot as plt
from matplotlib import cm
plt.contourf(X,Y,W)
plt.colorbar()
plt.axis('equal')
plt.figure('Contraintes en flexion XX')
SXX = E/(1-nu**2)*h/2.*(D2WDX2+nu*D2WDY2)
plt.contourf(X,Y,SXX)
plt.colorbar()
plt.axis('equal')
# from mpl_toolkits.mplot3d import Axes3D
# fig =figure('Deplacement')
# ax = fig.gca(projection='3d")
# Attention valable en version matplotlib 3.7
import matplotlib
print('Matplotlib version:',matplotlib.__version__)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(X, Y, W , rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
plt.show()
