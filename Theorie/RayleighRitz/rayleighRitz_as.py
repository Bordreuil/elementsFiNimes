#
# Polytech' FQSC 2012 - Cours Mecanique des structures
#   cyril.bordreuil@univ-montp2.fr
#  Principe Variationnel
#
#  Probleme : Poutre sollicitee en traction par une charge lineique
#
#  Methode de Rayleigh-Ritz 

from pylab import *
from numpy import *
from numpy.linalg import *

L_barre = 1000.    # mm
E       = 200000.  # MPa
S       = 200.     # mm**2
c       = 1.       # N/mm**2
print('---Mise en place pour u(x)=a_1*x+a_2*x**2')
K2=E*S*L_barre*array([[1.      ,L_barre],
		      [L_barre ,4./3.*L_barre**2.]],'d')

F2=c*L_barre**3.*array([1./3.,1./4.*L_barre],'d')

a2=solve(K2,F2)


print('---Mise en place pour u(x)=a_1*x+a_2*x**2+a_3*x**3')
K3=E*S*L_barre*array([[1.         ,L_barre          ,L_barre**2.],
		      [L_barre    ,4./3.*L_barre**2.,3./2.*L_barre**3.],
		      [L_barre**2.,3./2.*L_barre**3.,9./5.*L_barre**4.]],'d')
F3=c*L_barre**3.*array([1./3.,1./4.*L_barre,1./5.*L_barre**2.],'d')
a3=solve(K3,F3)
print(a3)
incx = 50.
x=arange(0,L_barre,incx)
print('---Calcul des deplacements pour les deux solutions')
u2   = a2[0]*x+a2[1]*x**2.
def2 = a2[0]  +2.*a2[1]*x
u3   = a3[0]*x+a3[1]*x**2.+a3[2]*x**3.
def3 = a3[0]  +a3[1]*x*2.+a3[2]*x**2.*3.
print('---Calcul de la solution exacte')
uexact=c/(6.*S*E)*(3.*L_barre**2*x-x**3.)

print('---Tracer des deplacements')
title('Deplacements')
plot(x,u2,'o',x,u3,'s',x,uexact,'b')

legend(['second ordre','troisieme ordre','exacte'],loc='lower right')
figure()
print('solution exacte:',len(uexact))
print('solution du second ordre:',len(u2))
plot(x,abs(u2-uexact)/uexact)
xlabel('position en mm',fontsize=12)
title('erreur relative deplacement')
figure()
title('deformations')
plot(x,def2,'o',x,def3,'r',linewidth=2)
xlabel('position en mm',fontsize=12)
ylabel('deformation')
figure()
plot(x,abs(def2-def3))
title('erreur absolue en deformation/contrainte')
figure()
plot(x,abs(def2-def3)/def3)
title('erreur relative en deformation/contrainte')
show()
