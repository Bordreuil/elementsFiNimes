from barreElement2d import *
from elementsTools   import *
from matrixTools    import *
from visuTools      import *
#  Resolution d un probleme de structure treillis
plotUndistord = False
L_barre = 1000.     # mm
E       = 200000.  # MPa
S       = 200.     # mm**2

print '-------Definition du maillage'
s3s2 = sqrt(3.)/2.
s3 = sqrt(3.)
s2 = sqrt(2.)

coords =array([[0.,0.],                       
               [L_barre,0.],
               [2.*L_barre,0.],
               [3.*L_barre,0.],
               [4.*L_barre,0.],
               [0.,L_barre],                       
               [L_barre,L_barre],
               [2.*L_barre,L_barre],
               [3.*L_barre,L_barre],
               [4.*L_barre,L_barre],]   ,'d') 

Du  = zeros(coords.shape,'d')

el1 = barre2D([0,1],L_barre,E,S,0.*pi/180.)
el2 = barre2D([1,2],L_barre,E,S,0.*pi/180.)
el3 = barre2D([2,3],L_barre,E,S,0.*pi/180.)
el4 = barre2D([3,4],L_barre,E,S,0.*pi/180.)
el5 = barre2D([5,6],L_barre,E,S,0.*pi/180.)
el6 = barre2D([6,7],L_barre,E,S,0.*pi/180.)
el7 = barre2D([7,8],L_barre,E,S,0.*pi/180.)
el8 = barre2D([8,9],L_barre,E,S,0.*pi/180.)
el9 = barre2D([0,5],L_barre,E,S,90.*pi/180.)
el10 = barre2D([1,6],L_barre,E,S,90.*pi/180.)
el11 = barre2D([2,7],L_barre,E,S,90.*pi/180.)
el12 = barre2D([3,8],L_barre,E,S,90.*pi/180.)
el13 = barre2D([4,9],L_barre,E,S,90.*pi/180.)
el14 = barre2D([0,6],s2*L_barre,E,S,45.*pi/180.)
el15 = barre2D([2,6],s2*L_barre,E,S,135.*pi/180.)
el16 = barre2D([3,7],s2*L_barre,E,S,135.*pi/180.)
el17 = barre2D([3,9],s2*L_barre,E,S,45.*pi/180.)

els=[el1,el2,el3,el4,el5,el6,el7,el8,el9,el10,el11,el12,el13,el14,el15,el16,el17]

plotElements(coords,els)
axis([-100,4.*L_barre+100,-100,2.*L_barre+100.])
print  '--------Definition du probleme global'
ndofs = getNumberOfDofs(coords)
            
print '\t\tNbre de ddls:',ndofs

print '--------Assemblage des matrices de rigidite elementaires'

print '--------Resolution'

print '--------Calcul des coordonnes deforme avec une magniture de:'

print '--------Visualisation de la deformee et des contraintes'
plotElements(coords,els)
show()
