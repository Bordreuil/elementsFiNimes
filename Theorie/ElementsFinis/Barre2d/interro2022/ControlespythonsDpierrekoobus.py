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

#position des noeuds
coords =array([[0.,0.],                      #0
               [2.*L_barre,0.],              #1
               [3.*L_barre,0.],              #2
               [2.*L_barre,L_barre],         #3
               [0.,2.*L_barre],              #4
               [2.*L_barre,2.*L_barre],      #5
               [3.*L_barre,2.*L_barre],      #6
               [5.*L_barre,L_barre]]   ,'d') #7

imposedDofs    = [4,]
valuesImposed  = [0.,0.,0.,0.]
# 7 noeuds x 2 ddl = 14 ddls
ddlsActive = listActiveDofs(14,imposedDofs)
print('Taille de coords:',coords.shape)
print('ddls actifs :', ddlsActive)


Du  = zeros(coords.shape,'d')


el1 = barre2D([0,1],2.*L_barre,E,S,0.*pi/180.)
el2 = barre2D([1,2],L_barre,E,S,0.*pi/180.)
el3 = barre2D([0,5],sqrt(2.)*2.*L_barre,E,S,45.*pi/180.)
el4 = barre2D([0,4],L_barre,E,S,90.*pi/180.)
el5 = barre2D([4,5],2.*L_barre,E,S,0.*pi/180.)
el6 = barre2D([5,6],L_barre,E,S,0.*pi/180.)
el7 = barre2D([1,3],L_barre,E,S,90.*pi/180.)
el8 = barre2D([3,5],L_barre,E,S,90.*pi/180.)
el9 = barre2D([2,3],sqrt(2.)*L_barre,E,S,135.*pi/180.)
el10 = barre2D([3,6],sqrt(2.)*L_barre,E,S,45.*pi/180.)
el11 = barre2D([2,6],2.*L_barre,E,S,90.*pi/180.)
el12 = barre2D([6,7],sqrt(5.)*L_barre,E,S,-63.*pi/180.)
el13 = barre2D([2,7],sqrt(5.)*L_barre,E,S,63.*pi/180.)


els=[el1,el2,el3,el4,el5,el6,el7,el8,el9,el10,el11,el12,el13]

#Force applique
Kglob     = zeros((14,14),'d')
F     = zeros((14,),'d')
F[4] =5000
F[9] =5000
figure()
print('--------Assemblage des matrices de rigidite elementaires')
for el in els:
    k    = el.stiffness()
    ddls = el.ddls()
    conn = el.connectivite()
    Kglob=assembMatrix(Kglob,k,ddls)
    plot(coords[conn,0],coords[conn,1],'r',linewidth=2)

plotElements(coords,els)
axis([-100,5.*L_barre+100,-100.,2.*L_barre+100.])
print ('--------Definition du probleme global')
ndofs = getNumberOfDofs(coords)

print('\t\tNbre de ddls:',ndofs)

print('--------Assemblage des matrices de rigidite elementaires')

print('--------Calcul des coordonnes deforme avec une magniture de:')

print('--------Visualisation de la deformee et des contraintes')
plotElements(coords,els)
show()
