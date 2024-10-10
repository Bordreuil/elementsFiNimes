# Polytech' FQSC 2012 - Cours Mecanique des structures
#      cyril.bordreuil@univ-montp2.fr
#  Probleme : Poutre sollicitee en traction par une charge lineique
#
#  Methode de elements finis
from pylab import *
from numpy import *
from numpy.linalg import *

L_barre = 100.     # mm
E       = 200000.  # MPa
S       = 200.     # mm**2
c       = 1        # N/mm**2

Nelem  = 300          # Nombre d elements
Nnoeu  = Nelem+1    # Nombre de noeuds
Lelem  = L_barre/float(Nelem)
Xelem  = arange(0.,L_barre+Lelem,Lelem)
print('Longueur element :',Lelem)
print('Position Noeud   :',Xelem)
# Definition de la matrice globale
K      = zeros((Nnoeu,Nnoeu),'d')
print('premiere impression de la matrice globale')
print(K)
print(' adore les EF')
F      = zeros((Nnoeu,),'d')

print('---Procedure de calcul des matrices elementaires et assemblages')

for i in range(Nelem):
    print('----------Element:',i,' assemble')
    # Matrice et vecteur source elementaire
    k = E*S/Lelem*array([[1.,-1.],
                        [-1.,1.]],'d')
    f =c/Lelem*array([Xelem[i+1]**3/6.-Xelem[i]**2.*Xelem[i+1]/2+Xelem[i]**3./3.,
                      Xelem[i+1]**3/3.-Xelem[i]*Xelem[i+1]**2./2+Xelem[i]**3./6.],'d')

    K[i:i+2,i:i+2] += k
    print('Matrice de raideur au cours de l assemblage:')
    print(K)
    F[i:i+2]       += f
    #ok=input('On continue?')

print('---Resolution du probleme')
import time
tdeb=time.time()
print('Raideur total:',K)
print('Raideur du probleme:',K[1:,1:])
du = solve(K[1:,1:],F[1:])
#du  = dot(inv(K[1:,1:]),F[1:])
print(du)
print('Temps de resolution de K.u=F',time.time()-tdeb)
ok = input('On continue')
ufem=zeros((Nnoeu,),'d')
ufem[1:]=du
print('---Calcul de la solution exacte')
x      = arange(0,L_barre,1.)
uexact = c/(6.*S*E)*(3.*L_barre**2*x-x**3.)

print('---Tracer des deplacements')
plot(Xelem,ufem,'o',x,uexact,'b')
xlabel('X en mm')
ylabel('u en mm')
legend(['Rayleigh Ritz avec  EF','exacte'],loc='lower right')
figure()
title('deformation dans la poutre')
defexact=c/(6.*S*E)*(3.*L_barre**2-3.*x**2.)
plot(x,defexact)
for i in range(Nelem):
	defelem=(ufem[i+1]-ufem[i])/Lelem
	plot([Xelem[i],Xelem[i+1]],[defelem,defelem],'r',linewidth=2)
#	hold('on')
show()
