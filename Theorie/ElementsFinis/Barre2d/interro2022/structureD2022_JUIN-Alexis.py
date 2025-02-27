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

coords =array([[0.,0.],
               [2.*L_barre,0.],
               [3.*L_barre,0.],
               [2.*L_barre,L_barre],
               [0.,2.*L_barre],
               [2.*L_barre,2.*L_barre],
               [3.*L_barre,2.*L_barre],
               [5.*L_barre,L_barre]]   ,'d')

imposedDofs=[8,9,14,15]  #conditions limites
#chaque point à 2ddl [8,9] bloque le point de coord [0,2L] [14,15] bloque le point de coord [5L;L]

ddlsActive = listActiveDofs(16,imposedDofs)

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

plotElements(coords,els)
axis([-100,5.*L_barre+100,-100.,2.*L_barre+100.])
print ('--------Definition du probleme global')
ndofs = getNumberOfDofs(coords)

Kglob     = zeros((ndofs,ndofs),'d')
F     = zeros((ndofs,),'d')
F[2] =-75000. #placement sur des ddl, 1er d'un point c'est selon x et 2eme selon y
F[3] =-129903.8106
figure()


print('\t\tNbre de ddls:',ndofs)

print('--------Assemblage des matrices de rigidite elementaires')

for el in els:
    k    = el.stiffness()
    ddls = el.ddls()
    conn = el.connectivite()
    Kglob=assembMatrix(Kglob,k,ddls)
    plot(coords[conn,0],coords[conn,1],'r',linewidth=2)
#printMatrix(K[4:,4:])
plot(coords[:,0],coords[:,1],'o')
axis([-100,3500,-1600.,2000.])
#show()
Kdep= Kglob.copy()

magnitude = 100.
print('--------Calcul des coordonnes deforme avec une magniture de:')
print(Du)
Coords     = coords+magnitude*Du
plot(Coords[:,0],Coords[:,1],'o')
show()
sigmas=[]
Kprob = sliceMatrix(Kglob,ddlsActive,ddlsActive)

du= linalg.solve(Kprob,F[ddlsActive])

print(nodeDdlNumber(5))

for el in els:
    ddls = el.ddls()
    sigma = el.calculContrainte(Duf[ddls])
    sigmas.append(sigma)
print(sigmas)
figure()
plotNodes(Coords)
jet = get_cmap('jet')
print('--------------Visualisation de la deformee et des contraintes')
plotContraintes(els,Coords,sigmas,jet)
axis([-100,3500,-1600.,2000.])
show()

print('--------Visualisation de la deformee et des contraintes')
plotElements(coords,els)
show()
