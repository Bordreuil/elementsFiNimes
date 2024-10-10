from numpy import *
#import numpy.linalg as la
from numpy.linalg import *
from pylab import *
# Definition des variables du probleme
E = 210000.
S =  2500.
c =  1.
L =  1000.
# definition de la matrice de raideur
K=E*S*array([[L,L**2],
         [L**2,4./3.*L**3]],'f')

F = c*array([L**3./3.,L**4./4.],'f')

# recherche des coefficients a1 et a2
a=solve(K,F)

inc = 100.

x=arange(0.,L+inc,inc)
figure('Deplacements')
plot(x,a[0]*x+a[1]*x**2) # solution de Rayleigh ritz
plot(x,c/6./E/S*(3.*L**2*x-x**3.),'o') # solution exacte

figure('Deformations')
plot(x,a[0]+2*a[1]*x)
plot(x,c/6./E/S*(3*L**2-3.*x**2),'o')
show()
