import sys
sys.path.append('..')

from barreElement2d import *
from elementsTools   import *
from matrixTools    import *
from visuTools      import *
#  Resolution d un probleme de structure treillis
plotUndistord = False
L_barre = 1000.     # mm
E       = 200000.  # MPa
S       = 200.     # mm**2

print('-------Definition du maillage')
s3s2 = sqrt(3.)/2.
s3 = sqrt(3.)
s2 = sqrt(2.)

coords =array([[0.,0.],                       
               [L_barre,0.],
               [L_barre,L_barre],
               [L_barre+s3*L_barre,L_barre],]   ,'d') 

Du  = zeros(coords.shape,'d')

el1 = barre2D([0,1],L_barre,E,S,0.*pi/180.)
el2 = barre2D([0,2],s2*L_barre,E,S,45.*pi/180.)
el3 = barre2D([1,2],L_barre,E,S,0.*pi/180.)
el4 = barre2D([1,3],2.*L_barre,E,S,30.*pi/180.)
el5 = barre2D([2,3],s3*L_barre,E,S,0.*pi/180.)


els=[el1,el2,el3,el4,el5]

plotElements(coords,els)
axis([-100,3.*L_barre+100,-100,2.*L_barre+100.])
print ('--------Definition du probleme global')
ndofs = getNumberOfDofs(coords)
            
print('\t\tNbre de ddls:',ndofs)

print('--------Assemblage des matrices de rigidite elementaires')

print('--------Resolution')

print('--------Calcul des coordonnes deforme avec une magniture de:')

print('--------Visualisation de la deformee et des contraintes')
plotElements(coords,els)
show()
